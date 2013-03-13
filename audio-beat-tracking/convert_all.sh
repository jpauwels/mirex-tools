#!/bin/bash

for year in 2010 2011 2012;
do
	../convert_json_instants_to_lab.py maz-dataset.lst $year/outputs-js $year/outputs-lab;
	../convert_json_instants_to_lab.py mck-dataset.lst $year/outputs-js $year/outputs-lab;
done

for year in 2012;
do
	../convert_json_instants_to_lab.py smc-dataset.lst $year/outputs-js $year/outputs-lab;
done