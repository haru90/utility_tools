#!/usr/bin/env python

import click
import glob
import os
import re

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def rename(in_dir_path):
    for f in glob.glob(os.path.join(in_dir_path, '*')):
        if os.path.isdir(f):
            rename(f)

    for old_f_path in glob.glob(os.path.join(in_dir_path, '*')):
        old_f_name = os.path.basename(old_f_path)
        new_f_path = os.path.join(in_dir_path, re.sub(r'\W+', '_', old_f_name))
        try:
            os.rename(old_f_path, new_f_path)
        except Exception as e:
            print(e)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_directory_path', default=os.getcwd())
def main(input_directory_path):
    '''Rename files'''
    rename(input_directory_path)


if __name__ == '__main__':
    main()
