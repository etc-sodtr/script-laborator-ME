#!/usr/bin/env python

import glob
import csv

sum = 0.0
ora =9.30
counter =0 #grupez prin acesta cate 12 fisiere pentru o mediere
 
for filename in sorted(glob.glob('*.lvm')) :
	#print "numele fisierului :" + filename +" "+ str(counter + 1)
	counter +=1
	#my_file.write("\n" + str(filename) + "\n")
	with open(filename) as csv_file:
		buffer = []
		rec = csv_file.readlines()
		count =0
		for line in rec :
			count +=1
			if count == 25: #informatia relevanta se afla pe randul 25 din fisier
				line.split()
  				field = line.split('	', 9)# separatorul este format dintr-un "tab"
    				term2 = field[8] # informatia relevanta este in al 9-lea cuvant din rand (dupa al 8-lea separator)
				#print term2
				if counter % 12 !=0:
					sum += float(term2)

				else:
					sum += float(term2)
					average = sum/12
					sum = 0
					print "media pentru ora %.2f este : %.4f \n" %((ora + counter/12), average)
	

if counter%12 != 0:
	print "Atentie ! Ultima oara media nu s-a calculat pentru 12 fisiere! \n"

