input = "1,2,3,4,5"

print type(input.split(","))
print type(tuple(input.split(",")))

values = ['', '', '', '', '', '', '', '1', '', '2', '', '3', '', '4', '', '5']

j=0
for i in values:
    if i == "":
        values.pop(j)
    j += 1
print values