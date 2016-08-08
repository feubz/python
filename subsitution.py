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

#print in_data
print('Where are going to write the following string into the file: {}'.format(in_data))

#open the output file with write right and truncate
with open(outfile, 'r+') as out_file:
	out_file.truncate()
	out_file.write(in_data)
	out_file.seek(0)
	print(out_file.read())








