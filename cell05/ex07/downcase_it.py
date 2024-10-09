#!/usr/bin/env python3
import sys

arg = (sys.argv[1])
lowarg = arg.lower()

if len(sys.argv[1:]) == 0:
    print ('None')
    
elif len(sys.argv[1:]) >= 1:
    print(lowarg)
