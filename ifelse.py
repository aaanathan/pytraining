try:
    a = int(raw_input("Enter your marks:"))
    
    if a > 0:
        if a>=90:
            print"a is A GRADE"
        elif a>=80 and a<90:
                print"a is B grade"
        elif a>=70 and a<80:
            print"a is C grade"
        elif a>=60 and a<70:
            print"a is D grade"
        else:
            print"fail"   
    else:
        print "Please enter valid marks"
except:
    print "Please enter number only"

if a>0:
    if a>=60 and a<70:
        print "D"
    else:
        if a>=70 and a<80:
            print "C"
        else:
            if a>=80 and a<90:
                print "B"
            else:
                if a>=90:
                    print "A"
else:
    print "Please enter valid number"
