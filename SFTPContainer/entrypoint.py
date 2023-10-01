#!/usr/bin/python3


import os
import subprocess
import pwd
import sys

# get environment variables - User 
# set the permissions on the public key 
# create a user

userName = os.environ.get("SFTP_USER")
keyPath = os.environ.get("KEY_PATH")

subprocess.run(['useradd', '-m', userName])

os.mkdir(f"/home/{userName}/.ssh")
subprocess.run(['touch', f'/home/{userName}/.ssh/authorized_keys'])

with open(f'{keyPath}', 'r') as pubkey:
    keydata = pubkey.read()
with open(f'/home/{userName}/.ssh/authorized_keys', 'w') as keysfile:
    keysfile.write(keydata)

os.chmod(f"/home/{userName}/.ssh", 0o755)
os.chmod(f"/home/{userName}/.ssh/authorized_keys", 0o600)
##chown both the directory and authorized keys files
uid = (pwd.getpwnam(userName)).pw_uid
os.chown(f"/home/{userName}/.ssh", uid)
os.chown(f"/home/{userName}/.ssh/authorized_keys", uid)
##start the sshd service /urs/sbin/sshd
subprocess.run(['/usr/sbin/sshd'])

subprocess.call(["python3", "/usr/local/bin/loop.py"])
