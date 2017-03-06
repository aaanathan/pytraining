result='''
    This is sample
    of multiline output
    asdf
    asdfas
    df
    asdfa
    sdf
    asfd
    asdf
    as
    fd
'''
print result
print "sample"
print type(result)
lines = result.split("\n")
name = "arockia"

print "My name is " + name +" and I am living in " + str(2017)
print "My name is %s and I am living in %d and test %f" %(name,2017,10.15)