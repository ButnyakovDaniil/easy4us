import os
import argparse

parser = argparse.ArgumentParser(usage="e2u.finder",
                                 description="Ioncube encrypted files finder")
parser.add_argument("-d", "--directory", required=True, metavar="",
                    help="where is your project/site stored")
parser.add_argument("-t", "--text", required=False, default=".", metavar="",
                    help="where you want to store a list of encoded files (default=directory)")
args = parser.parse_args()

if args.directory[0] != '/' or ((args.text[0] != '/') * (args.text[0]!='.')):
    print("Path to your directory should be absolute\nexample: /home/user/project/version")
    exit(1)

length = len(args.text)
if args.text[length - 1] == '/':
    args.text[length - 1] = ''

command = "cd " + args.directory + \
          " && grep -r -l -i --include=\*.py 'ioncube encrypted' > " \
          + args.text + "/encodedFilesList.txt"
os.system(command)
