import sys
import os
import hashlib

hash_list = []
search_for_directory = "SearchFor"
search_in_directory = "SearchIn"

def dir_listing():
	print "Finding the directory"
	#directory = raw_input("Enter The Directory you wish to be hashed : ")

	"""
	Create hash list
	"""
	for fn in os.listdir(search_for_directory):
			file_name = os.path.join(search_for_directory,fn)
			#print file_name
			hasher = hashlib.md5()
			with open(file_name, 'rb') as afile:
    				buf = afile.read()
    				hasher.update(buf)
				hex_hash = (hasher.hexdigest())
				hash_list.append(hex_hash)
	print hash_list

	"""
	Search for file hashes in hash list
	"""
	match_count = 0
	file_count = 0
	for fn in os.listdir(search_in_directory):
			file_name = os.path.join(search_in_directory,fn)
			print file_name
			hasher = hashlib.md5()
			with open(file_name, 'rb') as afile:
    				buf = afile.read()
    				hasher.update(buf)
				hex_hash = (hasher.hexdigest())
			if hex_hash in hash_list:
				match_count = match_count + 1
			file_count = file_count + 1
	print "There were", match_count, "files matching, out of", file_count, "files"
	
dir_listing()
