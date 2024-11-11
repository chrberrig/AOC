# Creates a folder, and a file for each day, as well as creating a text file for input for each day
import os
import argparse
import aocd

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", dest = "year", default = "2010", help="Current year")
parser.add_argument("-p", "--path", dest = "path", default = "/home/berrig/Documents/aoc", help="path to destination for directories")
args = parser.parse_args()

for idx in range(1, 26):
	day_dir = f'{args.path}/{args.year}/day{idx}'
	os.makedirs(daydir)
	if not os.path.exists(f'{daydir}/day{idx}.py'):
		f = open(f'{daydir}/day{idx}.py', 'w')
		f.write("import numpy as np\nimport aocd\n")
		f.write()
	
        try aocd.get_data(day=idx): 
		i = open(f'{daydir}/day{idx}input.txt', 'w')
		i.write(aocd.get_data(day=idx, year=args.year))
	except: 


