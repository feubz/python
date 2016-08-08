from sys import argv
from os.path import exists
import subprocess
import getpass

whoami = getpass.getuser()
script, infile, outfile = argv
print('Hello {}, we are going to copy data from {} to {}'.format(whoami,infile,outfile))

#open the file and read the content
in_data = open(infile).read()

#verify that the output file exist
print('Does the output file {} exist? {}'.format(outfile,exists(outfile)))


#open the output file with write right and truncate
out_file = open(outfile, 'r+')
#write the data into the output file
out_file.write(in_data)

#Display the file content
print(out_file.read())

#print('The file contain the following line : \n {}').format(output)

#display the output file
out_file.close()



