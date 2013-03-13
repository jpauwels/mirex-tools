#!/bin/bash

for year in 2010 2011 2012;
do
	../convert_json_labels_to_lab.py mirex-dataset.lst $year/outputs-js $year/outputs-lab;
	../convert_json_labels_to_lab.py rwcpop-dataset.lst $year/outputs-js $year/outputs-lab;
done

for year in 2012;
do
	../convert_json_labels_to_lab.py rwcpop-dataset.lst $year/outputs-js-rwc $year/outputs-lab-rwc;
	mv $year/outputs-lab-rwc/Ground-truth/* $year/outputs-lab/Ground-truth-RWC;
	rm -rf $year/outputs-lab-rwc;
	../convert_json_labels_to_lab.py salami-dataset.lst $year/outputs-js $year/outputs-lab;
done