import os
import time

sys_slash = '/' # The slash used for your system's paths

def look_for_files(typeformat="",path_str="",prefix=""):
    return_table = []
    empty_format = True if len(typeformat) < 1 else False  
    path_str = prefix+path_str
    
    if os.path.exists(path_str):
        for file in os.listdir(path_str):
            i_file = path_str+sys_slash+file
            if os.path.isfile(i_file):
                
                if empty_format:
                    return_table.append(i_file)
                elif not empty_format and file.endswith(typeformat):
                    return_table.append(i_file)
                    
    return return_table
                
                
def get_custom(prefix,i):
    return prefix.replace("%i%",str(i))

path_str = ""

while(path_str != "exit"):

    path_str = input("\nEnter path or exit to exit the script:")
    path_format = ""
    path_format = input("\nEnter format (txt,obj,etc) || Not typing anything will print all filetypes: ")
    custom_prefix = input("\nEnter prefix before filename (Use %i% for the item number) || Not typing anything will use item[count] = filename: ")
    
    if os.path.exists(path_str):
        print("\nPath does exist!\n")

        file_table = []
        for directory in os.walk(path_str):
            if os.path.isdir(directory[0]):
                for file in look_for_files(path_format,directory[0]):
                    file_table.append(file)
                    
        print("\nTotal items = " + str(len(file_table)))
        
        if len(custom_prefix) < 1:
            custom_prefix = "item[%i%] = "
            
        input("Press ENTER to print")
        
        for i in range(0,len(file_table)):
            print(get_custom(custom_prefix,i) + file_table[i])
    else:
        print("\nPath doesn't exist!\n")
