import packer as p
import os
#get command line arguments into list
args = p.parse()
directory = args.directory
print(args)
#get the files from the directory into a list
files = os.listdir(directory)
#make an output directory for the files to go into
os.mkdir(os.path.join(directory, args.output))
#this is where the fun happens
for f in files:
    read_data = p.opendata(os.path.join(directory, f))
    newdir = os.path.join(directory, args.output, f)
    print(newdir)
    os.mkdir(newdir)
    i = 1
    while i < 11:
        filename = os.path.join(newdir, str(i))
        #p.addwrite(read_data, i+1, os.path.join(newfile, "k"))


