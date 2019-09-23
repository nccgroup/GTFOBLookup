# GTFOBLookup
Offline command line lookup utility for [GTFOBins](https://gtfobins.github.io/) and [LOLBAS](https://lolbas-project.github.io/).

## Files
- **.gitignore**: Gitignore file
- **gtfoblookup.1**: Linux man page for GTFOBLookup
- **gtfoblookup.py**: GTFOBLookup utility
- **LICENSE.md**: License file
- **README.md**: This file

## Dependencies
GTFOBLookup requires the following non-standard Python libraries to be installed:
- colorama (`pip3 install colorama`)
- git (`pip3 install gitpython`)
- yaml (`pip3 install pyyaml`)

## Installation/Setup
To install GTFOBLookup, git clone the repository to your machine and run `gtfoblookup.py update` whilst connected to the internet:

## usage
On Linux, navigate to the GTFOBLookup directory and run `man ./gtfoblookup.1` or see below:
<pre>
gtfoblookup.py [-h] {update,purge,linux,windows} ...

OPTIONS
   Sub-commands
       argparse-manpage update
              update local copies of repositories

       argparse-manpage purge
              remove local copies of repositories

       argparse-manpage linux
              search the local copy of GTFOBins

       argparse-manpage windows
              search the local copy of LOLBAS

OPTIONS 'argparse-manpage update'
       usage: argparse-manpage update [-h] [-r repo]

       -r repo, --repo repo
              Only update the specified repository

OPTIONS 'argparse-manpage purge'
       usage: argparse-manpage purge [-h] [-r repo]

       -r repo, --repo repo
              Only delete the specified repository

OPTIONS 'argparse-manpage linux'
       usage: argparse-manpage linux [-h] [-l list]
                                     {shell,cmd,rev,nrev,bind,nbind,upload,download,write,read,load,suid,sudo,cap,lsuid,all}
                                     ...

   Sub-commands
       argparse-manpage linux shell
              search the 'shell' category of GTFOBins

       argparse-manpage linux cmd
              search the 'command' category of GTFOBins

       argparse-manpage linux rev
              search the 'reverse-shell' category of GTFOBins

       argparse-manpage linux nrev
              search the 'non-interactive-reverse-shell' category of GTFOBins

       argparse-manpage linux bind
              search the 'bind-shell' category of GTFOBins

       argparse-manpage linux nbind
              search the 'non-interactive-bind-shell' category of GTFOBins

       argparse-manpage linux upload
              search the 'file-upload' category of GTFOBins

       argparse-manpage linux download
              search the 'file-download' category of GTFOBins

       argparse-manpage linux write
              search the 'file-write' category of GTFOBins

       argparse-manpage linux read
              search the 'file-read' category of GTFOBins

       argparse-manpage linux load
              search the 'library-load' category of GTFOBins

       argparse-manpage linux suid
              search the 'suid' category of GTFOBins

       argparse-manpage linux sudo
              search the 'sudo' category of GTFOBins

       argparse-manpage linux cap
              search the 'capabilities' category of GTFOBins

       argparse-manpage linux lsuid
              search the 'limited-suid' category of GTFOBins

       argparse-manpage linux all
              search all categories of GTFOBins

OPTIONS 'argparse-manpage linux shell'
       usage: argparse-manpage linux shell [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux cmd'
       usage: argparse-manpage linux cmd [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux rev'
       usage: argparse-manpage linux rev [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux nrev'
       usage: argparse-manpage linux nrev [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux bind'
       usage: argparse-manpage linux bind [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux nbind'
       usage: argparse-manpage linux nbind [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux upload'
       usage: argparse-manpage linux upload [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux download'
       usage: argparse-manpage linux download [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux write'
       usage: argparse-manpage linux write [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux read'
       usage: argparse-manpage linux read [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux load'
       usage: argparse-manpage linux load [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux suid'
       usage: argparse-manpage linux suid [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux sudo'
       usage: argparse-manpage linux sudo [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux cap'
       usage: argparse-manpage linux cap [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux lsuid'
       usage: argparse-manpage linux lsuid [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'argparse-manpage linux all'
       usage: argparse-manpage linux all [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -l list, --list list
              list all types/categories/executables featured in the local copy of GTFOBins

OPTIONS 'argparse-manpage windows'
       usage: argparse-manpage windows [-h] [-l list]
                                       {ads,awl,comp,copy,creds,decode,download,dump,encode,exec,recon,uac,upload,all}
                                       ...

   Sub-commands
       argparse-manpage windows ads
              search the 'ADS' category of LOLBAS

       argparse-manpage windows awl
              search the 'AWL Bypass' category of LOLBAS

       argparse-manpage windows comp
              search the 'Compile' category of LOLBAS

       argparse-manpage windows copy
              search the 'Copy' category of LOLBAS

       argparse-manpage windows creds
              search the 'Credentials' category of LOLBAS

       argparse-manpage windows decode
              search the 'Decode' category of LOLBAS

       argparse-manpage windows download
              search the 'Download' category of LOLBAS

       argparse-manpage windows dump
              search the 'Dump' category of LOLBAS

       argparse-manpage windows encode
              search the 'Encode' category of LOLBAS

       argparse-manpage windows exec
              search the 'Execute' category of LOLBAS

       argparse-manpage windows recon
              search the 'Reconnaissance' category of LOLBAS

       argparse-manpage windows uac
              search the 'UAC Bypass' category of LOLBAS

       argparse-manpage windows upload
              search the 'Upload' category of LOLBAS

       argparse-manpage windows all
              search all categories of LOLBAS

OPTIONS 'argparse-manpage windows ads'
       usage: argparse-manpage windows ads [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows awl'
       usage: argparse-manpage windows awl [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows comp'
       usage: argparse-manpage windows comp [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows copy'
       usage: argparse-manpage windows copy [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows creds'
       usage: argparse-manpage windows creds [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows decode'
       usage: argparse-manpage windows decode [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows download'
       usage: argparse-manpage windows download [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows dump'
       usage: argparse-manpage windows dump [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows encode'
       usage: argparse-manpage windows encode [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows exec'
       usage: argparse-manpage windows exec [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows recon'
       usage: argparse-manpage windows recon [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows uac'
       usage: argparse-manpage windows uac [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows upload'
       usage: argparse-manpage windows upload [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'argparse-manpage windows all'
       usage: argparse-manpage windows all [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

       -l list, --list list
              list all types/categories/executables featured in the local copy of LOLBAS
</pre>
