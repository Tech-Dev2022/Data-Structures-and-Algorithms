"""
    File: timing1.py
    Prints the running times for problem sizses that double using a single loop
"""

import time

problemSize = 10000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()
    # The start of the algorithm 
    work = 1
    for i in range(problemSize):
        work += 1
        work -= 1
    # The end of the algorithm 
    elapsed = time.time() - start
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
    
    
"""
    The idea of the algorithm is quite simple, perform some work function (i.e., counting up and down from 1 to 2 back to 1) inside a nested loop
    a given number of times (the problem size of 1000000). Once this is done calcualted the time elapsed as the difference between the elapsed time
    and the start time. 
    
    Double the problem size and repeat the process 5 more times
"""
