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
    #Update
    parserUpdate = subparsers.add_parser('update', help="update local copy " + 
                                         "of GTFOBins")
    parserUpdate.set_defaults(func=update)
    #Purge
    parserPurge = subparsers.add_parser('purge', help="remove local copy of " + 
                                        "GTFOBins")
    parserPurge.set_defaults(func=purge)
    #Shell
    parserShell = subparsers.add_parser('shell', help="search for " + 
                                        "applications that can be used to " + 
                                        "spawn an interactive shell")
    parserShell.set_defaults(func=search, typ='shell')
    #Command
    parserCmd = subparsers.add_parser('cmd', help="search for applications " + 
                                      "that can be used to run " + 
                                      "non-interactive system commands")
    parserCmd.set_defaults(func=search, typ='command')
    #Reverse shell
    parserRev = subparsers.add_parser('rev', help="search for applications " + 
                                      "that can be used to spawn a reverse " + 
                                      "shell")
    parserRev.set_defaults(func=search, typ='reverse-shell')
    #Non-interactive reverse shell
    parserNrev = subparsers.add_parser('nrev', help="search for applications " + 
                                       "that can be used to spawn a " + 
                                       "non-interactive reverse shell")
    parserNrev.set_defaults(func=search, typ='non-interactive-reverse-shell')
    #Bind shell
    parserBind = subparsers.add_parser('bind', help="search for applications " + 
                                       "that can be used to spawn a bind shell")
    parserBind.set_defaults(func=search, typ='bind-shell')
    #Non-interactive bind shell
    parserNbind = subparsers.add_parser('nbind', help="search for " + 
                                        "applications that can be used to " + 
                                        "spawn a non-interactive bind shell")
    parserNbind.set_defaults(func=search, typ='non-interactive-bind-shell')
    #File upload
    parserUpload = subparsers.add_parser('upload', help="search for " + 
                                         "applications that can be used to " + 
                                         "upload files")
    parserUpload.set_defaults(func=search, typ='file-upload')
    #File download
    parserDownload = subparsers.add_parser('download', help="search for " + 
                                           "applications that can be used to " +
                                           "download files")
    parserDownload.set_defaults(func=search, typ='file-download')
    #File write
    parserWrite = subparsers.add_parser('write', help="search for " + 
                                        "applications that can be used to " + 
                                        "write to files")
    parserWrite.set_defaults(func=search, typ='file-write')
    #File read
    parserRead = subparsers.add_parser('read', help="search for applications " +
                                       "that can be used to read files")
    parserRead.set_defaults(func=search, typ='file-read')
    #Library load
    parserLoad = subparsers.add_parser('load', help="search for applications " +
                                       "that load shared libraries")
    parserLoad.set_defaults(func=search, typ='library-load')
    #SUID
    parserSuid = subparsers.add_parser('suid', help="search for applications " +
                                       "that, with the SUID bit set, can be " + 
                                       "used to escalate privileges")
    parserSuid.set_defaults(func=search, typ='suid')
    #Sudo
    parserSudo = subparsers.add_parser('sudo', help="search for applications " + 
                                       "that, when run with sudo, can be used" + 
                                       " to escalate privileges")
    parserSudo.set_defaults(func=search, typ='sudo')
    #Capabilities
    parserCap = subparsers.add_parser('cap', help="search for applications " + 
                                      "that have the 'CAP_SETUID' capability " +
                                      "set")
    parserCap.set_defaults(func=search, typ='capabilities')
    #Limited SUID
    parserLsuid = subparsers.add_parser('lsuid', help="search for " + 
                                        "applications that, with the SUID " + 
                                        "bit set, can be used to escalate " + 
                                        "privileges on systems that allow " + 
                                        "the default 'sh' shell to run with " + 
                                        "sudo privileges")
    parserLsuid.set_defaults(func=search, typ='limited-suid')
    #All
    parserAll = subparsers.add_parser('all', help="search for applications " +
                                      "in all categories")
    parserAll.set_defaults(func=search, typ='all')
    #No args
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
    
def search(args):
    """Searches local copy of GTFOBins for a specified binary in a specified 
    category
    """
    #TODO
        
        
if __name__ == "__main__":
    args = parseArgs()
    args.func(args)
