#!/usr/bin/python3


import argparse
from git import Repo
import os
import shutil
import sys
import textwrap
import yaml


repoDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                  "GTFOBins.github.io")

types = {"shell": "shell",
         "cmd": "command",
         "rev": "reverse-shell",
         "nrev": "non-interactive-reverse-shell",
         "bind": "bind-shell",
         "nbind": "non-interactive-bind-shell",
         "upload": "file-upload",
         "download": "file-download",
         "write": "file-write",
         "read": "file-read",
         "load": "library-load",
         "suid": "suid",
         "sudo": "sudo",
         "cap": "capabilities",
         "lsuid": "limited-suid"
        }

#Text formatting
green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
reset = "\033[0m"


def parseArgs():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser(description='Offline GTFOBins Lookup')
    subparsers = parser.add_subparsers()
    typParsers = []
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
    parserShell.set_defaults(typ=types['shell'])
    typParsers.append("parserShell")
    #Command
    parserCmd = subparsers.add_parser('cmd', help="search for applications " + 
                                      "that can be used to run " + 
                                      "non-interactive system commands")
    parserCmd.set_defaults(typ=types['cmd'])
    typParsers.append("parserCmd")
    #Reverse shell
    parserRev = subparsers.add_parser('rev', help="search for applications " + 
                                      "that can be used to spawn a reverse " + 
                                      "shell")
    parserRev.set_defaults(typ=types['rev'])
    typParsers.append("parserRev")
    #Non-interactive reverse shell
    parserNrev = subparsers.add_parser('nrev', help="search for applications " + 
                                       "that can be used to spawn a " + 
                                       "non-interactive reverse shell")
    parserNrev.set_defaults(typ=types['nrev'])
    typParsers.append("parserNrev")
    #Bind shell
    parserBind = subparsers.add_parser('bind', help="search for applications " + 
                                       "that can be used to spawn a bind shell")
    parserBind.set_defaults(typ=types['bind'])
    typParsers.append("parserBind")
    #Non-interactive bind shell
    parserNbind = subparsers.add_parser('nbind', help="search for " + 
                                        "applications that can be used to " + 
                                        "spawn a non-interactive bind shell")
    parserNbind.set_defaults(typ=types['nbind'])
    typParsers.append("parserNbind")
    #File upload
    parserUpload = subparsers.add_parser('upload', help="search for " + 
                                         "applications that can be used to " + 
                                         "upload files")
    parserUpload.set_defaults(typ=types['upload'])
    typParsers.append("parserUpload")
    #File download
    parserDownload = subparsers.add_parser('download', help="search for " + 
                                           "applications that can be used to " +
                                           "download files")
    parserDownload.set_defaults(typ=types['download'])
    typParsers.append("parserDownload")
    #File write
    parserWrite = subparsers.add_parser('write', help="search for " + 
                                        "applications that can be used to " + 
                                        "write to files")
    parserWrite.set_defaults(typ=types['write'])
    typParsers.append("parserWrite")
    #File read
    parserRead = subparsers.add_parser('read', help="search for applications " +
                                       "that can be used to read files")
    parserRead.set_defaults(typ=types['read'])
    typParsers.append("parserRead")
    #Library load
    parserLoad = subparsers.add_parser('load', help="search for applications " +
                                       "that load shared libraries")
    parserLoad.set_defaults(typ=types['load'])
    typParsers.append("parserLoad")
    #SUID
    parserSuid = subparsers.add_parser('suid', help="search for applications " +
                                       "that, with the SUID bit set, can be " + 
                                       "used to escalate privileges")
    parserSuid.set_defaults(typ=types['suid'])
    typParsers.append("parserSuid")
    #Sudo
    parserSudo = subparsers.add_parser('sudo', help="search for applications " + 
                                       "that, when run with sudo, can be used" + 
                                       " to escalate privileges")
    parserSudo.set_defaults(typ=types['sudo'])
    typParsers.append("parserSudo")
    #Capabilities
    parserCap = subparsers.add_parser('cap', help="search for applications " + 
                                      "that have the 'CAP_SETUID' capability " +
                                      "set")
    parserCap.set_defaults(typ=types['cap'])
    typParsers.append("parserCap")
    #Limited SUID
    parserLsuid = subparsers.add_parser('lsuid', help="search for " + 
                                        "applications that, with the SUID " + 
                                        "bit set, can be used to escalate " + 
                                        "privileges on systems that allow " + 
                                        "the default 'sh' shell to run with " + 
                                        "sudo privileges")
    parserLsuid.set_defaults(typ=types['lsuid'])
    typParsers.append("parserLsuid")
    #All
    parserAll = subparsers.add_parser('all', help="search for applications " +
                                      "in all categories")
    parserAll.set_defaults(typ="all")
    typParsers.append("parserAll")
    #Set common properties
    for subparser in typParsers:
        subparser = vars()[subparser]
        subparser.set_defaults(func=search)
        subparser.add_argument('-f', '--file', help="use a file containing a " +
                  "list of binaries \(one per line\) instead of a single " +
                  "binary", action='store_const', const=parseFile, dest='func')
        subparser.add_argument('binary', help='the binary to search for')
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
            print(green + "Local copy of GTFOBins is up to date" + reset)
        else:
            print(green + "Local copy of GTFOBins updated" + reset)
            
def purge(args):
    """Removes local copy of GTFOBins"""
    if os.path.exists(repoDir):
        shutil.rmtree(repoDir)
    else:
        print(red + "Local copy of GTFOBins not found" + reset)
    
def extract(typ, md):
    """Extracts details of a specified function of a specified binary from local
    copy of GTFOBins
    """
    print("    {0}:\n".format(typ))
    for data in md:
            if data is not None:
                try:
                    for header in data['functions'][typ]:
                        for text in header:
                            lines = header[text].split("\n")
                            indent = "        "
                            if text == "code":
                                print(yellow)
                                indent += "    "
                            for line in lines:
                                if line != '':
                                    print(textwrap.fill(line, width=80,
                                          initial_indent=indent, 
                                          subsequent_indent=indent))
                            print("\n" + reset)
                except:
                    print(red + "        No results of this type were found " +
                          "for this binary \n" + reset)

def search(args):
    """Searches local copy of GTFOBins for a specified binary in a specified 
    category
    """
    if not os.path.exists(repoDir):
        sys.exit(red + "Local copy of GTFOBins not found, please update" + 
                 reset)
    mdPath = os.path.join(repoDir, "_gtfobins", "{0}.md".format(args.binary))
    if os.path.isfile(mdPath):
        with open(mdPath, 'r') as f:
            md = f.read()
        print("{0}:\n".format(args.binary))
        if args.typ == "all":
            for typ in types.values():
                mdParsed = yaml.load_all(md)
                extract(typ, mdParsed)
        else:
            mdParsed = yaml.load_all(md)
            extract(args.typ, mdParsed)
    else:
        print(red + "'{0}' was not found in the local copy of ".format(
                 args.binary) + "GTFOBins" + reset)

def parseFile(args):
    """Parses a list of binaries in a supplied file"""
    with open(args.binary, 'r') as f:
        bins = f.readlines()
    for binary in bins:
        if binary.strip() != "":
            args.binary = binary.strip()
            search(args)
     
        
if __name__ == "__main__":
    args = parseArgs()
    args.func(args)
