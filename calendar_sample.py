import calendar

dob = 6
cal = calendar.month(2017,03)

print cal

w_days = cal.split("\n")[1].split(" ")
#print cal.split("\n")[2:]
for week in cal.split("\n")[2:]:
    final_week = week.split(" ")
    print "before"
    print final_week
    j = 0
    for i in final_week:
        if i == "":
            final_week.pop(j)
        j += 1
    print "AFter"
    print final_week
    print str(dob)
    if str(dob) in final_week:
        print final_week
        i=0
        for t in final_week:
            if str(dob) == t:
                position = i
                print position
            i += 1

print w_days[position]
