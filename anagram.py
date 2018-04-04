#! /usr/bin/env python3
# anagram.py - 入力した文字列からアナグラムを生成

import sys, itertools, random

DEFAULT_OUTPUT_NUM = 50  # 出力するアナグラム文字列の数のデフォルト値

if len(sys.argv) < 2:
    print('Usage: ./anagram.py [original text] [number of outputs (option)]')
    sys.exit(0)
elif len(sys.argv) == 3:
    output_num = int(sys.argv[2])
else:
    output_num = DEFAULT_OUTPUT_NUM

input = sys.argv[1]

output_strs = []
for output_tuple in itertools.permutations(input, len(input)):
    output_str = ''.join(map(str, output_tuple))
    output_strs.append(output_str)

output_num = min(output_num, len(output_strs))

sampled_outputs = random.sample(output_strs, output_num)
for output_str in sampled_outputs:
    print(output_str)
