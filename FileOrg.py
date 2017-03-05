import sys,os,collections
list_ftypes=[]

directory_location=raw_input("Enter the location")
if not directory_location.endswith("/"):
    directory_location += "/"
for i in os.walk(directory_location):
    for f in i[-1]:
        list_ftypes.append(str(f).split(".")[-1])

print list(set(sorted(list_ftypes)))

for d in list(set(sorted(list_ftypes))) :
    print directory_location+"files-"+d
    os.makedirs(directory_location+"files-"+d)

for i in os.walk(directory_location):
    for j in i[-1]:
        fname = i[0]+j
        print fname
        # Read the file with rb mode by passing fname and store it in a variable
        # find the extension and prepare the target path
        # Create the file in the location based on the extension

# satish.polumati@gmail.com
# Send Ebook and this file source.