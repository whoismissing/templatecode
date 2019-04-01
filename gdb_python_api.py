#!/usr/bin/python3

# Learning gdb python api: http://blog.scottt.tw/2012/01/exploring-gdb-python-api-with-ipython_31.html
# https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html

import gdb

# Usage: gdb -q -x prog.py

gdb.execute('file ./example')
o = gdb.execute('disassemble pwnme', to_string=True)
print(o)
r = gdb.execute('r < payload', to_string=True)
print(r)
ct = gdb.execute('context', to_string=True)
print(ct)

#gdb.execute('quit')
