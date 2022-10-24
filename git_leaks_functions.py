from git import Repo

import os
import copy

import re
import signal
import sys
import time
#import pwn
import pdb



def handler_signal(signal, frame):
	print('\n\n [!] Out .............. \n')
	sys.exit(1)

signal.signal(signal.SIGINT, handler_signal)


REPO_DIR = './skale/skale-manager'


# time.sleep(15)

def extract(path):
	#Repo permite especificar la url de un repositorio que luego se guarda en la variable especificada
	repo = Repo(path)
	# print(repo)
	# print(repo.status)

	print('Repository extracted')
	time.sleep(1)
	return repo.iter_commits()



def transform(commits):

	#list with all commit objects
	commits = list(commits)


	#variables for the progress bar
	Reference = len(commits) 
	iterationNumber = 0
	progress = 0

	#list where I will store the matches
	processedCommits = list()

	for i in commits:
		iterationNumber += 1
		patterns = [re.compile(r'password'),re.compile(r'key'),re.compile(r'security'),re.compile(r'critical')]
		for pattern in patterns:
			if ( bool(re.search(pattern, i.message)) ):
				processedCommits.append(i)
		if (iterationNumber/Reference)*100 - progress > 0:
			progress += 1
			print('Filtering commits:')
			print(str(int((iterationNumber/Reference)*100))+'%','[' + ''.join(['=' for i in range(int((iterationNumber/Reference)*100))])+ str('>') + ''.join([' ' for i in '=' for i in range(int((1 - (iterationNumber/Reference))*100))]) +']')
			time.sleep(0.001)
			os.system('cls')

	return processedCommits


def transformToDictionary(commits):

	#list with all commit objects
	commits = list(commits)


	#variables for the progress bar
	Reference = len(commits) 
	iterationNumber = 0
	progress = 0

	
	#patterns to search
	patterns = [[re.compile(r'password'), 'password'], [re.compile(r'key'), 'key'], [re.compile(r'security'), 'security'], [re.compile(r'critical'), 'critical']]

	#dictionary where I will store the matches classified by 'pettern searched' and 'commit date'
	matches = {i[1]:[dict()] for i in patterns}

	for i in list(commits):
		iterationNumber += 1


		#if the commit message contains the pattern I store it in the dictionry
		for index, pattern_and_key in enumerate(patterns):
			pattern = pattern_and_key[0]
			key = pattern_and_key[1]
			counter = 0
			if ( bool(re.search(pattern, i.message)) ):
				counter += 1

				matches[key][0].setdefault(str(i.committed_datetime), i.message)


		if (iterationNumber/Reference)*100 - progress > 0:
			progress += 1
			print('Filtering commits:')
			print(str(int((iterationNumber/Reference)*100))+'%','[' + ''.join(['=' for i in range(int((iterationNumber/Reference)*100))])+ str('>') + ''.join([' ' for i in '=' for i in range(int((1 - (iterationNumber/Reference))*100))]) +']')
			time.sleep(0.001)
			os.system('cls')

	return matches

def load(processedCommits):
	Register = open('commitRegister.txt', 'a')
	print('MATCHES FOUND: ')
	for i,commit in enumerate(processedCommits):
		print('matched commit {j:.0f}:\n'.format(j=i) , commit.message)
		Register.write(str(commit.message))
		Register.write('\n\n\n')
	Register.close()

	time.sleep(1)









#TO CHECK ALL OBJECT ATTRIBUTES (i)
# for j in (dir(i)):
#     print(j, end = ':  ')
#     exec(f'print(i.{j})')
#     print()
# input()