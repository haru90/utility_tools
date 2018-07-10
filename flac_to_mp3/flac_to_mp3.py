import glob
import os
import subprocess
import sys


def encode(in_dir_path, out_root_dir_path):
    for f in glob.glob(os.path.join(in_dir_path, '*')):
        if os.path.isdir(f):
            out_dir_path = os.path.join(out_root_dir_path, os.path.basename(f))
            if not os.path.exists(out_dir_path):
                os.mkdir(out_dir_path)
            encode(f, out_dir_path)

    for in_path in glob.glob(os.path.join(in_dir_path, '*.flac')):
        in_basename = os.path.splitext(os.path.basename(in_path))[0]
        out_path = os.path.join(out_root_dir_path, in_basename + '.mp3')
        ffmpeg_argv = ['ffmpeg', '-i', in_path, '-ab', '320k', '-c:v', 'copy', '-n', out_path]
        try:
            print('\nEncoding ' + in_path + '\n')
            subprocess.run(ffmpeg_argv)
        except:
            print("Error: Fail to encode " + in_path)


def main(argv):
    if len(argv) != 3:
        print('Usage: python flac_to_mp3.py [input directory path] [output directory path]')
        sys.exit(1)

    in_dir_path = argv[1]
    out_root_dir_path = argv[2]

    out_dir_path = os.path.join(out_root_dir_path, os.path.basename(in_dir_path))
    if not os.path.exists(out_dir_path):
        os.mkdir(out_dir_path)

    encode(in_dir_path, out_dir_path)


if __name__ == '__main__':
    main(sys.argv)
