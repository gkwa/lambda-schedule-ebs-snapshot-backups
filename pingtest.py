import subprocess as sub


def lambda_handler(event, context):
    print('hello')
    #  p = sub.Popen(['ping', '-c1', '127.0.0.1'],stdout=sub.PIPE,stderr=sub.PIPE)
    p = sub.Popen(['curl', '-vL', '-X TRACE', 'http://google.com'],
                  stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = p.communicate()
    o = output.decode('utf-8').strip()
    e = errors.decode('utf-8').strip()
    print(e)
    print(o)
