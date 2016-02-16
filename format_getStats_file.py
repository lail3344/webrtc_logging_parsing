#!/home/luq/anaconda2/bin/python

import sys
import json
import pprint as pp
from pygments import highlight, lexers, formatters

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

formatted_json = json.dumps(data)

colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())

pp.pprint(colorful_json)
