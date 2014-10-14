'''
Created on Oct 14, 2014

@author: guoc
'''
import os
import mimetypes

def file_len(fname):
    with open(fname) as f:
        count = 0;
        for line in f:
            count += 1
    return count

def get_files(input_dir):
    files = os.listdir(input_dir)
    found_files = []
    for item in files:
        # convert to relative path
        item = os.path.join(input_dir, item)
        if os.path.isdir(item):
            found_files += get_files(item)
        elif os.path.isfile(item):
            filepath = os.path.normpath(item)
            found_files.append(filepath)

    return found_files

if __name__ == "__main__":
    #file_count("D:\\projects_ignite\\eclipse_python_2.7\\nova")
    files = get_files(".")
    for f in files:
        file_type = mimetypes.guess_type(f)
        if file_type[0] == 'text/plain':
            output = f + "-" + str(file_len(f))
        else:
            output = f + "-" + str(file_type[0]) 
        print(output)     