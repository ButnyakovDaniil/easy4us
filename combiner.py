import os
import argparse

from finder import *

parser = argparse.ArgumentParser(usage="e2u",
                                 description="Ioncube encrypter (easytoyou.eu)")
parser.add_argument("-d", "--directory", required=True, metavar="",
                    help="where is your project/site stored")
parser.add_argument("-t", "--text", required=False, default=".", metavar="",
                    help="where you want to store a list of encoded files (default=directory)")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-s", "--save", action="store_true", default=False,
                   help="saving list of encoded files")
args = parser.parse_args()

fileFinder(args.directory, args.text)



