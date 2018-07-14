#!/usr/bin/env python

import click
import glob
import os
import subprocess

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def escape(str):
    return str.translate(str.maketrans({'[': '[[]', ']': '[]]'}))


def encode(in_dir_path, out_root_dir_path):
    for f in glob.glob(os.path.join(escape(in_dir_path), '*')):
        if os.path.isdir(f):
            out_dir_path = os.path.join(out_root_dir_path, os.path.basename(f))
            if not os.path.exists(out_dir_path):
                os.mkdir(out_dir_path)
            encode(f, out_dir_path)

    for in_path in glob.glob(os.path.join(escape(in_dir_path), '*.flac')):
        in_basename = os.path.splitext(os.path.basename(in_path))[0]
        out_path = os.path.join(out_root_dir_path, in_basename + '.mp3')
        ffmpeg_argv = ['ffmpeg', '-i', in_path, '-ab', '320k', '-c:v', 'copy', '-n', out_path]
        try:
            print('\nEncoding ' + in_path + '\n')
            subprocess.run(ffmpeg_argv)
        except Exception as e:
            print(e)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_directory_path')
@click.argument('output_directory_path', default=os.getcwd())
def main(input_directory_path, output_directory_path):
    '''Encode FLAC audio files into MP3 320kbps CBR files'''
    out_dir_path = os.path.join(output_directory_path, os.path.basename(input_directory_path))
    if not os.path.exists(out_dir_path):
        os.mkdir(out_dir_path)

    encode(input_directory_path, out_dir_path)


if __name__ == '__main__':
    main()
