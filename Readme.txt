Author: Parteek Singh

COmmands Without makefile
===========================================================
Commands: python Assign3.py data1.txt 2 kmeans
commands: python Assign3.py data1.txt 2 average

Commands With makefile:
==========================================================
Commands:make kmeans<number of data set>
commands:make kmeans<number of data set>
Example:
command: make kmeans1

Language: Python 
version : 3.4

Dependencies:
===================================
from random import randint
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import timeit
import re
=====================================

Assumption:
All the data set is seprated by single space

Bonus:
I have done for 2 dimensional and 3 dimensional scatter plot