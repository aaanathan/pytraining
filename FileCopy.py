import os
fname = "/home/aaanathan/PythonDevEnv/pytraining/test1.txt"
dname = "/home/aaanathan/PythonDevEnv/pytraining/test.txt"

with open(fname,'rb') as f:
    f.seek(0)
    content = f.read(1024)
    print content
    with open(dname,'wb') as d:
        d.writelines(content)
        os.remove(fname)