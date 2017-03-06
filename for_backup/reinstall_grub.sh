#! /bin/bash

sudo mount /dev/sdh1 /mnt
sudo mount --bind /dev /mnt/dev 
sudo mount --bind /dev/pts /mnt/dev/pts 
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys

sudo chroot /mnt

grub-install /dev/sdh
update-grub
