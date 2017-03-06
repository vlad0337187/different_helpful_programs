#! /usr/bin/python3


import os
import os.path
import sys  # for exit()
import shutil




def create_link(source, target):
	
	if os.path.exists(target):
		
		print("")
		
		if os.path.islink(target):
			if os.path.realpath(target) == source:
				print("Link already exists. All is well. ({0})".format(target))
				return
			its_type = "link"
		elif os.path.isdir(target):
			its_type = "folder"
		elif os.path.isfile(target):
			its_type = "file"
		
		print("Such address already exists, it's {1}. ({0})".format(target, its_type))
			
		while True:
			print("")
			print("What will we do?")
			print("O - overwrite it (remove and create a link), P - pass, don't do anything,")
			print("L - list of files (for directories only), Q - quit.")
			inp = input()
			if inp == "O":
				shutil.rmtree(target)
				os.symlink(source, target)
				print("Link created. (from {0} to {1})".format(source, target))
			elif inp == "P":
				break
			elif inp == "L":
				if not (its_type == "folder"):
					print("Given path is not a folder, cannot view list of it's files.")
				else:
					files_list = os.listdir(target)
					if files_list == []:
						print("There are no files in this directory.")
					else:
						print("Directory contains next files:")
						for i in files_list:
							print(i)
			elif inp == "Q":
				sys.exit()
	else:
		os.symlink(source, target)
		print("Link created. (from {0} to {1})".format(source, target))





create_link('/media/vlad/Storm/Backup/linux/home/.hgrc', '/home/vlad/.hgrc')

