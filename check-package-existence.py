#!/usr/bin/python
from subprocess import run
from sys import stderr

KERNEL = 'linux515'

try:
    for filename in ['community/gnome-vanilla/Packages-Root',
                     'community/gnome-vanilla/Packages-Mhwd',
                     'community/gnome-vanilla/Packages-Desktop',
                     'community/gnome-vanilla/Packages-Live']:
        with open(filename, 'r') as file:
            for line in file.readlines():
                line = line.split('#')[0].strip()
                if line == '': continue
                if line.startswith('>'): line = line.split(' ', 1)[1]
                line = line.replace('KERNEL', KERNEL)
                print(f'\rchecking {line}\033[J', end='', file=stderr)
                if run(['pacman', '-Sp', line], capture_output=True).returncode != 0:
                    print(f'\r{line}\033[J')
            print('\r\033[J', end='', file=stderr)

except KeyboardInterrupt:
    print('\r\033[J', end='')
    print('\r\033[J', end='', file=stderr)
