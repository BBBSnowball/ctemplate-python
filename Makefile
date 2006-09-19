all:

compile:
	python setup.py build
	cp build/lib*/*.so .

test:
	python tests/test.py

clean:
	rm -rf build *.so
