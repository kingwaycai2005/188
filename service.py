#!/usr/bin/python

import sys,os

if sys.argv[1] == 'nscd':
	if sys.argv[2] == 'status':
		os.system('/etc/init.d/nscd status')
