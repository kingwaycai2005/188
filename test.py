#!/usr/bin/python

import sys
import os

sysname = os.system('uname -a ')
diskinfo = os.system('df -h')

print sysname
print '-------------'
print diskinfo
