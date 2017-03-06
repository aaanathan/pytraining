import time
import math
i=0
t1 = time.time()
print t1
while i<5:
    print "%d and wait for 2s" %(i)
    time.sleep(1)
    i += 1
t2 = time.time()

diff = t2-t1

print diff