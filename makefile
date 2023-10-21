prepare:
	@pip install -r REQUIREMENTS.txt

unittest:
	@python3 unittests/__init__.py

build:
	@python3 setup.py bdist_wheel sdist

install:
	@pip install .

uninstall:
	@pip uninstall somni-log -y

remove-build:
	rm -r build dist

remove:
	rm -r build dist
	@pip uninstall somni-log -y

rebuild-install:
	make remove
	make build
	make install

publish:
	@twine upload dist/*