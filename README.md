# GTFOBLookup
Offline command line lookup utility for [GTFOBins](https://gtfobins.github.io/) and [LOLBAS](https://lolbas-project.github.io/).

## Files
- **.gitignore**: Gitignore file
- **gtfoblookup.1**: Linux man page for GTFOBLookup
- **gtfoblookup.py**: GTFOBLookup utility
- **LICENSE.md**: License file
- **README.md**: This file
- **requirements.txt**: List of required Python packages

## Dependencies
GTFOBLookup requires the following non-standard Python libraries to be installed:
- appdirs (`pip3 install appdirs`)
- colorama (`pip3 install colorama`)
- git (`pip3 install gitpython`)
- yaml (`pip3 install pyyaml`)

These can all be installed with the following command: `pip3 install -r requirements.txt`

## Installation/Setup
To install GTFOBLookup, git clone the repository to your machine and run `gtfoblookup.py update` whilst connected to the internet:

## usage
On Linux, navigate to the GTFOBLookup directory and run `man ./gtfoblookup.1` or see below:
<pre>
gtfoblookup.py [-h] {update,purge,linux,windows} ...

OPTIONS
   Sub-commands
       gtfoblookup.py update
              update local copies of repositories

       gtfoblookup.py purge
              remove local copies of repositories

       gtfoblookup.py linux
              search the local copy of GTFOBins

       gtfoblookup.py windows
              search the local copy of LOLBAS

OPTIONS 'gtfoblookup.py update'
       usage: gtfoblookup.py update [-h] [-r repo]

       -r repo, --repo repo
              Only update the specified repository

OPTIONS 'gtfoblookup.py purge'
       usage: gtfoblookup.py purge [-h] [-r repo]

       -r repo, --repo repo
              Only delete the specified repository

OPTIONS 'gtfoblookup.py linux'
       usage: gtfoblookup.py linux [-h] [-l list]
                                     {shell,cmd,rev,nrev,bind,nbind,upload,download,write,read,load,suid,sudo,cap,lsuid,all}
                                     ...

   Sub-commands
       gtfoblookup.py linux shell
              search the 'shell' category of GTFOBins

       gtfoblookup.py linux cmd
              search the 'command' category of GTFOBins

       gtfoblookup.py linux rev
              search the 'reverse-shell' category of GTFOBins

       gtfoblookup.py linux nrev
              search the 'non-interactive-reverse-shell' category of GTFOBins

       gtfoblookup.py linux bind
              search the 'bind-shell' category of GTFOBins

       gtfoblookup.py linux nbind
              search the 'non-interactive-bind-shell' category of GTFOBins

       gtfoblookup.py linux upload
              search the 'file-upload' category of GTFOBins

       gtfoblookup.py linux download
              search the 'file-download' category of GTFOBins

       gtfoblookup.py linux write
              search the 'file-write' category of GTFOBins

       gtfoblookup.py linux read
              search the 'file-read' category of GTFOBins

       gtfoblookup.py linux load
              search the 'library-load' category of GTFOBins

       gtfoblookup.py linux suid
              search the 'suid' category of GTFOBins

       gtfoblookup.py linux sudo
              search the 'sudo' category of GTFOBins

       gtfoblookup.py linux cap
              search the 'capabilities' category of GTFOBins

       gtfoblookup.py linux lsuid
              search the 'limited-suid' category of GTFOBins

       gtfoblookup.py linux all
              search all categories of GTFOBins

OPTIONS 'gtfoblookup.py linux shell'
       usage: gtfoblookup.py linux shell [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux cmd'
       usage: gtfoblookup.py linux cmd [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux rev'
       usage: gtfoblookup.py linux rev [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux nrev'
       usage: gtfoblookup.py linux nrev [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux bind'
       usage: gtfoblookup.py linux bind [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux nbind'
       usage: gtfoblookup.py linux nbind [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux upload'
       usage: gtfoblookup.py linux upload [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux download'
       usage: gtfoblookup.py linux download [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux write'
       usage: gtfoblookup.py linux write [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux read'
       usage: gtfoblookup.py linux read [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux load'
       usage: gtfoblookup.py linux load [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux suid'
       usage: gtfoblookup.py linux suid [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux sudo'
       usage: gtfoblookup.py linux sudo [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux cap'
       usage: gtfoblookup.py linux cap [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux lsuid'
       usage: gtfoblookup.py linux lsuid [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

OPTIONS 'gtfoblookup.py linux all'
       usage: gtfoblookup.py linux all [-h] [-f] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -l list, --list list
              list all types/categories/executables featured in the local copy of GTFOBins

OPTIONS 'gtfoblookup.py windows'
       usage: gtfoblookup.py windows [-h] [-l list]
                                       {ads,awl,comp,copy,creds,decode,download,dump,encode,exec,recon,uac,upload,all}
                                       ...

   Sub-commands
       gtfoblookup.py windows ads
              search the 'ADS' category of LOLBAS

       gtfoblookup.py windows awl
              search the 'AWL Bypass' category of LOLBAS

       gtfoblookup.py windows comp
              search the 'Compile' category of LOLBAS

       gtfoblookup.py windows copy
              search the 'Copy' category of LOLBAS

       gtfoblookup.py windows creds
              search the 'Credentials' category of LOLBAS

       gtfoblookup.py windows decode
              search the 'Decode' category of LOLBAS

       gtfoblookup.py windows download
              search the 'Download' category of LOLBAS

       gtfoblookup.py windows dump
              search the 'Dump' category of LOLBAS

       gtfoblookup.py windows encode
              search the 'Encode' category of LOLBAS

       gtfoblookup.py windows exec
              search the 'Execute' category of LOLBAS

       gtfoblookup.py windows recon
              search the 'Reconnaissance' category of LOLBAS

       gtfoblookup.py windows uac
              search the 'UAC Bypass' category of LOLBAS

       gtfoblookup.py windows upload
              search the 'Upload' category of LOLBAS

       gtfoblookup.py windows all
              search all categories of LOLBAS

OPTIONS 'gtfoblookup.py windows ads'
       usage: gtfoblookup.py windows ads [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows awl'
       usage: gtfoblookup.py windows awl [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows comp'
       usage: gtfoblookup.py windows comp [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows copy'
       usage: gtfoblookup.py windows copy [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows creds'
       usage: gtfoblookup.py windows creds [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows decode'
       usage: gtfoblookup.py windows decode [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows download'
       usage: gtfoblookup.py windows download [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows dump'
       usage: gtfoblookup.py windows dump [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows encode'
       usage: gtfoblookup.py windows encode [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows exec'
       usage: gtfoblookup.py windows exec [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows recon'
       usage: gtfoblookup.py windows recon [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows uac'
       usage: gtfoblookup.py windows uac [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows upload'
       usage: gtfoblookup.py windows upload [-h] [-f] [-t type] executable

       executable
              the executable to search for

       -f, --file
              use a file containing a list of executables (one per line) instead of a single
              executable

       -t type, --type type
              search for a specific type of executable

OPTIONS 'gtfoblookup.py windows all'
       usage: gtfoblookup.py windows all [-h] [-f] [-t type] executable

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
