# GTFOBLookup
Offline command line lookup utility for [GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io).

## Installation/Setup
To install GTFOBLookup, git clone the repository to your machine and run the following command:
<pre>
gtfoblookup.py update
</pre>

## usage
<pre>
gtfoblookup.py [-h]
    {update,purge,shell,cmd,rev,nrev,bind,nbind,upload,download,write,read,load,suid,sudo,cap,lsuid,all}...

Offline command line lookup utility for GTFOBins (https://gtfobins.github.io/)

positional arguments:
  {update,purge,shell,cmd,rev,nrev,bind,nbind,upload,download,write,read,load,suid,sudo,cap,lsuid,all}
    update              update local copy of GTFOBins
    purge               remove local copy of GTFOBins
    shell               search the 'shell' category of GTFOBins
    cmd                 search the 'command' category of GTFOBins
    rev                 search the 'reverse-shell' category of GTFOBins
    nrev                search the 'non-interactive-reverse-shell' category of
                        GTFOBins
    bind                search the 'bind-shell' category of GTFOBins
    nbind               search the 'non-interactive-bind-shell' category of
                        GTFOBins
    upload              search the 'file-upload' category of GTFOBins
    download            search the 'file-download' category of GTFOBins
    write               search the 'file-write' category of GTFOBins
    read                search the 'file-read' category of GTFOBins
    load                search the 'library-load' category of GTFOBins
    suid                search the 'suid' category of GTFOBins
    sudo                search the 'sudo' category of GTFOBins
    cap                 search the 'capabilities' category of GTFOBins
    lsuid               search the 'limited-suid' category of GTFOBins
    all                 search all categories of GTFOBins

optional arguments:
  -h, --help            show this help message and exit
</pre>
Each GTFOBins category can be searched using the following syntax:
<pre>
gtfoblookup.py &lt;category&gt; [-h] [-f] binary

positional arguments:
  binary      the binary to search for

optional arguments:
  -h, --help  show this help message and exit
  -f, --file  use a file containing a list of binaries (one per line) instead
              of a single binary
</pre>
