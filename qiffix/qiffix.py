#! /usr/bin/env python3
"""
Converts debits to credits in a QIF file
usage: qiffix.py FILE

"""
from docopt import docopt

opts = docopt(__doc__)

qif_file = opts['FILE']

with open(qif_file) as qif:
    for line in qif:
       if line[0] == 'T' and line[1] != '-':
         print(line[:1] + '-' + line[1:], end='')
       elif line[0] == 'T' and line[1] == '-':
         print(line[:1] + line[2:], end='')
       else:
         print(line, end='')
