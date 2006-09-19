Python interface to the ctemplate library
=========================================

Run python internal help() for a complete API overview:
$ python -c "import ctemplate; help(ctemplate)"

Example:

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
dictionary["NOT_TRUE"] = False
print template.Expand(dictionary)
