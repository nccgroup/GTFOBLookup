#!/usr/bin/python3


import argparse
from git import Repo
import os
import shutil
import sys


repoDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                  "GTFOBins.github.io")


def parseArgs():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser(description='GTFOBins Lookup')
    subparsers = parser.add_subparsers()
    parserUpdate = subparsers.add_parser('update', 
                                         help="update local copy of GTFOBins")
    parserUpdate.set_defaults(func=update)
    parserPurge = subparsers.add_parser('purge', 
                                         help="remove local copy of GTFOBins")
    parserPurge.set_defaults(func=purge)
    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit(0)
    else:
        return parser.parse_args()

def update(args):
    """Updates local copy of GTFOBins"""
    repoUrl = "https://github.com/GTFOBins/GTFOBins.github.io.git"
    print("Checking {0} for updates...".format(repoUrl))
    if not os.path.exists(repoDir):
        print("Local copy of GTFOBins not found, downloading...")
        Repo.clone_from(repoUrl, repoDir)
    else:
        repo = Repo(repoDir)
        current = repo.head.commit
        repo.remotes.origin.pull()
        if current == repo.head.commit:
            print("Local copy of GTFOBins is up to date")
        else:
            print("Local copy of GTFOBins updated")
            
def purge(args):
    """Removes local copy of GTFOBins"""
    shutil.rmtree(repoDir)

        
if __name__ == "__main__":
    args = parseArgs()
    args.func(args)
