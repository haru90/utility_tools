#!/usr/bin/env python

import click
import os
import re
import subprocess
import sys

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
PASSWORD_F_PATH = '{}/.PASSWORD'.format(os.environ['HOME'])


def decrypt(input_path):
    decrypted_path = os.path.splitext(input_path)[0]
    try:
        result = subprocess.run(['openssl', 'aes-256-cbc', '-d', '-in', input_path, '-out', decrypted_path, '-pass',
                                 'file:{}'.format(PASSWORD_F_PATH)])
        if result.returncode != 0:
            sys.exit('Error: Failed to decrypt {}'.format(input_path))
        subprocess.run(['rm', input_path])
        if re.match(r'^.+\.tar\.gz$', decrypted_path):
            decrypted_root_dir_path = os.path.split(decrypted_path)[0]
            if decrypted_root_dir_path == '':
                decrypted_root_dir_path = '.'
            result = subprocess.run(['tar', 'xzf', decrypted_path, '-C', decrypted_root_dir_path])
            if result.returncode != 0:
                sys.exit('Error: Failed to extract {}'.format(decrypted_path))
            subprocess.run(['rm', decrypted_path])
    except Exception as e:
        sys.exit(e)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_path')
def main(input_path):
    decrypt(input_path)


if __name__ == '__main__':
    main()
