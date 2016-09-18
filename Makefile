lint:
	venv/bin/pylint -rn test.py s3stash

test:
	venv/bin/python test.py

release: lint test
	rm -r dist/
	venv/bin/python setup.py sdist bdist_wheel
	venv/bin/twine upload dist/*

.PHONY: lint test
