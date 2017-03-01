import os
import string
# from shutil import copyfile
import shutil

path = "./alphabet/alphabet/"
message_folder = "generated_message/"
newpath = path + message_folder

def generate_secret_message():
	# message = raw_input("Message : ")
	m = "abcd"
	dictionary = getDictionary()
	manageFolder()
	encryptMessage(m, dictionary)
	
	
	
def getDictionary():
	file_list = os.listdir(path)
	if 'generated_message' in file_list:
		file_list.remove('generated_message')
	alphabets = list(string.ascii_lowercase)
	alphabets.append(".")
	alphabets.append(" ")
	return dict(zip(alphabets, file_list))

def manageFolder():
	if os.path.exists(newpath):
		for the_file in os.listdir(newpath):
			file_path = os.path.join(newpath, the_file)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
				#elif os.path.isdir(file_path): shutil.rmtree(file_path)
			except Exception as e:
				print(e)
	else:
		os.makedirs(newpath)

def encryptMessage(m, dictionary):
	for char in m:
		if dictionary.get(str(char), None) == None:
			file_name = dictionary.get(" ", None)
		else:
			file_name = dictionary.get(str(char), None)
		shutil.copy(path+file_name, newpath+file_name)



generate_secret_message()