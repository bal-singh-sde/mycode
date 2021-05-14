#!/usr/bin/env python3

import os

for root, dirs, files in os.walk("/home/student/mycode"):
    print("Root:", root)
    print("Files:", files)



