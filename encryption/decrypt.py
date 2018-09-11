#!/usr/bin/env python

import click
import os
import re
import subprocess
import sys

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
PASSWORD_F_PATH = '{}/.PASSWORD'.format(os.environ['HOME'])


def decrypt(input_path):
    out_path = os.path.splitext(input_path)[0]
    try:
        result = subprocess.run(['openssl', 'aes-256-cbc', '-d', '-in', input_path, '-out', out_path, '-pass',
                                 'file:{}'.format(PASSWORD_F_PATH)])
        if result.returncode != 0:
            sys.exit('Error: Failed to decrypt {}'.format(input_path))
        subprocess.run(['rm', input_path])
        if re.match(r'^.+\.tar\.gz$', out_path):
            result = subprocess.run(['tar', 'xzf', out_path])
            if result.returncode != 0:
                sys.exit('Error: Failed to extract {}'.format(out_path))
            subprocess.run(['rm', out_path])
    except Exception as e:
        sys.exit(e)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_path')
def main(input_path):
    decrypt(input_path)


if __name__ == '__main__':
    main()
