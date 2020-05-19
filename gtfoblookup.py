#!/usr/bin/env python


"""Released as open source by NCC Group Plc - http://www.nccgroup.com/

Developed by James Conlan, James.Conlan@nccgroup.com

https://github.com/nccgroup/GTFOBLookup

You should have received a copy of the GNU General Public License along with 
GTFOBLookup. If not, see https://www.gnu.org/licenses.
"""


import argparse
from appdirs import user_cache_dir
import colorama
from git import Repo
import os
import re
import shutil
import sys
import textwrap
import yaml


repodir = user_cache_dir("GTFOBLookup", "NCC Group")

repos = {"GTFOBins": {
                    "url": "https://github.com/GTFOBins/GTFOBins.github.io.git",
                    "dir": os.path.join(repodir, "GTFOBins.github.io"),
                    "exeDirs": ["_gtfobins"],
                    "exeFileExt": ".md",
                    "opSys": "linux",
                    "cats": {"shell": "shell",
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
                             "lsuid": "limited-suid",
                             "all": "all"
                            },
                    "types": {},
                    "searchFunc": "gtfobSearch"
                    },
         "LOLBAS": {"url": "https://github.com/LOLBAS-Project/LOLBAS.git", 
                    "dir": os.path.join(repodir, "LOLBAS"),
                    "exeDirs": ["yml/OSBinaries", "yml/OSLibraries", 
                                "yml/OSScripts", "yml/OtherMSBinaries"],
                    "exeFileExt": ".yml",
                    "opSys": "windows",
                    "cats": {"ads": "ADS",
                             "awl": "AWL Bypass",
                             "comp": "Compile",
                             "copy": "Copy",
                             "creds": "Credentials",
                             "decode": "Decode",
                             "download": "Download",
                             "dump": "Dump",
                             "encode": "Encode",
                             "exec": "Execute",
                             "recon": "Reconnaissance",
                             "uac": "UAC Bypass",
                             "upload": "Upload",
                             "all": "all"
                             },
                    "types": {"bin": {"name": "Binary", "exeDirsIdx": 0},
                              "lib": {"name": "Library", "exeDirsIdx": 1},
                              "script": {"name": "Script", "exeDirsIdx": 2},
                              "other": {"name": "OtherMSBinary", 
                                        "exeDirsIdx": 3},
                              "all": {"name": "all"}
                             },
                    "searchFunc": "lolbasSearch"
                   }
        }

#Text formatting
green = "\033[32m"
red = "\033[31m"
bold = "\033[1m"
dim = "\033[2m"
reset = "\033[0m"


def genParser():
    """Generates a parser for command line arguments"""
    parser = argparse.ArgumentParser(description="Offline command line lookup" +
                                     " utility for GTFOBins " + 
                                     "(https://gtfobins.github.io/) and " +
                                     "LOLBAS " + 
                                     "(https://lolbas-project.github.io/)")
    parser.set_defaults(func=printUsage, parser=parser)
    subparsers = parser.add_subparsers()
    #Update
    parserUpdate = subparsers.add_parser('update', help="update local copies " + 
                                         "of repositories")
    parserUpdate.set_defaults(func=update)
    parserUpdate.add_argument('-r', '--repo', help="Only update the specified" +
                              " repository", metavar="repo", action='store', 
                              dest='repo')
    #Purge
    parserPurge = subparsers.add_parser('purge', help="remove local copies of" + 
                                        " repositories")
    parserPurge.set_defaults(func=purge)
    parserPurge.add_argument('-r', '--repo', help="Only delete the specified" +
                              " repository", metavar="repo", action='store', 
                             dest='repo')
    #Linux
    parserLinux = subparsers.add_parser('linux', help="search the local copy " +
                                        "of GTFOBins")
    parserLinux.set_defaults(func=default, parser=parserLinux, 
                             repo="GTFOBins")
    linSubparsers = parserLinux.add_subparsers()
    #Windows
    parserWindows = subparsers.add_parser('windows', help="search the local " +
                                        "copy of LOLBAS")
    parserWindows.set_defaults(func=default, parser=parserWindows, 
                               repo="LOLBAS")
    winSubparsers = parserWindows.add_subparsers()
    #Common options
    for repo in repos:
        parentParser = "parser{0}".format(repos[repo]['opSys'].capitalize())
        #List
        locals()[parentParser].add_argument('-l', '--list', help="list all" + 
                                            " types/categories/executables " +
                                            "featured in the local copy of " +
                                            "{0}".format(repo), 
                                            metavar="list", 
                                            action='store', dest='list')
        #Categories
        osAbbr = repos[repo]['opSys'][:3]
        parentParser = "{0}Subparsers".format(osAbbr)
        for cat in repos[repo]['cats']:
            parserName = "parser{0}{1}".format(osAbbr.capitalize(),
                                               cat.capitalize())
            if cat == "all":
                helptxt = "search all categories of {0}".format(repo)
            else:
                helptxt = ("search the '{0}".format(repos[repo]['cats'][cat]) +
                           "' category of {0}".format(repo))
            vars()[parserName] = locals()[parentParser].add_parser(cat, 
                                                                   help=helptxt)
            vars()[parserName].set_defaults(func=search, 
                                            cat=repos[repo]['cats'][cat], 
                                            typ="all")
            vars()[parserName].add_argument('-f', '--file', help="use a file " + 
                                            "containing a list of executables" +
                                            " (one per line) instead of a " +
                                            "single executable", 
                                            action='store_const', 
                                            const=parseFile, 
                                            dest='func')
            #Types
            if repos[repo]['types']:
                vars()[parserName].add_argument('-t', '--type', 
                                                help="search for a specific " +
                                                "type of executable", 
                                                metavar="type",
                                                action='store', dest='typ')
            vars()[parserName].add_argument('executable', 
                                            help='the executable to search for')
            
    return parser
    
def exit():
    """Exits the program"""
    colorama.deinit()
    sys.exit()
    
def printUsage(args):
    """Prints parser usage instructions for a given parser"""
    args.parser.print_usage()
    
def repCheck(repo):
    """Exits the program if no local copy of the specified repo is found"""
    if not os.path.exists(repos[repo]['dir']):
        print(red + "Local copy of {0} not found, please ".format(repo) + 
              "update" + reset)
        exit()

def genReposToChange(args):
    """Generates a list of repositories to perform an action on"""
    toChange = []
    if not args.repo or args.repo == "all":
        for repo in repos:
            toChange.append(repo)
    else:
        for repo in repos:
            if repo.lower() == args.repo.lower():
                toChange.append(repo)
    return toChange

def errorInvalidRepo():
    """Prints invalid repository error"""
    print("Repository must be one of {0}".format(list(repos.keys())))
        
def update(args):
    """Updates local copies of GTFOBins and LOLBAS"""
    toUpdate = genReposToChange(args)
    if toUpdate:
        for repo in toUpdate:
            print("Checking {0} for updates...".format(repo))
            if not os.path.exists(repos[repo]['dir']):
                print("Local copy of {0} not found, ".format(repo) + 
                      "downloading...")
                Repo.clone_from(repos[repo]['url'], repos[repo]['dir'])
                print(green + "Local copy of {0} downloaded".format(repo) + 
                      reset)
            else:
                rep = Repo(repos[repo]['dir'])
                current = rep.head.commit
                rep.remotes.origin.pull()
                if current == rep.head.commit:
                    print(green + "Local copy of {0} is up to ".format(repo) + 
                          "date" + reset)
                else:
                    print(green + "Local copy of {0} ".format(repo) + 
                          "updated" + reset)
    else:
        errorInvalidRepo()
            
def purge(args):
    """Removes local copies of GTFOBins and LOLBAS"""
    toPurge = genReposToChange(args)
    if toPurge:
        for repo in toPurge:
            if os.path.exists(repos[repo]['dir']):
                shutil.rmtree(repos[repo]['dir'], ignore_errors=True)
                print(green + "Local copy of {0} deleted".format(repo) + reset)
            else:
                print(red + "Local copy of {0} not found".format(repo) + reset)
    else:
        errorInvalidRepo()
        
def parseYaml(path):
    """Parses yaml found in file at given path"""
    with open(path) as f:
        yml = f.read()
    return yaml.load_all(yml, Loader=yaml.FullLoader)
        
def listExes(args):
    """Lists the executables featured in the local copy of a repo"""
    exes = []
    for folder in repos[args.repo]['exeDirs']:
        for file in os.listdir(os.path.join(repos[args.repo]['dir'], folder)):
            if file.endswith(repos[args.repo]['exeFileExt']):
                if repos[args.repo]['exeFileExt'] == ".md":
                    exes.append(file[:-3])
                elif repos[args.repo]['exeFileExt'] == ".yml":
                    ymlParsed = parseYaml(os.path.join(repos[args.repo]['dir'], 
                                          folder, file))
                    for data in ymlParsed:
                        if data is not None:
                            exes.append(data['Name'])
    exes.sort(key=str.lower)
    maxLen = len(max(exes, key=len))
    cols = 5
    cols -= maxLen / 20
    cols = int(cols)
    if cols == 0:
        cols += 1
    splitExes = [exes[x:x+cols] for x in range(0, len(exes), cols)]
    lineFormat = "{:<" + str(maxLen + 3) + "}"
    for line in splitExes:
        lineOut = ""
        for executable in line:
            lineOut += lineFormat.format(executable)
        print(lineOut)
        
def listCats(args):
    """Lists the categories featured in the local copy of a repo"""
    if repos[args.repo]['cats']:
        for cat in sorted(list(repos[args.repo]['cats'].keys()), key=str.lower):
            if cat != "all":
                print(bold + cat + reset + ": " + repos[args.repo]['cats'][cat])
    else:
        print(red + args.repo + " has no categories" + reset)
    
def listTypes(args):
    """Lists the types featured in the local copy of a repo"""
    if repos[args.repo]['types']:
        for typ in sorted(list(repos[args.repo]['types'].keys()), 
                          key=str.lower):
            if typ != "all":
                print(bold + typ + reset + ": " + 
                      repos[args.repo]['types'][typ]['name'])
    else:
        print(red + args.repo + " has no types" + reset)
        
def lst(args):
    """Lists categories/types/binaries in a repo"""
    repCheck(args.repo)
    if args.list.lower() == "executables":
        listExes(args)
    elif args.list.lower() == "categories":
        listCats(args)
    elif args.list.lower() == "types":
        listTypes(args)
    else:
        print("Cannot list '{0}'. Valid options are: ".format(args.list) + 
              "'executables', 'categories', and 'types'")
        
def errorNoCatResults():
    """Prints no results found for this exe error"""
    print(red + "        No results of this type were found " +
                          "for this executable \n" + reset)
    
def calcSubIndent(initIndent, title, addSpacing):
    """Generates subindent based on given title, initial indent, and additional 
    spacing
    """
    subIndent = initIndent
    for i in range(len(title) + addSpacing):
        subIndent += " "
    return subIndent
    
def extractMd(cat, path):
    """Extracts details of a specified function of a specified binary from the 
    local copy of GTFOBins
    """
    print("    {0}{1}{2}:\n".format(bold, cat, reset))
    md = parseYaml(path)
    indent = "        "
    for data in md:
            if data is not None:
                try:
                    for func in data['functions'][cat]:
                        for attr in func:
                            lines = func[attr].split("\n")
                            initLine = "{0}{1}{2}: ".format(bold, 
                                                           attr.capitalize(),
                                                           reset)
                            if attr == "code":
                                initLine += dim
                            initLine += lines[0]
                            lines.pop(0)
                            subIndent = calcSubIndent(indent, attr, 2)
                            print(textwrap.fill(initLine, width=80,
                                                  initial_indent=indent, 
                                                  subsequent_indent=subIndent))
                            for line in lines:
                                if line != '':
                                    print(textwrap.fill(line, width=80,
                                          initial_indent=subIndent, 
                                          subsequent_indent=subIndent))
                        print(reset)
                except:
                    errorNoCatResults()
                    
def splitOnCap(string):
    """Splits a string into words based on capitalisation whilst preserving 
    acronyms
    """
    split = re.sub( r"([A-Z])", r" \1", string).split()
    newString = ""
    for i in range(len(split)):
        if len(split[i]) == 1 and len(split[i-1]) == 1:
            newString += split[i]
        else:
            newString += " " + split[i]
    return newString
                    
def extractYml(cat, path):
    """Extracts details of a specified function of a specified executable of a 
    specified type from the local copy of LOLBAS
    """
    print("    {0}{1}{2}:\n".format(bold, cat, reset))
    yml = parseYaml(path)
    indent = "        "
    results = False
    for data in yml:
            if data is not None:
                for cmd in data['Commands']:
                    if cmd['Category'] == cat:
                        results = True
                        for attr in cmd:
                            if attr != "Category":
                                line = "{0}{1}{2}: ".format(bold, 
                                                               splitOnCap(attr),
                                                               reset)
                                if attr == "Command":
                                    line += dim
                                line += cmd[attr]
                                line += reset
                                subIndent = calcSubIndent(indent, attr, 3)
                                print(textwrap.fill(line, width=80,
                                                  initial_indent=indent, 
                                                  subsequent_indent=subIndent))
                        print() #Prints newline character
    if not results:
        errorNoCatResults()
    
def extract(args, path, extractFunc):
    """Uses a specified extraction function to extract data on a specified
    executable from specified categories of a specified repo
    """
    if args.cat == "all":
        for cat in repos[args.repo]['cats'].values():
            if cat != "all":
                extractFunc(cat, path)
    else:
        extractFunc(args.cat, path)
        
def errorExeNotFound(args):
    """Prints exe not found error message"""
    if args.typ == "all":
        print(red + "'{0}' was not found in the local copy of ".format(
              args.executable) + args.repo + reset)
    else:
        print(red + "'{0}' was not found in the local copy of ".format(
              args.executable) + args.repo + " with type '{0}'".format(
              repos[args.repo]['types'][args.typ]['name']) + reset)
    
def gtfobSearch(args):
    """Searches local copy of GTFOBins for a specified executable in a 
    specified category
    """
    repCheck(args.repo)
    exe = args.executable.lower()
    path = os.path.join(repos[args.repo]['dir'], repos[args.repo]['exeDirs'][0], 
                        exe + repos[args.repo]['exeFileExt'])
    if os.path.isfile(path):   
        print(green + bold + exe + reset + green + ":\n" + reset)
        extract(args, path, extractMd)
    else:
        errorExeNotFound(args)
        
def typCheck(args):
    """Checks if a specified type is valid for a specified repo"""
    if args.typ.lower() not in repos[args.repo]['types'].keys():
        print("Invalid type supplied, run " + dim + "gtfoblookup.py " + 
              repos[args.repo]['opSys'] + " --list types" + reset + " to see " + 
              "all valid types")
        exit()    

def lolbasSearch(args):
    """Searches local copy of LOLBAS for a specified executable of a specified 
    type in a specified category
    """
    repCheck(args.repo)
    exe = args.executable.lower()
    exeSplit = exe.split(".")
    parts = []
    if len(exeSplit) > 1:
        for i in exeSplit:
            i = parts.append(i.capitalize())
        exe = ".".join(parts[:-1])
    else:
        exe = exe.capitalize()
    typCheck(args)
    paths = []
    if args.typ == "all":
        for exeDir in repos[args.repo]['exeDirs']:
            paths.append(os.path.join(repos[args.repo]['dir'], exeDir, exe + 
                                      repos[args.repo]['exeFileExt']))
    else:
        paths.append(os.path.join(repos[args.repo]['dir'],
 repos[args.repo]['exeDirs'][repos[args.repo]['types'][args.typ]['exeDirsIdx']],
                     exe + repos[args.repo]['exeFileExt']))
    for path in paths:
        if os.path.isfile(path):   
            try:
                name = "{0}.{1}".format(exe, parts[-1].lower())
            except:
                name = exe
            parsed = parseYaml(path)
            for data in parsed:
                if data is not None and data['Name'] == name:
                    print(green + bold + name + reset + green + ":\n" + reset)        
                    extract(args, path, extractYml)
                    return
    errorExeNotFound(args)
    
def search(args):
    """Searches local copy of specified repo for a specified executable of a 
    specified type in a specified category
    """
    globals()[repos[args.repo]['searchFunc']](args)

def parseFile(args):
    """Parses a list of executables in a supplied file"""
    with open(args.executable, 'r') as f:
        exes = f.readlines()
    for exe in exes:
        if exe.strip() != "":
            args.executable = exe.strip()
            search(args)
            
def default(args):
    """The default function to run if no arguments are specified"""
    if args.list:
        lst(args)
    else:
        printUsage(args)
        
if __name__ == "__main__":
    if sys.version_info[0] < 3:
	    print(red + "Some functionality only works with Python3. Please " + 
			  "switch to using Python3 to make the most of GTFOBLookup." + 
			  reset)
    args = genParser().parse_args()
    colorama.init()
    args.func(args)
    colorama.deinit()
