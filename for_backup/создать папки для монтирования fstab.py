#! /usr/bin/python3


import os, os.path
import sys  # for exiting from program
#import shutils  # for removing directories with all it's folders


def create_folder(folder):
	"""Creates passed to it folder if it's absent,
	if it's present - asks user, what to do.
	"""
	print('')
	
	if os.path.exists(folder) and (os.listdir(folder) != []):
		print('Folder {0} already exists.'.format(folder))
		print('Remove it and create an empty one?')
		print("L - view the list of files in it, Y - yes, N - don't remove and pass, Q - quit.")
		
		while True:  # needs for case, when user wrote wrong symbol
			inp = input()
			
			if inp == 'Y':
				recursively_remove_folder(folder)
				os.makedirs(folder)
				print('Folder "{0}" was successfully created'.format(folder))
				break
			elif inp == 'N':
				print("Passing, we didn't remove '{0}' directory".format(folder))
				break
			elif inp == 'L':
				files_list = os.listdir(folder)
				if files_list == []:
					print('Directory contains no files.')
				else:
					print('Directory "{0}" contains next files:'.format(folder))
					for i in os.listdir(folder):
						print(i)
				print('What will we do with it?')
			elif inp == 'Q':
				sys.exit()
			else:
				print('Command not found. Please, try again.')
				continue
	
	elif os.path.exists(folder):
		print('Folder is already present and is empty. All is well. ({0})'.format(folder))
	else:
		os.makedirs(folder)
		print('Folder was successfully created. ({0})'.format(folder))




def recursively_remove_folder(item):
	if os.path.isdir(item):
		for i in os.listdir(item):
			recursively_remove_folder(os.path.join(item, i))
		os.rmdir(item)
	else:
		os.remove(item)




print('Program loaded.')
print('Now we will create all needed folders.')

create_folder('/home/vlad/Видео')
create_folder('/home/vlad/Документы')
create_folder('/home/vlad/Загрузки')
create_folder('/home/vlad/Изображения')
create_folder('/home/vlad/Музыка')
create_folder('/home/vlad/Шаблоны')
create_folder('/home/vlad/Рабочий стол')

create_folder('/home/vlad/.fonts')
create_folder('/home/vlad/.themes')
create_folder('/home/vlad/.icons')

create_folder('/home/vlad/for_Programs')
create_folder('/home/vlad/Programs')
create_folder('/home/vlad/lmms')
create_folder('/home/vlad/makehuman')
create_folder('/home/vlad/.mozilla')
create_folder('/home/vlad/.thunderbird')
create_folder('/home/vlad/.moonchild productions')
create_folder('/home/vlad/.Skype')
create_folder('/home/vlad/.ssh')

create_folder('/home/vlad/.config/blender')
create_folder('/home/vlad/.config/hexchat')
create_folder('/home/vlad/.config/Slack')
create_folder('/home/vlad/.config/supertuxkart')
create_folder('/home/vlad/.config/transmission')


print('')
while True:
	if os.path.exists('/media/vlad/Storm'):
		if os.path.ismount('/media/vlad/Storm'):
			print("Before we will create /media/vlad/Storm, please unmount it.")
			input("Press any key to try again.")
			continue
		break
	else:
		break
create_folder('/media/vlad/Storm')
