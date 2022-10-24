import json
import time
import git_leaks_functions
	  
# Data to be written 
dictionary ={ 
	"id": "04", 
	"name": "sunil", 
	"department": "HR"
} 
	  
# Serializing json  





def load_to_json(dic):

	json_object = json.dumps(dic, indent = 4)


	# print(json_object)

	Register = open('commitRegisterJSON.txt', 'w')
	Register.write(str(json_object))
	Register.close()

	time.sleep(1)
	print('Matches load to json file')


if __name__ == '__main__':
	REPO_DIR = './skale/skale-manager'
	repoCommits = git_leaks_functions.extract(REPO_DIR)
	processedCommits = git_leaks_functions.transformToDictionary(repoCommits)
	print(processedCommits)
	load_to_json(processedCommits)
	print()
