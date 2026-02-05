import os

def print_value(L1D,  L1I, L2, filename, output_file, values):
	names = ["SimuTime", "L1D Hit","L1I Hit","L1D Miss","L1I Miss","L2 Hit","L2 Miss","RealTime"]
	retStr = f"\n------ for {filename} ------\n"
	# printng 
	retStr += f"{L1D}\tL1D\n"
	retStr += f"{L1I}\tL1I\n"
	retStr += f"{L2}\tL2\n"

	for name in names:
		retStr +=  f"{values[name]}\t{name}\n"
	retStr += "\n\n"
	with open(BASEDIR+output_file, "a+") as f:
		f.writelines(retStr)

	print(retStr)
	return 0

def next_value(full_str, start_string):
	
	ind = 0
	while ind < len(start_string) -1 and full_str[ind] == start_string[ind]:
		ind += 1
	while not full_str[ind].isnumeric():
		ind += 1
	endind = ind
	while full_str[endind].isnumeric() or '.' == full_str[endind]:
		endind +=1
	v = full_str[ind:endind+1]
	try :
		if '.' in v:
			return float(v)
		return int(v)
	except :
		print(f"Coulldn't pars the value {v} into a float or integer")

BASEDIR = "OutputStats/Cache/SRAD/"
output_file = "allCacheStat.txt"
def main(L1D,  L1I, L2, special = None):
	if special == None:
		filename = f"SRAD_L1D{L1D}K_L1I{L1I}K_L2{L2}K.txt"	
	else :
		filename = special
	content = None
	with open(BASEDIR+filename, "r+") as f :
		content = f.readlines()
		content = [i.strip("\n") for i in content]
	if content == None :
		print("Couldn't open file")
	index = content.index("---------- End Simulation Statistics   ----------")
	print(f"index of file {filename} is {index}")
	content = content[:index]

	lineTofind = {
		"board.cache_hierarchy.l1dcaches.overallHits::total" : "L1D Hit",
		"board.cache_hierarchy.l1dcaches.overallMisses::total" : "L1D Miss",
		"board.cache_hierarchy.l1icaches.overallHits::total" : "L1I Hit",
		"board.cache_hierarchy.l1icaches.overallMisses::total" : "L1I Miss",
		"board.cache_hierarchy.l2caches.overallHits::total" : "L2 Hit",
		"board.cache_hierarchy.l2caches.overallMisses::total" : "L2 Miss",
		"simSeconds" : "SimuTime",
		"hostSeconds" : "RealTime",
	}

	values = {}
	for line in content :
		for k in lineTofind.keys():
			if k in line :
				# then find the value
				v = next_value(line, k)
				values[lineTofind[k]] = v
	print_value(L1D,  L1I, L2, filename, output_file , values )


L1D = 128
L1I = 2
L2 = 64 

for i in range(1,4):
	main(L1D, L1I, L2)
	L2 *=2
# main(0, 0, 0, special = "LUD_0.txt")
#main(1, 2, 1, special = "HS_L1D1K_L1I2K_L21K.txt")
#main(1, 2, 1, special = "HS_L1D1K_L1I2K_L264K.txt")
#main(2, 2, 1, special = "HS_L1D2K_L1I2K_L264K.txt")
#main(4, 2, 1, special = "HS_L1D4K_L1I2K_L264K.txt")
#main(.512, 2, 1, special = "HS_L1D512_L1I2K_L21K.txt")
#main(5120000, 2, 1, special = "HS_L1D512M_L1I2K_L264K.txt")
#

"SRAD_L1D128K_L1I2K_L264K.txt"
"SRAD_L1D128K_L1I2K_L2128K.txt"
"SRAD_L1D128K_L1I2K_L2256K.txt"
#"SRAD_L1D16K_L1I2K_L264K.txt"
#"SRAD_L1D256K_L1I2K_L264K.txt"
#"SRAD_L1D2K_L1I2K_L264K.txt"
#"SRAD_L1D32K_L1I2K_L264K.txt"
#"SRAD_L1D4K_L1I2K_L264K.txt"
#"SRAD_L1D64K_L1I2K_L264K.txt"
#"SRAD_L1D8K_L1I2K_L264K.txt"
"SRAD_L1D32K_L1I32K_L2512K.txt"
