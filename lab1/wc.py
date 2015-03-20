"""Word count (wc) unix like program.

Usage:
  wc <file>
  wc -m | --chars <file>
  wc -l | --lines <file>

Options:
  -h --help     Show this screen.
  -m --chars   Print the character counts.
  -l --lines    Print the newline counts.
"""
import sys
import os
from docopt import docopt

args = docopt(__doc__)

input_file = args['<file>']
count_chars = args['--chars']
count_lines = args['--lines']

if not count_chars and not count_lines:
    count_chars = count_lines = True


def blocks(infile, bufsize=1024):
    while True:
        try:
            data = infile.read(bufsize)
            if data:
                yield data
            else:
                break
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            break

if not os.path.isfile(input_file):
    print "`{}` is not a file or does not exist.".format(input_file)
    sys.exit()

chars_counter = 0
lines_counter = 0

with open(input_file) as fp:
    for line in fp:
        for c in line:
            chars_counter += 1
            if c == os.linesep:
                lines_counter += 1

print "File: {}".format(input_file)

if count_chars:
    print "Characters: {}".format(chars_counter)

if count_lines:
    print "Lines: {}".format(lines_counter)

