##############################################################################
#
# This script remove prefix from all files present in script folder.
#
##############################################################################


import os
import shutil

def main():

	dir_name = input('Give me a name of directory to perform reverse renaming files: ')
	dir_path = os.path.join(os.getcwd(), dir_name)
	
	images = os.listdir(dir_path)
	
	for image in images:
		print(image)
		try:
			prefix, image_name = image.split('_')[0], image.split('_')[1]
		except IndexError:
			continue

		dest_dir_path = os.path.join(dir_path, prefix)
		curr_image_path = os.path.join(dir_path, image)
		dest_image_path = os.path.join(dest_dir_path, image_name)

		try:
			shutil.move(curr_image_path, dest_image_path)
		except FileNotFoundError:
			os.makedirs(dest_dir_path)
			shutil.move(curr_image_path, dest_image_path)

if __name__ == "__main__":
	main()
