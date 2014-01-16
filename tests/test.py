#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os
import sys
sys.path.insert(0, os.getcwd())
import ctemplate
import unittest

try:
    import tappy
    tappy_available = True
except ImportError:
    tappy_available = False

DICTIONARY_EXPECTED_VALUE = \
"""global dictionary {
   BI_NEWLINE: >
<
   BI_SPACE: > <
};
dictionary 'my example dict (intended for tests/test.tpl)' {
   DICT_FOO: >87411<
   DICT_INT: >7411<
   DICT_LONG: >7412<
   DICT_TUPLE: >(1, 2, 3)<
   ESCAPE_HTML: ><baz><
   ESCAPE_JS: >'baz'<
   ESCAPE_JSON: >'baz'<
   ESCAPE_XML: >&nbsp;<
   METHOD_FOO: >baz<
   METHOD_INT: >4<
   METHOD_LONG: >5<
   section SECT1 (dict 1 of 1) -->
     dictionary 'empty dictionary' {
     }
   section SECT2 (dict 1 of 1) -->
     dictionary 'empty dictionary' {
     }
   section SUB1 (dict 1 of 2) -->
     dictionary 'my example dict/SUB1#1' {
       SUB_FOO: >bar1<
     }
   section SUB1 (dict 2 of 2) -->
     dictionary 'my example dict/SUB1#2' {
       SUB_FOO: >bar2<
     }
}
"""

EXPECTED_RESULT = """
Hallo, das ist ein Täst
GLOBAL_FOO 
GLOBAL_INT 
GLOBAL_LONG 

METHOD_FOO baz
METHOD_INT 4
METHOD_LONG 5

DICT_FOO 87411
DICT_INT 7411
DICT_LONG 7412
DICT_TUPLE (1, 2, 3)

ESCAPE_HTML &lt;baz&gt;
ESCAPE_JS \\x27baz\\x27
"""


#TODO We should split this into many small test cases.
class CTemplateTests(unittest.TestCase):
    def test_constants (self):
        self.assertEqual(ctemplate.DO_NOT_STRIP,      0)
        self.assertEqual(ctemplate.STRIP_BLANK_LINES, 1)
        self.assertEqual(ctemplate.STRIP_WHITESPACE,  2)
        self.assertEqual(ctemplate.TS_EMPTY, 1)
        self.assertEqual(ctemplate.TS_ERROR, 2)
        self.assertEqual(ctemplate.TS_READY, 3)

    def _set_global (self):
        ctemplate.SetGlobalValue("GLOBAL_FOO", "bar")
        ctemplate.SetGlobalValue("GLOBAL_INT", 1)
        ctemplate.SetGlobalValue("GLOBAL_LONG", 2L)

    def _set_methods (self, dictionary):
        dictionary.SetValue("METHOD_FOO", "baz")
        dictionary.SetValue("METHOD_INT", 4)
        dictionary.SetValue("METHOD_LONG", 5L)

    def _set_for_escape_test (self, dictionary):
        dictionary.SetValue("ESCAPE_HTML", "<baz>")
        dictionary.SetValue("ESCAPE_XML", "&nbsp;")
        dictionary.SetValue("ESCAPE_JS", "'baz'")
        dictionary.SetValue("ESCAPE_JSON", "'baz'")

    def _set_dict (self, dictionary):
        dictionary["DICT_FOO"] = "87411"
        dictionary["DICT_INT"] = 7411
        dictionary["DICT_LONG"] = 7412L
        dictionary["DICT_TUPLE"] = (1, 2, 3)

    def _set_section (self, dictionary):
        dictionary.ShowSection("SECT1")
        dictionary["SECT2"] = True
        dictionary["SECT3"] = False

    def _set_subdict (self, dictionary):
        sub_dict = dictionary.AddSectionDictionary("SUB1")
        sub_dict["SUB_FOO"] = "bar1"
        sub_dict = dictionary.AddSectionDictionary("SUB1")
        sub_dict["SUB_FOO"] = "bar2"

    def test_it (self):
        filename = os.path.join("tests", "test.tpl")
        ctemplate.RegisterTemplate(filename)
        template = ctemplate.Template(filename, ctemplate.DO_NOT_STRIP)
        #self._set_global()  #TODO fix it
        dictionary = ctemplate.Dictionary("my example dict")
        dictionary.SetFilename(filename)
        self._set_methods(dictionary)
        self._set_for_escape_test(dictionary)
        self._set_dict(dictionary)
        self._set_section(dictionary)
        self._set_subdict(dictionary)
        self.assertEqual(dictionary.Dump(), DICTIONARY_EXPECTED_VALUE)
        self.assertEqual(template.Expand(dictionary), EXPECTED_RESULT)
        self.assertEqual(ctemplate.GetBadSyntaxList(True, ctemplate.DO_NOT_STRIP), [])


if __name__ == '__main__':
    if tappy_available:
        tappy.unittest_main(tapfile="python-ctemplate.tap")
    else:
        unittest.main()
