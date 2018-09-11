#!/usr/bin/env python

import click
import os
import subprocess
import sys

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
PASSWORD_F_PATH = '{}/.PASSWORD'.format(os.environ['HOME'])


def encrypt(input_path):
    try:
        if os.path.isfile(input_path):
            result = subprocess.run(
                ['openssl', 'aes-256-cbc', '-e', '-in', input_path, '-out', '{}.enc'.format(input_path), '-pass',
                 'file:{}'.format(PASSWORD_F_PATH)])
            if result.returncode != 0:
                sys.exit('Error: Failed to encrypt {}'.format(input_path))
            # subprocess.run(['rm', input_path])
        elif os.path.isdir(input_path):
            tgz_path = '{}.tar.gz'.format(input_path)
            subprocess.run(['tar', 'czf', tgz_path, input_path])
            result = subprocess.run(
                ['openssl', 'aes-256-cbc', '-e', '-in', tgz_path, '-out', '{}.enc'.format(tgz_path), '-pass',
                 'file:{}'.format(PASSWORD_F_PATH)])
            if result.returncode != 0:
                print('Error: Failed to encrypt {}'.format(input_path), file=sys.stderr)
                result = subprocess.run(['tar', 'xzf', tgz_path])
                if result.returncode == 0:
                    subprocess.run(['rm', tgz_path])
                    sys.exit(1)
                else:
                    sys.exit('Error: Failed to extract {}'.format(tgz_path))
            # subprocess.run(['rm', '-rf', input_path])
            subprocess.run(['rm', tgz_path])
        else:
            sys.exit('Error: {} is not a file or directory'.format(input_path))
    except Exception as e:
        sys.exit(e)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_path')
def main(input_path):
    encrypt(input_path)


if __name__ == '__main__':
    main()
