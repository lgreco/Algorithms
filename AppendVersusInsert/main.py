#
# LUC COMP 363 002 F20
#
# A quick script to test performance of list append versus insert
#

import time             # Package with access to coc
testUpTo = 250000       # max size of list to test.
                        # Start with a value of 250,000 or
                        # less to avoid overtaxing your computer.
                        #
                        # On a nicely equipped MacBook Pro with a
                        # quad-core i5 and 16 GB of RAM, the following
                        # times were observed:
                        #
                        #             n          total time
                        #       262,144          21 seconds
                        #       524,288          81 seconds
                        #     1,048,576         357 seconds
                        #     2,097,152       1,498 seconds
                        #     4,194,304       6,113 seconds ( ~ 2 hrs)
                        #     8,388,608      23,801 seconds ( ~ 8 hrs)

# Function to test appending data to a list;
# It initializes a list, and appends numbers 1 through n
def testAppend(n):
    nums = []
    for i in range(n):
        nums.append(i)
    nums.reverse()


# Function to test inserting data to a list;
# It initializes a list, and inserts numbers 1 through n
# at the 0-th position of the list.
def testInsert(n):
    nums = []
    for i in range(n):
        nums.insert(0, i)

#
# main program
# Runs tests for n= 2, 4, 8, ..., <= testUpTo

n = 2     # initial value for n

# Output header
print("         n                 Append                   Insert")
print("                           time                     time")
print("----------                 --------                 --------")

# Main loop runs tests, then doubles the value of n.
while n < testUpTo:
    startTime = time.time()
    testAppend(n)
    appendTime = time.time() - startTime

    startTime = time.time()
    testInsert(n)
    insertTime = time.time() - startTime

    print(f'{n:10d}{appendTime:25f}{insertTime:25f}')

    n = n * 2

print()