# qiffix

A utility that converts debits to credits (and vice versa) in QIF (Quicken) files. Written for importing credit card transactions into YNAB. 

Especially for those banks (e.g. Lloyds Bank) who think that credit card spending should be classed as a credit. (???)

Written for Python 3+.

---

To run:

    ./qiffix.py myfile.qif
    
This will write the result to STDOUT. 

To write the result to a file instead:

    ./qiffix.py myfile.qif > myfile-fixed.qif
