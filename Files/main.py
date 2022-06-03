__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# -----------------------------------

import os
import shutil

# Changing path of parent directory to current directory
cwd = os.chdir("/Users/yrmee/Desktop/Winc/files")
# Path's stored in variable
cache_folder_path = "cache"
zip_path = "data.zip"

# 1. Write a function called clean_cache.
    # clean_cache: takes no arguments and creates an empty folder named cache in the current directory. 
    # If it already exists, it deletes everything in the cache folder.
def clean_cache():
    if os.path.isdir(cache_folder_path):
        shutil.rmtree(cache_folder_path)
    os.mkdir(cache_folder_path)


# 2. Write a function called cache_zip.
    # cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order. 
    # The function then unpacks the indicated zip file into a clean cache folder.
    # You can test this with data.zip file.
def cache_zip(zip_path: str, cache_folder_path: str):
    clean_cache()
    shutil.unpack_archive(zip_path, cache_folder_path)



# 3. Write a function called cached_files.
    # cached_files: takes no arguments and returns a list of all the files in the cache. 
    # The file paths should be specified in absolute terms. 
    # Search the web for what this means! No folders should be included in the list. 
    # You do not have to account for files within folders within the cache directory.
def cached_files():
    list_of_files = []
    for folder, subs, files in os.walk(cache_folder_path):
        for filename in files:
            list_of_files.append(os.path.abspath(os.path.join(folder, filename)))
    return list_of_files



# 4. Write a function called find_password.
    # find_password: takes the list of file paths from cached_files as an argument. 
    # This function should read the text in each one to see if the password is in there. 
    # Surely there should be a word in there to indicate the presence of the password? 
    # Once found, find_password should return this password string.
def find_password(list_of_files):
    for file in list_of_files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "password" in line:
                    password = line.split(" ")[1]
                    return password.strip()


# See al files in current directory in a list
show_current_list = os.listdir()

if __name__ == "__main__":
    print('Get path current working directory :      ', os.getcwd())
    print('Get path current file name :    ', __file__)
    print(os.getcwd())
    print(show_current_list)
    clean_cache()
    cache_zip(zip_path, cache_folder_path)
    cached_files()
    #print(cached_files())
    print(find_password(cached_files()))