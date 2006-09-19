from distutils.core import setup, Extension

module1 = Extension('ctemplate',
                    sources = ['src/ctemplate.cpp'],
                    libraries = ["ctemplate", "pthread"])

myname = "Bastian Kleineidam"
myemail = "calvin@debian.org"

setup (name = 'python-ctemplate',
       version = '0.1',
       description = 'Python wrapper for the ctemplate library',
       author = myname,
       author_email = myemail,
       maintainer = myname,
       maintainer_email = myemail,
       ext_modules = [module1])
