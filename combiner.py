import os
import argparse
from finder import *
from main import *

#parser = argparse.ArgumentParser(usage="e2u",
#                                 description="Ioncube encrypter (easytoyou.eu)")
#parser.add_argument("-d", "--directory", required=True, metavar="",
#                    help="where is your project/site stored")
#parser.add_argument("-t", "--text", required=False, default=".", metavar="",
#                    help="where you want to store a list of encoded files (default=directory)")
#group = parser.add_mutually_exclusive_group(required=False)
#group.add_argument("-s", "--save", action="store_true", default=False,
#                   help="saving list of encoded files")
#args = parser.parse_args()

#user-friendly inerface
directory = input("Directory of your project/site: ")
if directory[0] != '/':
    print("Path to your directory should be absolute\nexample: /home/user/project/version")
    exit(1)
username = input("Your easytoyou.eu username: ")
password = input("Your easytoyou.eu password: ")
decoder = input("Required decoder version (default: ic10php72): ")

fileFinder(directory, directory)
fileShower(directory, directory, True)

main("", directory, username, password, decoder, False)

