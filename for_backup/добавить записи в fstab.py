#! /usr/bin/python3


import os
import sys  #for exiting


what_to_add = r"""


# Монтируем раздел Storm (для дальнейшего монтирования папок пользователя):
UUID=385AF63B5AF5F58A           /media/vlad/Storm         ntfs  defaults,uid=1000,gid=1000 0 1

# Монтируем папки пользователя из Debian в нашу ОС:
# Стандартные документы:
/media/vlad/Storm/Backup/linux/home/Видео                        /home/vlad/Видео                                    none             bind
/media/vlad/Storm/Backup/linux/home/Документы                    /home/vlad/Документы                                none             bind
/media/vlad/Storm/Backup/linux/home/Загрузки                     /home/vlad/Загрузки                                 none             bind
/media/vlad/Storm/Backup/linux/home/Изображения                  /home/vlad/Изображения                              none             bind
/media/vlad/Storm/Backup/linux/home/Музыка                       /home/vlad/Музыка                                   none             bind
/media/vlad/Storm/Backup/linux/home/Шаблоны                      /home/vlad/Шаблоны                                  none             bind
/media/vlad/Storm/Backup/linux/home/Рабочий\040стол              /home/vlad/Рабочий\040стол                          none             bind
# Технические:
/media/vlad/Storm/Backup/linux/home/.fonts                       /home/vlad/.fonts                                   none             bind
/media/vlad/Storm/Backup/linux/home/.themes                      /home/vlad/.themes                                  none             bind
/media/vlad/Storm/Backup/linux/home/.icons                       /home/vlad/.icons                                   none             bind
# Профили программ:
/media/vlad/Storm/Backup/linux/home/for_Programs                 /home/vlad/for_Programs                             none             bind
/media/vlad/Storm/Backup/linux/home/Programs                     /home/vlad/Programs                                 none             bind
/media/vlad/Storm/Backup/linux/home/lmms                         /home/vlad/lmms                                     none             bind
/media/vlad/Storm/Backup/linux/home/makehuman                    /home/vlad/makehuman                                none             bind
/media/vlad/Storm/Backup/linux/home/.mozilla                     /home/vlad/.mozilla                                 none             bind
/media/vlad/Storm/Backup/linux/home/.thunderbird                 /home/vlad/.thunderbird                             none             bind
/media/vlad/Storm/Backup/linux/home/.moonchild\040productions    /home/vlad/.moonchild\040productions                none             bind
/media/vlad/Storm/Backup/linux/home/.Skype                       /home/vlad/.Skype                                   none             bind
/media/vlad/Storm/Backup/linux/home/.ssh                         /home/vlad/.ssh                                     none             bind
# Конфигурации программ:
/media/vlad/Storm/Backup/linux/home/.config/blender              /home/vlad/.config/blender                          none             bind
/media/vlad/Storm/Backup/linux/home/.config/hexchat              /home/vlad/.config/hexchat                          none             bind
/media/vlad/Storm/Backup/linux/home/.config/Slack                /home/vlad/.config/Slack                            none             bind
/media/vlad/Storm/Backup/linux/home/.config/supertuxkart         /home/vlad/.config/supertuxkart                     none             bind
/media/vlad/Storm/Backup/linux/home/.config/transmission         /home/vlad/.config/transmission                     none             bind
"""


if os.geteuid() != 0:
	print('Please, run this program as superuser.')
	sys.exit()


with open('/etc/fstab', 'tr') as fstab_file:
	fstab_content = fstab_file.read()


# check for alerady containing it
if what_to_add.strip() in fstab_content:
	print("")
	print("Needed lines are already it /etc/fstab. Please, check it.")
	sys.exit()


#backup
with open( os.path.join(os.path.dirname(__file__), "backup_fstab"), "tw") as backup_file:
	backup_file.write(fstab_content)
	print("")
	print('We made backup of old fstab to', os.path.join(os.path.dirname(__file__), "backup_fstab"))


print("Needed lines are not in fstab yet. Let's add them.")
with open( "/etc/fstab", "tw") as fstab_file:
	fstab_file.write( fstab_content + what_to_add )
	print("")
	print("/etc/fstab was successfully written.")
