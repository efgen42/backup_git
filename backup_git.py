#!/usr/bin/python3
import os
from rotate import rotate

BACKUP_DIRECTORY = 'F:\\gitlab'
FTPS_PATH = ' '
USER = ' '
PASS = ' '
FTPS_STR = 'ftps://' + USER + ':' + PASS + '@' + FTPS_PATH + '/'

if not os.path.isdir(BACKUP_DIRECTORY):
        os.mkdir(BACKUP_DIRECTORY)
        print('CREATE BACKUP DIR')

#print('FTPS_STR =' , FTPS_STR)
os.chdir(BACKUP_DIRECTORY)

print("\nНачало скачивания архивов\n")

os.system(f'"C:\Install\script\\wget.exe" -m --no-check-certificate -rnd {FTPS_STR}')

print("\nОкончание скачивания архивов\n")

#print(os.system('ls'))

rotate()