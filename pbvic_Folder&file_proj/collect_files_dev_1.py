import os
import sys

import stat
import time
import datetime

#check owner
import win32api
import win32con
import win32security

### Funs
def windows_print_folder(inputpath, files_folders):
    print("####################################################\n")
    print("#       Directory List For <directory_name>        #\n")
    print("####################################################\n")
    filesdic = {}
    for fileOrfolder in files_folders:
        if os.path.isfile(inputpath + "\\" + str(fileOrfolder)):
            sd = win32security.GetFileSecurity(inputpath + "\\" + str(fileOrfolder),
                                               win32security.OWNER_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorOwner()
            name, domain, type = win32security.LookupAccountSid(None, owner_sid)
            append_value(filesdic, fileOrfolder, "file")
            append_value(filesdic, fileOrfolder, domain)
            append_value(filesdic, fileOrfolder, name)
        else:
            append_value(filesdic, fileOrfolder, "dir")

        fileStatsObj = os.stat(inputpath + "\\" + str(fileOrfolder))
        modificationTime = time.ctime(fileStatsObj[stat.ST_MTIME])
        append_value(filesdic, fileOrfolder, modificationTime)

    print(filesdic)
    print("---------------------------------------------------\n")
    for key, values in filesdic.items():
        for v in values:
            if v == 'file':
                print("File Name: ", key)
            elif v == 'dir':
                print("Directory Name: ", key)
            else:
                print(" ",v)


        
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

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value

def no_of_argu(*args):
    # using len() method in args to count
    return (len(args))
###---------------------------------------------------

###=============main func=====================
def main():
    # Count the arguments
    arguments = len(sys.argv) - 1
    print("Number argument: ", arguments)

    inputpath = sys.argv[arguments]
    ## Check the folder exist or not, and then printout
    if arguments == 1:
        #os.path.exists(inputpath):
        #print(inputpath)

        ## Check OS system
        os_check = sys.platform
        #print(os_check)
        files_folders = os.listdir(inputpath)

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
    elif arguments < 1:
        ## Check OS system
        os_check = sys.platform
        print(os_check)

        if os_check == 'linux' or os_check == 'linux2':
            ## Check files in widow system
            print("No argument was provide - default of /temp will be used!\n")
            inputpath = "/temp"
            files_folders = os.listdir(inputpath)

            MacNLinux_print_folder(inputpath, files_folders)
        elif os_check == "darwin":
            ## Check files in widow system
            print("No argument was provide - default of /temp will be used!\n")
            inputpath = "/temp"
            files_folders = os.listdir(inputpath)

            MacNLinux_print_folder(inputpath, files_folders)
        elif os_check == "win32":
            ## Check files in widow system
            print("No argument was provided - default of c:\\temp will be used!\n")
            inputpath = "C:\\tmp"
            files_folders = os.listdir(inputpath)
            windows_print_folder(inputpath, files_folders)

        elif os_check == "win64":
            ## Check files in widow system
            print("No argument was provide - default of c:\\temp will be used!\n")
            inputpath = "c:\\temp"
            files_folders = os.listdir(inputpath)
            windows_print_folder(inputpath, files_folders)

if __name__=="__main__":
    main()
else:
    exit()
