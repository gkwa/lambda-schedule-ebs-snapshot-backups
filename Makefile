run:
	bash preparezip.sh
	bash upload.sh
	bash invoke.sh
	bash readlog.sh

clean:
	rm -rf stage
	rm -f outputfile.txt
	rm -f awsstdout.json
	rm -f lambda_function.zip

create:
	bash preparezip.sh
	bash create.sh

delete:
	bash delete.sh
