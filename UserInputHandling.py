'''try:
    marks= int(raw_input('Enter the marks:'))
except Exception as e:
    print "Enter valid marks"
    print e.message
'''
# Other way around this
counter=1
while counter: #Looping statement
    try:    # Exception handler
        marks = int(raw_input('Enter the marks:'))
        print "You have entered %dx" %(marks)
        counter=0
    except Exception as e: #Catch the exception.
        print e.message
