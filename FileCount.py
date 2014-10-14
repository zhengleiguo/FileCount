'''
Created on Oct 14, 2014

@author: guoc
'''
import os
import sys
import mimetypes
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--no-empty-lines", action = "store_true", dest = "ignore_empty", default = False, 
                  help="Count lines without empty lines")
parser.add_option("-c", "--no-comments", action = "store_true", dest="ignore_comment", default=False,
                  help="Don\'t count lines that have Cstyle or Pythonstyle comments.")
parser.add_option("-d", "--dir", action = "store", type = "string", dest="input_directory", 
                  help="Directory to count")
        
class FileCount:
    def __init__(self, ignore_comment, ignore_empty):
        self.found_files = []
        self.ignore_comment = ignore_comment;
        self.ignore_empty = ignore_empty;
    
    def file_len(self, fname):
        with open(fname) as f:
            count = 0;
            for line in f:
                count += 1
        return count
    
    def get_files(self, input_dir):
        files = os.listdir(input_dir)
        for item in files:
            # convert to relative path
            item = os.path.join(input_dir, item)
            if os.path.isdir(item):
                self.get_files(item)
            elif os.path.isfile(item):
                filepath = os.path.normpath(item)
                self.found_files.append(filepath)
    
    def count(self, input_dir):
        self.get_files(input_dir)
        for f in self.found_files:
            file_type = mimetypes.guess_type(f)
            if file_type[0] == 'text/plain':
                output = f + "-" + str(self.file_len(f))
            else:
                output = f + "-" + str(file_type[0]) 
            print(output)

def main():
    #file_count("D:\\projects_ignite\\eclipse_python_2.7\\nova")
    (options, args) = parser.parse_args(sys.argv[1:])
    #print args
    #print options
    if not options.input_directory:
        parser.error("-d option requires an argument!")
    else:
        fc = FileCount(options.ignore_comment, options.ignore_empty)
        fc.count(options.input_directory)
        pass        


if __name__ == "__main__":
    main()

   