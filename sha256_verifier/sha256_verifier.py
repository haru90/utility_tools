#!/usr/bin/env python

import click
import re
import subprocess
import sys

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def sha256_verify(f_path, hash_value):
    try:
        f_hash = subprocess.run(['shasum', '-a', '256', f_path], stdout=subprocess.PIPE).stdout.decode('utf-8')[:64]
    except Exception as e:
        sys.exit(e)
    return re.compile(hash_value, re.IGNORECASE).match(f_hash) is not None


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_path')
@click.argument('hash_value')
def main(input_path, hash_value):
    sha256_verify(input_path, hash_value)


if __name__ == '__main__':
    main()
