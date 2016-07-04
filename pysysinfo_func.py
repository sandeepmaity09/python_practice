#!/usr/bin/python3
#A System Information Gathering Script

import subprocess

#Command 1
def uname_func():
	uname="uname"
	uname_arg="-a"
	print("Gathering system information with %s command:\n"%uname)
	subprocess.call([uname,uname_arg])

def disk_func():
	diskspace="df"
	diskspace_arg="-h"
	print("Gathering disk information with %s command:\n"%diskspace)
	subprocess.call([diskspace,diskspace_arg])

def disk_func_sh():
	new_diskspace="df -h"
	print("Gathering disk information using %s command:\n"%new_diskspace)
	subprocess.call(new_diskspace,shell=True)

def main():
	uname_func()
	disk_func()
	disk_func_sh()

main()
