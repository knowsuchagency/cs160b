#!/usr/bin/env python3

from pathlib import Path
from pprint import pprint
from argparse import ArgumentParser
import os
import getpass
import subprocess

def get_user():
    parser = ArgumentParser()
    parser.add_argument('user', nargs="?")
    namespace = parser.parse_args()
    user = namespace.user or getpass.getuser()
    return user

def get_passwd() -> str:
    """
    Return string of /etc/passwd
    """

    return subprocess.Popen('getent passwd', shell=True, stdout=subprocess.PIPE).stdout.read().decode()

def get_group() -> str:
    """Return a string of /etc/group"""

    return subprocess.Popen('getent group', shell=True, stdout=subprocess.PIPE).stdout.read().decode()


if __name__ == "__main__":

    user = get_user()
    passwd = get_passwd()
    group = get_group()
    pprint(group.splitlines())

