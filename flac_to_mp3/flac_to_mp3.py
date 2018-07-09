import glob
import os
import subprocess
import sys

if len(sys.argv) != 3:
    print('Usage: python flac_to_mp3.py [input directory path] [output directory path]')
    sys.exit(1)

in_dir = sys.argv[1]
out_root_dir = sys.argv[2]

out_dir = os.path.join(out_root_dir, os.path.basename(in_dir))
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

in_paths = glob.glob(os.path.join(in_dir, '*.flac'))
for in_path in in_paths:
    in_basename = os.path.splitext(os.path.basename(in_path))[0]
    out_path = os.path.join(out_dir, in_basename + '.mp3')
    ffmpeg_args = ['ffmpeg', '-i', in_path, '-ab', '320k', '-c:v', 'copy', out_path]
    try:
        print('Encoding ' + in_path)
        subprocess.run(ffmpeg_args)
    except:
        print("Error: " + in_path)
