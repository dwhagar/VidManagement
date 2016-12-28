# Video Management Tools (c) by David Wade Hagar
#
# Video Management Tools is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see <http://creativecommons.org/licenses/by-nc-sa/4.0/>.
#
# See LICENSE.md for licensing details.

from os.path import exists, isdir
from os import walk

def validatePath(path):
    # If the path does not exist, fail gracefully.
    if (not exists(path)) or (not isdir(path)):
        print("You must specify a valid path.")
        return False

    return True

def findFiles(path):
    types = [".mkv", ".mp4", ".m4v", ".mov", ".avi"]
    files = []

    # Walk the file structure
    for root, dirs, files in walk(path):
        # Walk the files.
        for file in files:
            # Ignore "Sample" files
            if file.lower().find("sample") == -1:
                # Find the extension.
                index = file.rfind(".")
                # Cut it off, use that as a base to search.
                fileExt = file[index:]
                for testExt in types:
                    if fileExt.lower() == testExt:
                        file = (root, file)
                        files.append(file)

    return files