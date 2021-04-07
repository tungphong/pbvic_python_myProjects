import os
import sys

import stat
import time
import datetime

### Funs
def windows_print_folder(inputpath, files_folders):
    open_file = open('C:\\tungphong\\pbvic_python\\pbvic_work_proj\\folder_file\\test_folder\\test.txt', 'w')
    open_file.write("####################################################\n")
    open_file.write("#       Directory List For <directory_name>        #\n")
    open_file.write("####################################################\n")

    for fileOrfolder in files_folders:
        if os.path.isfile(inputpath+"\\"+str(fileOrfolder)):
            open_file.write(f"File name: {fileOrfolder}\n")
        else:
            open_file.write(f"<DIR>   {fileOrfolder}\n")
        fileStatsObj = os.stat(inputpath+"\\"+str(fileOrfolder))
        modificationTime = time.ctime(fileStatsObj[stat.ST_MTIME])
        open_file.write(f"    Last Modified Time :  {modificationTime}\n")
        open_file.write("----------------------------------------------\n")
    open_file.close()
def MacNLinux_print_folder(inputpath, files_folders):
    for fileOrfolder in files_folders:
        if os.path.isfile(inputpath+"\\"+str(fileOrfolder)):
            print(f"File name: {fileOrfolder}\n")
        else:
            print(f"<DIR>   {fileOrfolder}\n")
        fileStatsObj = os.stat(inputpath+"\\"+str(fileOrfolder))
        modificationTime = time.ctime(fileStatsObj[stat.ST_MTIME])
        print(f"    Last Modified Time :  {modificationTime}\n")
        print("----------------------------------------------\n")

###---------------------------------------------------
inputpath = input("Please enter your folder with full path: \n")
print(f'Your enter: {inputpath}')
files_folders = os.listdir(inputpath)
print(files_folders)

## Check OS system
os_check = sys.platform
print(os_check)


if os_check == 'linux' or os_check == 'linux2':
    ## Check files in Linux system
    print(os_check)
    MacNLinux_print_folder(inputpath, files_folders)
elif os_check == "darwin":
    ## Check files in Mac system
    print(os_check)
    MacNLinux_print_folder(inputpath, files_folders)
elif os_check == "win32":
    ## Check files in widow system
    print(os_check)
    windows_print_folder(inputpath, files_folders)
elif os_check == "win64":
    ## Check files in widow system
    print(os_check)
    windows_print_folder(inputpath, files_folders)

