PACKAGE_NAME=pyfrctl
REPOSITORY=testpypi

clean:
	rm -rvf build dist *.egg-info

bld:
	python setup.py sdist bdist_wheel

check:
	twine check ./dist/*

dpl:
	twine upload --verbose --repository testpypi dist/*

build: clean bld check