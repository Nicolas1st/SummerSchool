#!/bin/sh 

cp /var/log/kern.log $(lsblk -o MOUNTPOINT /dev/sda1 | grep /media)
