#!/usr/bin/python
# -*- encoding: utf8 -*-

import csv
import optparse
import sys


__author__ = 'sheep'


def main(fname, output_fname):
    '''\
    %prog [options] <fname> <output_fname>
    '''
    with open(fname, 'r') as f:
        with open(output_fname, 'w') as fo:
            spamreader = csv.reader(f, delimiter=',', quotechar='"')
            first = True
            for line in spamreader:
                if first:
                    first = False
                    continue

                xys = eval(line[-1])
                fo.write('%d\n' % ((len(xys)-1) * 15))
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

