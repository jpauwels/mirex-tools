#!/usr/bin/env python

# Script to convert a directory of js-files coming from NEMA to the corresponding 
# lab-files. It should be called from the command line with the following parameters:
# 
# <list>		a plain text file containing the base names (without extension)
# 				of the files to convert, separated by newlines
# <js_dir>		the directory with the js-files
# <lab_dir>		the directory in which the resulting lab-files should be saved
# 
# Author: Johan Pauwels (johan.pauwels@gmail.com)
# Last changed: 2010-08-08
# License: GPL
# 
# Made for Python 2.6

import json
import re
import os
import sys
import os.path

def convert_json_file_to_lab_files(base_name, js_dir, lab_dir):
	"""Convert NEMA js-file to lab-files

	Converts the file <base_name>.js located in <js_dir> to a set of
	lab-files in <lab_dir>. For each of the data series present in 
	the js-file, a subdirectory will be created. The resulting lab-files
	are thus written to <lab_dir>/<series_name>/<base_name>.lab, 
	e.g. /path/to/lab_dir/Ground-truth 0/transcriptionbeatmaz000000.lab

	"""

	# Read js-file and store into single-line string
	js_path = os.path.join(js_dir, base_name+'.js')
	with open(js_path) as js_file:
		js_content = js_file.read()
		js_content = js_content.replace('\n','')
		
		# Use regexp to isolate json
		data_exp = re.compile('var .*_data = ([^;]*);')
		names_exp = re.compile('var .*_seriesNames = ([^;]*);')
		data_match = data_exp.search(js_content)
		names_match = names_exp.search(js_content)
		names = names_match.group(1)		
		data = data_match.group(1)
		
		# Parse json
		n = json.loads(names)
		d = json.loads(data)

		# Write lab file for each series
		for j in range(len(n)):
			name_dir = os.path.join(lab_dir, n[j])
			if not os.path.exists(name_dir):
				os.makedirs(name_dir)
			lab_path = os.path.join(name_dir, base_name+'.lab')
			with open(lab_path, 'w') as lab_file:
				for k in range(len(d[j])):
					lab_file.write('{0}\n'.format(d[j][k]))


if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('Usage: ' + os.path.basename(sys.argv[0]) + ' list js_dir lab_dir')
		sys.exit()
		
	# Get paths from command line
	list_path = sys.argv[1]
	js_dir = sys.argv[2]
	lab_dir = sys.argv[3]
	
	# Open list
	with open(list_path) as list:
		for i in list:
			i = i.strip()
			# Convert every file in list
			print('Processing file ' + i)
			convert_json_file_to_lab_files(i, js_dir, lab_dir)