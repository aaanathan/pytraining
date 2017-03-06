import sys
import os

if len(sys.argv)>1:
    uname = sys.argv[1]
    print uname
else:
    print """Procedure the run the script:

          Pass the directory name as an argument to this script.

          Please try again"""