# Makefile used for local development.
# Can also generate a signed Debian .deb package
PYTHON:=python
VERSION:=$(shell python setup.py --version)
SVNBUILD:=$(HOME)/src/build-area
DEB_ORIG_TARGET:=$(SVNBUILD)/python-ctemplate_$(VERSION).orig.tar.gz
GPGKEY:=2DE589F5

all:

.PHONY: cleandeb
cleandeb:
	rm -rf debian/python-ctemplate debian/tmp
	rm -f debian/*.debhelper debian/{files,substvars}
	rm -f configure-stamp build-stamp

.PHONY: deb_orig
deb_orig:
	if [ ! -e $(DEB_ORIG_TARGET) ]; then \
	  $(PYTHON) setup.py sdist && \
	  cp dist/python-ctemplate-$(VERSION).tar.gz $(DEB_ORIG_TARGET); \
	fi

# ready for upload, signed with my GPG key
.PHONY: deb_signed
deb_signed: cleandeb
	(env -u LANG svn-buildpackage --svn-dont-clean --svn-verbose --svn-ignore \
	  --svn-prebuild="$(MAKE) deb_orig" --svn-lintian --svn-linda \
	  -sgpg -pgpg -k$(GPGKEY) -r"fakeroot --" 2>&1) | \
	tee $(SVNBUILD)/python-ctemplate-$(VERSION).build

.PHONY: localbuild
localbuild:
	$(PYTHON) setup.py build
	cp build/lib*/*.so .

.PHONY: test
test:	localbuild
	$(PYTHON) tests/test.py

.PHONY: clean
clean:	cleandeb
	rm -rf build dist
	rm -f *.so
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete

