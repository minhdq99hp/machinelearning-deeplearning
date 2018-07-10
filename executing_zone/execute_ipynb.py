#!/usr/bin/env python
"""
@minhdq99hp
"""

import os
import sys
import time

if len(sys.argv) < 2:
	print("You must pass a notebook argument to convert !")
	sys.exit(-1)

start = time.time()

nb_name = sys.argv[1]

os.system("jupyter nbconvert --to notebook --execute %s --ExecutePreprocessor.timeout=-1" %nb_name)

end = time.time()

print("Converted in %f seconds."%(end - start))