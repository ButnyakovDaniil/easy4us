import os
import argparse

parser = argparse.ArgumentParser(usage="e2u.finder",
                                 description="Ioncube encrypted files finder")
parser.add_argument("-d", "--directory", required=True, metavar="",
                    help="where is your project/site stored")
parser.add_argument("-t", "--text", required=False, default=".", metavar="",
                    help="where you want to store a list of encoded files (default=directory)")
parser.add_argument("--show", required=False, default=False, action="store_true",
                    help="show all encoded files in terminal")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-s", "--save", action="store_true", default=False,
                   help="save list of encoded files")
# group.add_argument("-q", "--quiet", action="store_false",
#                   help="doesn`t save list of encoded files (default)",)
args = parser.parse_args()

def fileFinder(directory, text):
    if directory[0] != '/' or ((text[0] != '/') * (text[0] != '.')):
        print("Path to your directory should be absolute\nexample: /home/user/project/version")
        exit(1)

    length = len(args.text)
    if text[length - 1] == '/':
        text[length - 1] = ''

    command = "cd " + directory + \
              " && grep -r -l -i --include=\*.py 'ioncube encrypted' > " \
              + text + "/encodedFilesList.txt"
    os.system(command)


def fileRemoving(directory, text, save):
    if save == False:
        if text == '.':
            text = directory
        command = "cd " + text + " && rm encodedFilesList.txt"
        os.system(command)

def fileShower(directory, text,show):
    if show==True:
        print("============================\n"
              "Those files have been found:")
        if text=='.':
            text=directory
        path=text+"/encodedFilesList.txt"
        with open(path, "r") as file:
            for line in file:
                print("./"+line)

fileFinder(args.directory, args.text)
fileShower(args.directory, args.text, args.show)
fileRemoving(args.directory, args.text, args.save)
