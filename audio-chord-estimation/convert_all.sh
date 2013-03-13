#!/bin/bash

for year in 2010 2011 2012;
do
	../convert_json_labels_to_lab.py mirex-dataset.lst $year/outputs-js $year/outputs-lab;
done

for year in 2012;
do
	../convert_json_labels_to_lab.py mcgill-dataset.lst $year/outputs-js $year/outputs-lab;
done