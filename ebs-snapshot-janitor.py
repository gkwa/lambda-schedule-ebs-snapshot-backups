import boto3
import re
import datetime
from datetime import date, timedelta

ec = boto3.client('ec2')
iam = boto3.client('iam')

"""
This function looks at *all* snapshots that have a "DeleteOn" tag containing
the current day formatted as YYYY-MM-DD. This function should be run at least
daily.
"""


def lambda_handler(event, context):
    account_ids = list()
    try:
        """
        You can replace this try/except by filling in `account_ids` yourself.
        Get your account ID with:
        > import boto3
        > iam = boto3.client('iam')
        > print(iam.get_user()['User']['Arn'].split(':')[4])
        """
        account_ids.append(iam.get_user()['User']['Arn'].split(':')[4])
    except Exception as e:
        # use the exception message to get the account ID the function executes
        # under
        account_ids.append(
            re.search(r'(arn:aws:sts::)([0-9]+)', str(e)).groups()[1])

    client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in client.describe_regions()['Regions']]

    for r in regions:
        print("region: %s" % r)

        ec = boto3.client('ec2', region_name=r)

        # delete instances we missed from a week ago
        for i in range(0, 7):
            delete_on = (datetime.date.today() +
                         timedelta(days=-i)).strftime('%Y-%m-%d')
            filters = [
                {'Name': 'tag-key', 'Values': ['DeleteOn']},
                {'Name': 'tag-value', 'Values': [delete_on]},
            ]

            snapshot_response = ec.describe_snapshots(
                OwnerIds=account_ids, Filters=filters)

            # print("Account ID %s" % ','.join(account_ids))

            for snap in snapshot_response['Snapshots']:
                print("Deleting snapshot %s" % snap['SnapshotId'])
                ec.delete_snapshot(SnapshotId=snap['SnapshotId'])
