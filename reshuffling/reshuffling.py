import os
from pathlib import Path
from random import shuffle


def reshuffling_sse(path, initial_file):
	"""path should be in C:/.../folder/ format
	filename should conform blabla.sse"""
	list_for_shuffle = [x for x in range(10245)]
	shuffle(list_for_shuffle)
	fragmented_file = []
	with open(os.path.join(path+initial_file)) as sse:
		lines = sse.readlines()
		for line in lines:
			if line.startswith('\\0\\'):
				line = line[3:-4]
				list_for_reindex_ = list(line)
				line = '\\0\\'
				for i in list_for_shuffle:
					line += list_for_reindex_[i]
				line += '\\0\\\n'
				fragmented_file.append(line)
			else:
				fragmented_file.append(line)
                
    # creation of file for the reshuffled alignment            
	Path(os.path.join(path+"reshuffled_for_scan.sse")).touch()
	with open(os.path.join(path+"reshuffled_for_scan.sse"), "a") as sse:
		for i in fragmented_file:
			sse.write(i)

def removing_file(path, file_name):
	try:
		os.remove(os.path.join(path+file_name))
	except:
		print("Nothing to remove")
