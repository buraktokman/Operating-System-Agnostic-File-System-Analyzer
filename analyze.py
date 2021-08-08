#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name      : Ercument Burak Tokman
# Purpose   : CS350 Operating Systems Course Project
#			  Analyze file count, size and type information on Windows and FreeBSD operating systems
# Author	: Ercument Burak Tokman - S013090
# Created   : 30 March 2018
# Modified	: 1 June 2018
#-------------------------------------------------------------------------------
import os, sys
import subprocess
import optparse
import pathlib
import magic
import datetime
from sys import platform
from os import listdir
from os.path import isfile, join
from termcolor import colored

def main():
	print(colored('ARGV:', 'red'), str(sys.argv[1:]))
	parser = optparse.OptionParser(usage='%prog [options] <file or folder directory>', description="Analyze file count, size and type information on different operating systems")
	parser.add_option('-f', '--file', 
                  dest='file', 
                  #default=filename,
                  help='input parameter required to do analysis'
                  )
	
	options, remainder = parser.parse_args()
	if options.file == None: #and options.directory == None:
		print(colored('ERROR:','red'), ' Neither file nor directory provided with parameters to analyze.\nUse -h or --help to see the parameters')
		print(colored('WARNING:', 'yellow'), 'File or directory not provided, script\'s directory choosen to proceed')
		directory = os.path.dirname(os.path.realpath(__file__))
		filename = directory + '/' + os.path.realpath(__file__)
		exit(1)
		#print(options.file)
	if os.path.isfile(str(options.file)):
		folder_file = 'file'
	elif os.path.isdir(str(options.file)):
		folder_file = 'folder'

	if platform == "linux" or platform == "linux2":
		os_type = 'linux'
	elif platform == "darwin":
		os_type = 'macOS'
	elif platform == "win32":
		os_type = 'windows'
	print(colored('INFO:', 'blue'), os_type + ' operating system detected')
    
	if folder_file == 'folder':
		#directory = os.path.dirname(os.path.realpath(folder_file))
		directory = options.file
		print(colored('INFO:', 'blue'), 'Folder provided as parameter')
		#directory = options.file
		print(colored('INFO:', 'blue'), 'FOLDER: ' + directory)
	
	elif folder_file == 'file':
		#directory = os.path.dirname(os.path.realpath(folder_file))
		filename = options.file
		print(colored('INFO:', 'blue'), 'File provided as parameter')
		print(colored('INFO:', 'blue'), 'FILE: ' + filename)


	print(colored('\n------ PARTI I - PYTHON MODULES', 'green'))
	if folder_file == 'file':
		if os.path.isfile(filename): 
			print(colored('ANALYZE FILE', 'blue'))
			file_absolute = os.path.abspath(filename)
			statinfo = os.stat(filename)
			print(colored('FILE: ', 'yellow'), filename)
			print(colored('ABSOLUTE PATH: ', 'yellow'), file_absolute)
			# FILE SIZE
			print(colored('SIZE: ', 'yellow') + str(statinfo.st_size) + ' bytes')

			# FILE EXTRA
			print(colored('TYPE: ', 'yellow'), magic.from_file(filename))
			print(colored('OWNER UID: ', 'yellow') + str(statinfo.st_uid))
			print(colored('LAST ACCESS: ', 'yellow') + str(datetime.datetime.fromtimestamp(int(statinfo.st_atime)).strftime('%Y-%m-%d %H:%M:%S')))
			print(colored('LAST MODIFIED: ', 'yellow') + str(datetime.datetime.fromtimestamp(int(statinfo.st_mtime)).strftime('%Y-%m-%d %H:%M:%S')))

	elif folder_file == 'folder':
		if os.path.isdir(directory):
			# FILE COUNT
			print(colored('FILE & FOLDER COUNT', 'blue'))
			file_count = -1
			dir_count = 0
			print(colored('ABSOLUTE PATH: ', 'yellow'), directory)
			for name in os.listdir(directory):
				if os.path.isdir(directory + '/' + name):
					dir_count += 1
				if os.path.isfile(directory + '/' + name):
					file_count += 1

			print(colored('FILE COUNT: ', 'yellow'), str(file_count))
			print(colored('FOLDER COUNT: ', 'yellow'), str(dir_count))
			print('---')

			# LIST FILES
			print(colored('List of files in directory:', 'blue'))
			for name in os.listdir(directory):
				print(name)
			

	print(colored('\n------ PART II - EXECUTE COMMAND AND SYSTEM CALLS', 'green'))
	if folder_file == 'file':
		if os.path.isfile(filename):
			print(colored('ANALYZE FILE', 'blue'))
			print(colored('FILE: ', 'yellow'), filename)
			print(colored('ABSOLUTE PATH: ', 'yellow'), file_absolute)
			if os_type != 'windows':
				# FILE SIZE
				process = subprocess.Popen(['file', filename], stdout=subprocess.PIPE)
				out, err = process.communicate()
				out_str = str(out, 'utf-8')
				out_str = out_str.split(':')
				#if '\n' in out_str:
					#out_str = 	out_str.replace('\n','')
				out_str[1] = out_str[1].replace('\n','')
				print(colored('TYPE: ', 'yellow'), out_str[1]) # end=''

				process = subprocess.Popen(['wc','-c',filename], stdout=subprocess.PIPE)
				out, err = process.communicate()
				out_str = str(out, 'utf-8')
				out_str = out_str.split(' ')
				'''
				if '\n' in out_str:
						out_str = 	out_str.replace('\n','')
				if ' ' in out_str:
						out_str = 	out_str.replace(' ','')
				if filename in out_str:
					out_str = 	out_str.replace(filename,'')
					'''
				print(colored('SIZE:', 'yellow'), str(out_str[4]) + ' bytes')
				#print(colored('SIZE:', 'yellow'), os.system('du -kh ' + filename + ' | cut -f1'))
				process = subprocess.Popen(['ls','-la',filename], stdout=subprocess.PIPE)
				out, err = process.communicate()
				out_str = str(out, 'utf-8')
				out_str = out_str.split(' ')
				#print(out_str)
				print(colored('OWNER: ', 'yellow') + str(out_str[2]))
				print(colored('LAST ACCESS: ', 'yellow') + str(out_str[9] + ' ' + out_str[7] + ' ' + out_str[10]))
				process = subprocess.Popen(['stat', filename], stdout=subprocess.PIPE)
				out, err = process.communicate()
				out_str = str(out, 'utf-8')
				out_str = out_str.split(' ')
				#print(out_str)
				print(colored('LAST MODIFIED: ', 'yellow') + str(out_str[15] + ' ' + out_str[13].replace('"','') + ' ' + out_str[17].replace('"','') + ' ' + out_str[16]))
			else:
				#filetype = os.system('exit')
				print(colored('TYPE: ', 'yellow'), str(magic.from_file(filename))) # end=''
				# FILE SIZE
				filesize = str(os.system('DIR ' + filename + ' > null'))
				statinfo = os.stat(filename)
				print(colored('SIZE:', 'yellow'), str(statinfo.st_size) + ' bytes')

	elif folder_file == 'folder':
		if os.path.isdir(directory):
			print(colored('FILE & FOLDER COUNT', 'blue'))
			print(colored('ABSOLUTE PATH: ', 'yellow'), directory)
			if os_type != 'windows':
				print(colored('FOLDER COUNT: ', 'yellow'))
				folder_count = os.system('cd "' + directory + '" && ls -l | grep ^d | wc -l')
				print(colored('FILE COUNT: ', 'yellow'))
				file_count = int(os.system('cd "' + directory + '" && ls -l | grep ^- | wc -l'))
				# FILE COUNT
				#command = 'find ' + directory + ' -type f | wc -l'
				#os.system(command)
				#from subprocess import call
				#call(command, shell=True)
				#process = subprocess.Popen([command], stdout=subprocess.PIPE)
				#out, err = process.communicate()
				#print(out)
			
				print('---')

				# LIST FILES
				print(colored('List of files in directory:', 'blue'))
				os.system('cd "' + directory + '" && ls | xargs -n 1 basename')
				#print(colored('List of files in current directory:', 'blue'))
				process = subprocess.Popen(['ls', directory], stdout=subprocess.PIPE)
				out, err = process.communicate()
				#print(str(out, 'utf-8'))
			else:
				print(colored('FOLDER COUNT: ', 'yellow'), end='')
				#print(os.system('dir /a-d | find /c ":"'))

				print(colored('FILE COUNT: ', 'yellow'), end='')
				print(os.system('dir /a-d | find /c ":"'))
				print(colored('List of files in directory:', 'blue'))
				os.system('cd ' + directory + ' && dir /b /a-d')
		print('---')
		print(colored('SUCCESS:', 'green'), 'Analysis completed')
			

if __name__ == '__main__':
	main()