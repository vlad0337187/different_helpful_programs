#! /usr/bin/python3


import os
import shutil


def copy_file(source, target):
	shutil.copy2(source, target, follow_symlinks=True)
	print("File successfully copied. < {0} >".format(source))




# для бэкапа и восстановления системы
copy_file("/media/vlad/Storm/Backup/linux/разные файлы/reinstall_grub.sh", "/home/vlad/Programs/my_projects/different_helpful_programs/for_backup")
copy_file("/media/vlad/Storm/Backup/linux/разные файлы/важные данные.txt", "/home/vlad/Programs/my_projects/different_helpful_programs/for_backup")
copy_file("/media/vlad/Storm/Backup/linux/разные файлы/добавить записи в fstab.py", "/home/vlad/Programs/my_projects/different_helpful_programs/for_backup")
copy_file("/media/vlad/Storm/Backup/linux/разные файлы/создать папки для монтирования fstab.py", "/home/vlad/Programs/my_projects/different_helpful_programs/for_backup")
copy_file("/media/vlad/Storm/Backup/linux/разные файлы/создать символические сслыки.py", "/home/vlad/Programs/my_projects/different_helpful_programs/for_backup")
copy_file("/media/vlad/Storm/Backup/linux/разные файлы/установить пакеты.py", "/home/vlad/Programs/my_projects/different_helpful_programs/for_backup")
