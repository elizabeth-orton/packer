import packer as p
import os
#get command line arguments into list
args = p.parse()
directory = args.directory
print(args)
#get the files from the directory into a list
files = os.listdir(directory)
#make an output directory for the files to go into
bigdir = os.path.join(directory, args.output)
try:
    os.mkdir(bigdir)
except:
    pass
cwd = os.getcwd()
#this is where the fun happens
for f in files:
    os.chdir(cwd + "/" + directory)
    try:
        read_data = p.opendata(os.path.join(cwd, directory, f)) #get the contents of the file
        newdir = os.path.join(cwd, directory, args.output, str(f)[:-3]) #this makes the path to the new directory
        try:
            os.mkdir(newdir) #make new directory, if it already exists just pass this
        except:
            pass
        os.chdir(newdir) #move into the new directory
        i = 1
        al1 = os.path.join(os.getcwd(), "algo1")
        try:
            os.mkdir(al1)
        except:
            pass
        os.chdir(al1)
        while i < 11: #make ten files
            filename = str(f)[:-3] + "algo1key" + str(i) + ".py"
            cipher = p.addwrite(read_data, i + 1, filename)
            p.restwrite(filename, cipher, i+1)
            i+=1
        i = 1
        os.chdir(newdir)
        al2 = os.path.join(os.getcwd(), "algo2")
        try:
            os.mkdir(al2)
        except:
            pass
        os.chdir(al2)
        while i < 11:
            filename = str(f)[:-3] + "algo2key" + str(i) + ".py"
            cipher = p.xwrite(read_data, i + 1, filename)
            p.restwrite(filename, cipher, i+1)
            i+=1
    except: #this will happen if it tries to run a directory
        pass


