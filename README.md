# GTFOBLookup
Offline command line lookup utility for [GTFOBins](https://gtfobins.github.io/), [LOLBAS](https://lolbas-project.github.io/), [WADComs](https://wadcoms.github.io), and [HijackLibs](https://hijacklibs.net/).

## Files
- **.gitignore**: Gitignore file
- **gtfoblookup.1**: Linux man page for GTFOBLookup
- **gtfoblookup.py**: GTFOBLookup utility
- **LICENSE.md**: License file
- **README.md**: This file
- **requirements.txt**: List of required Python packages

## Dependencies
Whilst GTFOBLookup will run in Python2.7, some features require Python3.

GTFOBLookup requires the following non-standard Python libraries to be installed:
- appdirs (`pip install appdirs`)
- colorama (`pip install colorama`)
- git (`pip install gitpython`)
- yaml (`pip install pyyaml`)

These can all be installed with the following command: `pip install -r requirements.txt`

## Installation/Setup
It is recommended to install GTFOBLookup using pipx:
<pre>
pipx install git+https://github.com/nccgroup/GTFOBLookup.git
</pre>

Once installed, run `gtfoblookup.py update` whilst connected to the internet to download local copies of the repositories.

## Usage
On Linux, navigate to the GTFOBLookup directory and run `man ./gtfoblookup.1` or see below:
<pre>
gtfoblookup.py [-h] {update,purge,gtfobins,lolbas,wadcoms,hijacklibs} ...

OPTIONS
   Sub-commands
       gtfoblookup.py update
              update local copies of repositories

       gtfoblookup.py purge
              remove local copies of repositories

       gtfoblookup.py gtfobins
              search the local copy of GTFOBins

       gtfoblookup.py lolbas
              search the local copy of LOLBAS

       gtfoblookup.py wadcoms
              search the local copy of WADComs

       gtfoblookup.py hijacklibs
              search the local copy of HijackLibs

OPTIONS 'gtfoblookup.py update'
       usage: gtfoblookup.py update [-h] [-r repo]

       -r repo, --repo repo
              Only update the specified repository

OPTIONS 'gtfoblookup.py purge'
       usage: gtfoblookup.py purge [-h] [-r repo]

       -r repo, --repo repo
              Only delete the specified repository

OPTIONS 'gtfoblookup.py gtfobins'
       usage: gtfoblookup.py gtfobins [-h] {list,search} ...

   Sub-commands
       gtfoblookup.py gtfobins list
              list all types/categories/executables/prerequisites/services/attack types/OSs featured in the local copy of GTFOBins

       gtfoblookup.py gtfobins search
              searchthe GTFOBins repository

OPTIONS 'gtfoblookup.py gtfobins list'
       usage: gtfoblookup.py gtfobins list [-h] attribute

       attribute
              the attribute to list

OPTIONS 'gtfoblookup.py gtfobins search'
       usage: gtfoblookup.py gtfobins search [-h] [-c categories] [-f] executable

       executable
              the executable to search for

       -c categories, --category categories
              category or categories (comma separated) to search in

       -f, --file
              use a file containing a list of executables (one per line) instead of a single executable

OPTIONS 'gtfoblookup.py lolbas'
       usage: gtfoblookup.py lolbas [-h] {list,search} ...

   Sub-commands
       gtfoblookup.py lolbas list
              list all types/categories/executables/prerequisites/services/attack types/OSs featured in the local copy of LOLBAS

       gtfoblookup.py lolbas search
              searchthe LOLBAS repository

OPTIONS 'gtfoblookup.py lolbas list'
       usage: gtfoblookup.py lolbas list [-h] attribute

       attribute
              the attribute to list

OPTIONS 'gtfoblookup.py lolbas search'
       usage: gtfoblookup.py lolbas search [-h] [-c categories] [-t types] [-f]
                                             executable

       executable
              the executable to search for

       -c categories, --category categories
              category or categories (comma separated) to search in

       -t types, --type types
              type or types (comma separated)of executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single executable

OPTIONS 'gtfoblookup.py wadcoms'
       usage: gtfoblookup.py wadcoms [-h] {list,search} ...

   Sub-commands
       gtfoblookup.py wadcoms list
              list all types/categories/executables/prerequisites/services/attack types/OSs featured in the local copy of WADComs

       gtfoblookup.py wadcoms search
              searchthe WADComs repository

OPTIONS 'gtfoblookup.py wadcoms list'
       usage: gtfoblookup.py wadcoms list [-h] attribute

       attribute
              the attribute to list

OPTIONS 'gtfoblookup.py wadcoms search'
       usage: gtfoblookup.py wadcoms search [-h] [-p prerequisites] [-s services]
                                              [-a attack_types] [-o OSs] [-f]
                                              executable

       executable
              the executable to search for

       -p prerequisites, --prereq prerequisites
              search for executables with a specific prerequisite or prerequisites (comma separated)

       -s services, --service services
              search for executables that interract with aspecific service or services(comma separated)

       -a attack_types, --attacktype attack_types
              search for executables that can be used for aspecific type or types (comma separated) of attacks

       -o OSs, --os OSs
              search for executables that can be run on a specific operating system oroperating systems (comma separated)

       -f, --file
              use a file containing a list of executables (one per line) instead of a single executable

OPTIONS 'gtfoblookup.py hijacklibs'
       usage: gtfoblookup.py hijacklibs [-h] {list,search} ...

  Sub-commands 'gtfoblookup.py hijacklibs'
       gtfoblookup.py hijacklibs list
              list all types/categories/executables/prerequisites/services/attack types/OSs featured in the local copy of HijackLibs

       gtfoblookup.py hijacklibs search
              searchthe HijackLibs repository

OPTIONS 'gtfoblookup.py hijacklibs list'
       usage: gtfoblookup.py hijacklibs list [-h] attribute

       attribute
              the attribute to list

  Sub-commands 'gtfoblookup.py hijacklibs search'
       usage: gtfoblookup.py hijacklibs search [-h] [-a attack_types] [-v vendors] [-f] executable

       executable
              the executable to search for (use "all" to show results for all executables)

OPTIONS 'gtfoblookup.py hijacklibs search'
       -a attack_types, --attacktype attack_types
              search for executables that can be used for aspecific type or types (comma separated) of attacks

       -v vendors, --vendor vendors
              search for executables from a specific vendor or vendors (comma separated)

       -f, --file
              use a file containing a list of executables (one per line) instead of a single executable
</pre>
