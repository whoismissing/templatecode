#!/usr/bin/python3

# Learning gdb python api: http://blog.scottt.tw/2012/01/exploring-gdb-python-api-with-ipython_31.html
# https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html

import gdb

# Usage: gdb -q -x prog.py

## This code will run whenever a breakpoint is hit
def stop_handler(event):
    print(gdb.execute('x/wx $sp', to_string=True))
    
gdb.events.stop.connect(stop_handler)

gdb.execute('file ./example')
o = gdb.execute('disassemble pwnme', to_string=True)
print(o)
r = gdb.execute('r < payload', to_string=True)
print(r)
ct = gdb.execute('context', to_string=True)
print(ct)

#gdb.execute('quit')
