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
    parserShell.set_defaults(func=shell)
    #Command
    parserCmd = subparsers.add_parser('cmd', help="search for applications " + 
                                      "that can be used to run " + 
                                      "non-interactive system commands")
    parserCmd.set_defaults(func=cmd)
    #Reverse shell
    parserRev = subparsers.add_parser('rev', help="search for applications " + 
                                      "that can be used to spawn a reverse " + 
                                      "shell")
    parserRev.set_defaults(func=rev)
    #Non-interactive reverse shell
    parserNrev = subparsers.add_parser('nrev', help="search for applications " + 
                                       "that can be used to spawn a " + 
                                       "non-interactive reverse shell")
    parserNrev.set_defaults(func=nrev)
    #Bind shell
    parserBind = subparsers.add_parser('bind', help="search for applications " + 
                                       "that can be used to spawn a bind shell")
    parserBind.set_defaults(func=bind)
    #Non-interactive bind shell
    parserNbind = subparsers.add_parser('nbind', help="search for " + 
                                        "applications that can be used to " + 
                                        "spawn a non-interactive bind shell")
    parserNbind.set_defaults(func=nbind)
    #File upload
    parserUpload = subparsers.add_parser('upload', help="search for " + 
                                         "applications that can be used to " + 
                                         "upload files")
    parserUpload.set_defaults(func=upload)
    #File download
    parserDownload = subparsers.add_parser('download', help="search for " + 
                                           "applications that can be used to " +
                                           "download files")
    parserDownload.set_defaults(func=download)
    #File write
    parserWrite = subparsers.add_parser('write', help="search for " + 
                                        "applications that can be used to " + 
                                        "write to files")
    parserWrite.set_defaults(func=write)
    #File read
    parserRead = subparsers.add_parser('read', help="search for applications " +
                                       "that can be used to read files")
    parserRead.set_defaults(func=read)
    #Library load
    parserLoad = subparsers.add_parser('load', help="search for applications " +
                                       "that load shared libraries")
    parserLoad.set_defaults(func=load)
    #SUID
    parserSuid = subparsers.add_parser('suid', help="search for applications " +
                                       "that, with the SUID bit set, can be " + 
                                       "used to escalate privileges")
    parserSuid.set_defaults(func=suid)
    #Sudo
    parserSudo = subparsers.add_parser('sudo', help="search for applications " + 
                                       "that, when run with sudo, can be used" + 
                                       " to escalate privileges")
    parserSudo.set_defaults(func=sudo)
    #Capabilities
    parserCap = subparsers.add_parser('cap', help="search for applications " + 
                                      "that have the 'CAP_SETUID' capability " +
                                      "set")
    parserCap.set_defaults(func=cap)
    #Limited SUID
    parserLsuid = subparsers.add_parser('lsuid', help="search for " + 
                                        "applications that, with the SUID " + 
                                        "bit set, can be used to escalate " + 
                                        "privileges on systems that allow " + 
                                        "the default 'sh' shell to run with " + 
                                        "sudo privileges")
    parserLsuid.set_defaults(func=lsuid)
    #All
    parserAll = subparsers.add_parser('all', help="search for applications " +
                                      "in all categories")
    parserAll.set_defaults(func=all)
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
    
def shell(args):
    """Searches for applications that can be used to spawn an interactive shell
    """
    #TODO
    
def cmd(args):
    """Searches for applications that can be used to run non-interactive system
    commands
    """
    #TODO
    
def rev(args):
    """Searches for applications that can be used to spawn a reverse shell"""
    #TODO
    
def nrev(args):
    """Searches for applications that can be used to spawn a non-interactive 
    reverse shell
    """
    #TODO
    
def bind(args):
    """Searches for applications that can be used to spawn a bind shell"""
    #TODO
    
def nbind(args):
    """Searches for applications that can be used to spawn a non-interactive 
    bind shell
    """
    #TODO
    
def upload(args):
    """Searches for applications that can be used to upload files"""
    #TODO
    
def download(args):
    """Searches for applications that can be used to download files"""
    #TODO
    
def write(args):
    """Searches for applications that can be used to write to files"""
    #TODO
    
def read(args):
    """Searches for applications that can be used to read files"""
    #TODO
    
def load(args):
    """Searches for applications that load shared libraries"""
    #TODO
    
def suid(args):
    """Searches for applications that, with the SUID bit set, can be used to 
    escalate privileges
    """
    #TODO
    
def sudo(args):
    """Searches for applications that, when run with sudo, can be used to 
    escalate privileges
    """
    #TODO
    
def cap(args):
    """Searches for applications that have the 'CAP_SETUID' capability set"""
    #TODO

def lsuid(args):
    """Searches for applications that, with the SUID bit set, can be used to 
    escalate privileges on systems that allow the default 'sh' shell to run 
    with sudo privileges
    """
    #TODO
    
def all(args):
    """Searches for applications in all categories"""
    #TODO
        
        
if __name__ == "__main__":
    args = parseArgs()
    args.func(args)
