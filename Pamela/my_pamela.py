#!/usr/bin/env python

import sys
import os
import subprocess
import hashlib

def command(my_cmd):
    return subprocess.call(my_cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

def main():
        print 'Select path for decrypt/encrypt file or container: (ex: /home/user/test.txt')
        my_name = raw_input()

        print 'Choose a size for the file or container (in MB)'
        size = raw_input()

        print 'Enter passphrase to encrypt/decrypt the file or container:'
        passphrase = raw_input()

        command("touch %s" % my_name)
        print 'Creating container or file...'
        command("dd if=/dev/zero bs=1M count=%s of=%s" % (size, my_name))
        print 'Creating container or file ...'
		
        command("echo -n %s | sudo cryptsetup luksFormat %s" % (passphrase, my_name))
        command("echo '%s' | sudo cryptsetup luksOpen %s secret-device" % (passphrase, my_name))
        command("sudo mkfs.ext4 /dev/mapper/secret-device")
        command("sudo cryptsetup luksClose secret-device")
        print 'Container successfuly created'

main()