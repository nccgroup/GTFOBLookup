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
                    "categories": {"shell": "shell",
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
                    "prereqs": {},
                    "services": {},
                    "attacktypes": {},
                    "os": {},
                    "searchFunc": "gtfobSearch"
                    },
         "LOLBAS": {"url": "https://github.com/LOLBAS-Project/LOLBAS.git", 
                    "dir": os.path.join(repodir, "LOLBAS"),
                    "exeDirs": ["yml/OSBinaries", "yml/OSLibraries", 
                                "yml/OSScripts", "yml/OtherMSBinaries"],
                    "exeFileExt": ".yml",
                    "categories": {"ads": "ADS",
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
                    "prereqs": {},
                    "services": {},
                    "attacktypes": {},
                    "os": {},
                    "searchFunc": "lolbasSearch"
                   },
         "WADComs": {"url": "https://github.com/WADComs/WADComs.github.io.git", 
                    "dir": os.path.join(repodir, "WADComs"),
                    "exeDirs": ["_wadcoms"],
                    "exeFileExt": ".md",
                    "categories": {},
                    "types": {},
                    "prereqs": {"username": "Username",
                                "password": "Password",
                                "nocreds": "No_Creds",
                                "hash": "Hash",
                                "shell": "Shell",
                                "all": "all"
                               },
                    "services": {"smb": "SMB",
                                 "wmi": "WMI",
                                 "dcom": "DCOM",
                                 "kerberos": "Kerberos",
                                 "rpc": "RPC",
                                 "ldap": "LDAP",
                                 "ntlm": "NTLM",
                                 "all": "all"
                                },
                    "attacktypes": {"enum": "Enumeration",
                                   "exploit": "Exploitation",
                                   "persistence": "Persistence",
                                   "privesc": "PrivEsc",
                                   "all": "all"
                                  },
                    "os": {"windows": "Windows",
                           "linux": "Linux",
                           "all": "all"
                          },
                    "searchFunc": "wadcomsSearch"
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
                                     "(https://gtfobins.github.io/), LOLBAS" +
                                     "(https://lolbas-project.github.io/), " +
                                     "and WADComs (https://wadcoms.github.io)")
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
    #GTFOBins
    parserGtfobins = subparsers.add_parser('gtfobins', help="search the local" +
                                        " copy of GTFOBins")
    parserGtfobins.set_defaults(func=printUsage, parser=parserGtfobins, 
                             repo="GTFOBins")
    gtfobinsSubparsers = parserGtfobins.add_subparsers()
    #LOLBAS
    parserLolbas = subparsers.add_parser('lolbas', help="search the local " +
                                        "copy of LOLBAS")
    parserLolbas.set_defaults(func=printUsage, parser=parserLolbas, 
                               repo="LOLBAS")
    lolbasSubparsers = parserLolbas.add_subparsers()
    #WADComs
    parserWadcoms = subparsers.add_parser('wadcoms', help="search the local " +
                                        "copy of WADComs")
    parserWadcoms.set_defaults(func=printUsage, parser=parserWadcoms, 
                               repo="WADComs")
    wadcomsSubparsers = parserWadcoms.add_subparsers()
    #Common options
    for repo in repos:
        parentParser = "parser{0}".format(repo.lower().capitalize())
        subparsers = "{0}Subparsers".format(repo.lower())
        #List
        parserList = locals()[subparsers].add_parser('list', help="list all " + 
                                            "types/categories/executables/" +
                                            "prerequisites/services/attack " +
                                            "types/OSs featured in the local " +
                                            "copy of {0}".format(repo))
        parserList.set_defaults(func=lst)
        parserList.add_argument('attribute', help="the attribute to list")
        #Search
        parserSearch = locals()[subparsers].add_parser('search', help="search" +
                                                       "the {0} ".format(repo) +
                                                       "repository")
        parserSearch.set_defaults(func=search, parser=parserSearch)
        #Category
        if repos[repo]['categories']:
            parserSearch.add_argument('-c', '--category', help="category or " +
                                      "categories (comma separated) to search" +
                                      " in", action='store', dest='cats',
                                      metavar='categories')
            parserSearch.set_defaults(cats="all")
        #Type
        if repos[repo]['types']:
            parserSearch.add_argument('-t', '--type', help="type or types " +
                                      "(comma separated)of executable to " + 
                                      "search for", action='store',
                                      dest='types', metavar='types')
            parserSearch.set_defaults(types="all")
        #Prereqs
        if repos[repo]['prereqs']:
            parserSearch.add_argument('-p', '--prereq', help="search for " +
                                      "executables with a specific " +
                                      "prerequisite or prerequisites (comma " +
                                      "separated)", action='store', 
                                      dest='prereqs', metavar='prerequisites')
            parserSearch.set_defaults(prereqs="all")
        #Services
        if repos[repo]['services']:
            parserSearch.add_argument('-s', '--service', help="search for " +
                                      "executables that interract with a" +
                                      "specific service or services" +
                                      "(comma separated)", action='store',
                                      dest='services', metavar='services')
            parserSearch.set_defaults(services="all")
        #Attack Types
        if repos[repo]['attacktypes']:
            parserSearch.add_argument('-a', '--attacktype', help="search for " +
                                      "executables that can be used for a" +
                                      "specific type or types (comma " +
                                      "separated) of attacks", action='store',
                                      dest='attackTypes', metavar='attack_types'
                                     )
            parserSearch.set_defaults(attackTypes="all")
        #OSs
        if repos[repo]['os']:
            parserSearch.add_argument('-o', '--os', help="search for " +
                                      "executables that can be run on a " +
                                      "specific operating system or" +
                                      "operating systems (comma separated)",
                                      action='store', dest='os', metavar='OSs')
            parserSearch.set_defaults(os="all")
        #File
        parserSearch.add_argument('-f', '--file', help="use a file " + 
                                  "containing a list of executables (one per " +
                                  "line) instead of a single executable", 
                                  action='store_const', const=parseFile, 
                                  dest='func')
        #Executable
        parserSearch.add_argument('executable', help="the executable to " +
                                  "search for (use \"all\" to show results " +
                                  "for all executables")
    return parser

def printUsage(args):
    """Prints parser usage instructions for a given parser"""
    args.parser.print_usage()
    
def repCheck(repo):
    """Exits the program if no local copy of the specified repo is found"""
    if not os.path.exists(repos[repo]['dir']):
        print(red + "Local copy of {0} not found, please ".format(repo) + 
              "update" + reset)
        sys.exit()

def errorInvalidRepo():
    """Prints invalid repository error"""
    print("Repository must be one of {0}".format(list(repos.keys())))

def genReposToChange(args):
    """Generates a list of repositories to perform an action on"""
    toChange = []
    if not args.repo or args.repo == "all":
        for repo in repos:
            toChange.append(repo)
    else:
        argRepos = args.repo.split(",")
        for repo in argRepos:
            if repo.lower() in [x.lower() for x in repos]:
                toChange.append(repo)
            else:
                errorInvalidRepo()
    return toChange

def update(args):
    """Updates local copies of repos"""
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
    """Removes local copies of repos"""
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
    if os.path.isfile(path):
        with open(path) as f:
            yml = f.read()
        data = yaml.load_all(yml, Loader=yaml.SafeLoader)
        objects = []
        for i in data:
            if i is not None:
                objects.append(i)
        return objects

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

def lst(args):
    """Lists attributes in a repo"""
    repCheck(args.repo)
    attr = args.attribute.lower()
    if attr == "executables":
        listExes(args)
    else:
        if attr in repos[args.repo]:
            if repos[args.repo][attr]:
                for i in sorted(list(repos[args.repo][attr].keys()),      
                                key=str.lower):
                    if i != "all":
                        if attr == "types":
                            print(bold + i + reset + ": " + repos[args.repo][
                                                               attr][i]['name'])
                        else:
                            print(bold + i + reset + ": " + repos[args.repo][
                                                                       attr][i])
            else:
                print(red + args.repo + " has no " + args.attribute + 
                      " attribute" + reset)
        else:
            print("Cannot list '{0}'. Valid options ".format(args.attribute) + 
                "are: 'executables', 'categories', 'types', 'prereqs', " +
                "'services', 'attacktypes', and 'os'")

def errorNoCatResults():
    """Prints no results found for this exe error"""
    print(red + "        No results were found for this executable with the " +
          "specified attributes \n" + reset)

def calcSubIndent(initIndent, title, addSpacing):
    """Generates subindent based on given title, initial indent, and additional 
    spacing
    """
    subIndent = initIndent
    for i in range(len(title) + addSpacing):
        subIndent += " "
    return subIndent

def extractMdGtfob(paths, attrs):
    """Extracts details of a specified function of a specified binary from the 
    local copy of GTFOBins
    """
    md = parseYaml(paths[0])
    indent = "        "
    for cat in attrs['categories']:
        print("    {0}{1}{2}:\n".format(bold, cat, reset))
        for data in md:
            if cat in data['functions']:
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
                                            subsequent_indent=subIndent)
                                            )
                        for line in lines:
                            if line != '':
                                print(textwrap.fill(line, width=80,
                                    initial_indent=subIndent, 
                                    subsequent_indent=subIndent))
                    print(reset)
            else:
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

def extractYmlLolbas(paths, attrs):
    """Extracts details of a specified function of a specified executable of a 
    specified type from the local copy of LOLBAS
    """
    ymls = []
    for path in paths:
        yml = (parseYaml(path))
        if yml is not None:
            ymls.append(yml)
    indent = "        "
    for cat in attrs['categories']:
        print("    {0}{1}{2}:\n".format(bold, cat, reset))
        results = False
        for yml in ymls:
            for data in yml:
                for cmd in data['Commands']:
                    if cmd['Category'] == cat:
                        for attr in cmd:
                            if attr != "Category":
                                line = "{0}{1}{2}: ".format(bold, splitOnCap(attr),
                                                            reset)
                                if attr == "Command":
                                    line += dim
                                line += cmd[attr] if cmd[attr] else 'N/A'
                                line += reset
                                subIndent = calcSubIndent(indent, attr, 3)
                                print(textwrap.fill(line, width=80,
                                                    initial_indent=indent, 
                                                    subsequent_indent=subIndent))
                        print() #Prints newline character
                        results = True
        if not results:
            errorNoCatResults()

def checkAttrs(dataLst, attrs, attr, field):
    """Checks if given values of a given attribute are present in a given field 
    of given data
    """
    for data in dataLst:
        results = False
        for attrib in attrs[attr]:
            try:
                if attrib in data[field]:
                    results = True
                    break
            except:
                results = True
                break
        if not results:
            dataLst.remove(data)
    return dataLst

def extractMdWadcoms(paths, attrs):
    """Extracts details of a specified executable with specified attributes from
    the local copy of WADComs
    """
    mds = {}
    for path in paths:
        md = parseYaml(path)
        if md != None:
            mds[os.path.split(path)[1].split(".")[0]] = md
    indent = "    "
    for md in mds:
        matches = checkAttrs(mds[md], attrs, "prereqs", "items")
        matches = checkAttrs(matches, attrs, "services", "services")
        matches = checkAttrs(matches, attrs, "attacktypes", "attack_types")
        matches = checkAttrs(matches, attrs, "os", "OS")
        if matches:
            print("{0}{1}{2}{3}{1}:{3}\n".format(bold, green, md, reset))
            for data in matches:
                for attr in data:
                    if type(data[attr]) == str:
                        lines = data[attr].split("\n")
                    else:
                        lines = data[attr]
                    initLine = "{0}{1}{2}: ".format(bold, attr.capitalize(),
                                                    reset)
                    if attr == "command":
                        initLine += dim
                    initLine += lines[0]
                    lines.pop(0)
                    subIndent = calcSubIndent(indent, attr, 2)
                    print(textwrap.fill(initLine, width=80,
                                        initial_indent=indent, 
                                        subsequent_indent=subIndent)
                                        )
                    if lines:
                        lastLine = lines.pop()
                        lastLine += reset
                        lines.append(lastLine)
                        for line in lines:
                            if line != '':
                                print(textwrap.fill(line, width=80,
                                    initial_indent=subIndent, 
                                    subsequent_indent=subIndent))
            print(reset)

def extract(args, paths, extractFunc):
    """Uses a specified extraction function to extract data on a specified
    executable with specified attributes from a specified repo
    """
    attrs = {}
    try:
        attrs['categories'] = args.cats.lower().split(",")
    except:
        attrs['categories'] = []
    try:
        attrs['prereqs'] = args.prereqs.lower().split(",")
    except:
        attrs['prereqs'] = []
    try:
        attrs['services'] = args.services.lower().split(",")
    except:
        attrs['services'] = []
    try:
        attrs['attacktypes'] = args.attackTypes.lower().split(",")
    except:
        attrs['attacktypes'] = []
    try:
        attrs['os'] = args.os.lower().split(",")
    except:
        attrs['os'] = []
    for attr in attrs:
        if "all" in attrs[attr]:
            attrs[attr] = list(repos[args.repo][attr].values())
            attrs[attr].remove("all")
        else:
            newVals = []
            for val in attrs[attr]:
                try:
                    newVals.append(repos[args.repo][attr][val])
                except:
                    pass
            attrs[attr] = newVals
    extractFunc(paths, attrs)

def errorExeNotFound(args):
    """Prints exe not found error message"""
    print(red + "'{0}' was not found in the local copy of ".format(
          args.executable) + args.repo + " with the specified attributes" +
          reset)

def checkExeFiles(exe, dir, extension):
    """Checks if a file exists in the specified dir that matches the specified
    exe and returns the matching filepath
    """
    files = os.listdir(dir)
    for f in files:
        parts = f.split(".")
        if parts[0].upper() == exe.upper() \
            and "." + parts[1].upper() == extension.upper():
            return os.path.join(dir, f)
    return None

def gtfobSearch(args):
    """Searches local copy of GTFOBins for a specified executable in a 
    specified category
    """
    repCheck(args.repo)
    exe = args.executable.lower()
    dir = os.path.join(repos[args.repo]['dir'], repos[args.repo]['exeDirs'][0])
    paths = []
    if exe == "all":
        for f in os.listdir(dir):
            if f.endswith(repos['GTFOBins']['exeFileExt']):
                paths.append(os.path.join(dir, f))
    else:
        paths.append(checkExeFiles(exe, dir, repos['GTFOBins']['exeFileExt']))
    for path in paths:
        if path is not None and os.path.isfile(path):   
            print(path)
            print(green + bold + path.split("/")[-1].split(".")[0] + reset + 
                  green + ":\n" + reset)
            extract(args, [path], extractMdGtfob)
        else:
            errorExeNotFound(args)

def lolbasSearch(args):
    """Searches local copy of LOLBAS for a specified executable of a specified 
    type in a specified category
    """
    repCheck(args.repo)
    exe = args.executable.lower()
    exeSplit = exe.split(".")
    if len(exeSplit) > 1:
        exe = ".".join(exeSplit[:-1])
    paths = []
    if args.types:
        types = args.types.lower().split(",")
        if "all" in types:
            for i in repos[args.repo]['types'].values():
                if i['name'] != "all":
                    dir = os.path.join(repos[args.repo]['dir'],
                                   repos[args.repo]["exeDirs"][i['exeDirsIdx']])
                    if exe == "all":
                        for f in os.listdir(dir):
                            if f.endswith(repos['LOLBAS']['exeFileExt']):
                                paths.append(os.path.join(dir, f))
                    else:
                        f = checkExeFiles(exe, dir,
                                          repos['LOLBAS']['exeFileExt'])
                        if f is not None: paths.append(f) 
        else:
            for typ in types:
                if typ in repos[args.repo]['types']:
                    dir = os.path.join(repos[args.repo]['dir'],
                                      repos[args.repo]["exeDirs"][repos[
                                      args.repo]['types'][typ]['exeDirsIdx']])
                    if exe == "all":
                        for f in os.listdir(dir):
                            if f.endswith(repos['LOLBAS']['exeFileExt']):
                                paths.append(os.path.join(dir, f))
                    else:
                        f = checkExeFiles(exe, dir,
                                          repos['LOLBAS']['exeFileExt'])
                        if f is not None: paths.append(f) 
    tryExtract = False
    for path in paths:
        if exe == "all":
            parsed = parseYaml(path)
            for data in parsed:
                if data is not None:
                    print(green + bold + data['Name'] + reset + green + ":\n" +
                          reset)        
                    tryExtract = True
                    break
        elif os.path.isfile(path):   
            if len(exeSplit) > 2:
                name = "{0}.{1}".format(exe, exeSplit[-1].lower())
            else:
                name = exe
            parsed = parseYaml(path)
            for data in parsed:
                if data is not None and (data['Name'].upper() == name.upper() or 
                data['Name'].upper().startswith(name.upper() + ".")):
                    print(green + bold + name + reset + green + ":\n" + reset)        
                    tryExtract = True
                    break
        if tryExtract:
            extract(args, [path], extractYmlLolbas)
        else:
            errorExeNotFound(args)

def wadcomsSearch(args):
    """Searches local copy of WADComs for a specified executable with specified
    attributes
    """
    repCheck(args.repo)
    searchPath = os.path.join(repos[args.repo]['dir'], repos[args.repo][
                 'exeDirs'][0])
    searchName = args.executable.capitalize() if (args.executable.lower() == 
                 args.executable) else args.executable
    paths = []
    results = False
    if args.executable.lower() == "all":
        for f in os.listdir(searchPath):
            if f.endswith(repos['WADComs']['exeFileExt']):
                paths.append(os.path.join(searchPath, f))
    else:
        paths.append(checkExeFiles(args.executable, searchPath,
                                repos['WADComs']['exeFileExt']))
    if len(paths):
        extract(args, paths, extractMdWadcoms)
    else:
        errorExeNotFound(args)

def search(args):
    """Searches local copy of specified repo for a specified executable of a 
    specified type in a specified category
    """
    globals()[repos[args.repo]['searchFunc']](args)

def parseFile(args):
    """Parses a list of executables in a supplied file"""
    try:
        with open(args.executable, 'r') as f:
            exes = f.readlines()
    except FileNotFoundError as e:
        sys.exit("{0}File '{1}' does not exist{2}".format(red, args.executable, reset))
    for exe in exes:
        exe = exe.strip()
        if exe != "":
            split = exe.split('/')
            if len(split) > 1:
                exe = split[-1]
            else:
                split = exe.split('\\')
                exe = split[-1]
            args.executable = exe
            search(args)

if __name__ == "__main__":
    if sys.version_info[0] < 3:
	    print(red + "Some functionality only works with Python3. Please " + 
			  "switch to using Python3 to make the most of GTFOBLookup." + 
			  reset)
    args = genParser().parse_args()
    colorama.init()
    args.func(args)
