#!/usr/bin/env python
f = open("/proc/mounts")
for x in f:
    print x,
f.close()
