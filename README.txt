Python interface to the ctemplate library
=========================================

The main functions and classes of the ctemplate library are
wrapped as native Python objects.
Run python internal help() for an API overview:
$ python -c "import ctemplate; help(ctemplate)"

Example:

# loads example.tpl in current directory
template = ctemplate.Template("example.tpl", ctemplate.DO_NOT_STRIP)
dictionary = ctemplate.Dictionary("my example dict")
# dict setters call SetValue() automatically
dictionary["VALUE"] = "TEST"
# all objects except booleans are converted to strings
dictionary["NUMBER"] = 87411
dictionary["TUPLE"] = (1, 2, 3)
# boolean True calls ShowSection()
dictionary["IN_CA"] = True
# boolean False is ignored
dictionary["IGNORED"] = False
# And of course the expand function
print template.Expand(dictionary)

Installation
============
Run "python setup.py install". See "python setup.py install --help" for
options.

