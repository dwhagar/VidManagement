#!/usr/bin/env python3

import argparse
from sys import argv
from subprocess import check_output
from shutil import copy2
from tools import *

def parseArgs(argv):
    """Parse command-line arguments."""
    argparser = argparse.ArgumentParser(
        prog="copyVidoes.py",
        description="A tool to copy videos all videos, recursively, from one location to another.",
        fromfile_prefix_chars="@")

    argparser.add_argument("--source", "-s", default = None ,help = "specify where to scan for video files")
    argparser.add_argument("--dest", "-d", default = None, help = "specify where to copy video files to")

    options = argparser.parse_args(argv[1:])

    return options

def main(args):
    # Path to the find_colors script.
    findColors = "/Users/cyclops/odrive/Dropbox/Scripts/"
    options = parseArgs(args)

    if (options.source is None) or (options.dest is None):
        print("Invalid option(s).")
        return 1
    if (not validatePath(options.source)) or (not validatePath(options.dest)):
        print("Invalid path(s).")
        return 1

    files = findFiles(options.source)

    for file in files:
        filename = file[0] + "/" + file[1]
        color = check_output([findColors + "finder_colors.py", filename], universal_newlines = True)
        color = color.strip('\n')
        if color != "gray":
            check_output([findColors + "finder_colors.py", "gray", filename], universal_newlines = True)
            copy2(filename, options.dest)

main(argv)
