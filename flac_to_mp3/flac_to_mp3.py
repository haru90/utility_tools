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
            print('f: ' + f, '\nout_dir_path: ', out_dir_path)
            encode(f, out_dir_path)

    for in_path in glob.glob(os.path.join(in_dir_path, '*.flac')):
        in_basename = os.path.splitext(os.path.basename(in_path))[0]
        out_path = os.path.join(out_root_dir_path, in_basename + '.mp3')
        ffmpeg_args = ['ffmpeg', '-i', in_path, '-ab', '320k', '-c:v', 'copy', out_path]
        try:
            print('Encoding ' + in_path)
            subprocess.run(ffmpeg_args)
        except:
            print("Error: " + in_path)


if len(sys.argv) != 3:
    print('Usage: python flac_to_mp3.py [input directory path] [output directory path]')
    sys.exit(1)

in_dir_path = sys.argv[1]
out_root_dir_path = sys.argv[2]

out_dir_path = os.path.join(out_root_dir_path, os.path.basename(in_dir_path))
if not os.path.exists(out_dir_path):
    os.mkdir(out_dir_path)

encode(in_dir_path, out_dir_path)
