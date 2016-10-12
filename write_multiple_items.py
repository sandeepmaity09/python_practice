#!/usr/bin/python3

def write_multiple_items(files,separator,*args):
    files.write(separator.join(args))

