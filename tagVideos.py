#!/usr/local/bin/python3

import argparse
from sys import argv
from os import rename
from pymediainfo import MediaInfo
from tools import *

def parseArgs(argv):
    """Parse command-line arguments."""
    argparser = argparse.ArgumentParser(
        prog="copyVidoes.py",
        description="A tool to copy videos all videos, recursively, from one location to another.",
        fromfile_prefix_chars="@")

    argparser.add_argument("--source", "-s", default = None ,help = "specify where to scan for video files")

    options = argparser.parse_args(argv[1:])

    return options

def main(args):
    # Path to the find_colors script.
    options = parseArgs(args)

    if options.source is None:
        print("Invalid option.")
        return 1
    if not validatePath(options.source):
        print("Invalid path.")
        return 1

    files = findFiles(options.source)

    for file in files:
        index = file[1].rfind(".")
        fileExt = file[1][index:]
        qualText = "SDTV"
        info = MediaInfo.parse(file[0] + "/" + file[1])

        for track in info.tracks:
            if track.track_type == 'Video':
                height = track.height
                if height >= 2160:
                    qualText = "WEBDL-2160"
                elif height >= 1080:
                    qualText = "WEBDL-1080"
                elif height >= 720:
                    qualText = "WEBDL-720"
                elif height >= 480:
                    qualText = "WEBDL-480"

                if height >= 480:
                    if track.scan_type == "Progressive":
                        qualText += "p"
                    else:
                        qualText += "i"
                break

        srcFile = file[0] + '/' + file[1]
        newFile = file[0] + '/' + file[1][0:index] + "." + qualText + fileExt.lower()
        rename(srcFile, newFile)

main(argv)
