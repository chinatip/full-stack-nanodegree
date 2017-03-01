import os
def rename_files():
	#get file names from a folder
	file_list = os.listdir(r"D:\My projects\full-stack-nanodegree\Programming Foundations with Python\alphabet\alphabet\secret-message")
	saved_path = os.getcwd()
	os.chdir(r"D:\My projects\full-stack-nanodegree\Programming Foundations with Python\alphabet\alphabet\secret-message")
	#for each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()