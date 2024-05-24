#!/usr/bin/env python3

import sys

# Author: Nikhil Tandukar
# Author ID: Tnikhil
# Date Created: 2024/05/24

if len(sys.argv) > 1 :
    timer = int(sys.argv[1])
else:
    timer = 3

while timer >= 1:
    print(timer)
    timer -= 1

print("blast off!")                        
