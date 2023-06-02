'''
format: Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone.
Your task is to print the absolute difference (in seconds) between them.

Sample Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output:
25200
88200

Explanation:
In the first query, when we compare the time in UTC for both the time stamps,
we see a difference of 7 hours. which is 7*3600 seconds or 25200 seconds.
Similarly, in the second query, time difference is 5 hours and 30 minutes for
time zone adjusting for that we have a difference of 1 day and 30 minutes. Or
24*3600 + 30*60 = 88200


'''

import math
import os
import random
import re
import sys

def time_delta(t1, t2):
    "Write your logic here."

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
