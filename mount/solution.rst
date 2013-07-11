Objective of Assignment
=======================
The assignment was to write a python program that execute the same output as we type mount command in the terminal.

The python program can be executed by using:-

::

    $ python mount.py

or

::

    $ chmod +x mount.py
    $ ./mount.py

The coded program is given at the `link <https://github.com/shaliniroy/repo/blob/master/mount/mount.py>`_

Explanation of the code
-----------------------

::

    f = open("/proc/mounts")

    This line open the file /proc/mounts

     
    for x in f:
    
    This line iterate through each line.


    print x,

    This line print the file.      


    f.close()

    This line close the opened file.
