import os
fname = "/home/aaanathan/Documents/Python - introduction.pptx"
dname = "/home/aaanathan/PythonDevEnv/pytraining/Python - introduction.pptx"

with open(fname,'rb') as f:
    #f.seek(0)
    content = f.read()
    with open(dname,'wb') as d:
        d.writelines(content)
        #os.remove(fname)