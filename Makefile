###################################################################
#                                  Makefile                       #
###################################################################
python3=/usr/bin/python3
pythonCmdFlags=-c

kmeans1: Assign3.py
	python3 $< data1.txt 2 kmeans

average1: Assign3.py
	python3 $< data1.txt 2 average

kmeans2: Assign3.py
	python3 $< data2.txt 2 kmeans

average2: Assign3.py
	python3 $< data2.txt 2 average

kmeans3: Assign3.py
	python3 $< data3.txt 2 kmeans

average3: Assign3.py
	python3 $< data3.txt 2 average

kmeans4: Assign3.py
	python3 $< data4.txt 3 kmeans

average4: Assign3.py
	python3 $< data4.txt 3 average