##############################################################################
#
# This script take prefix from the user and rename all file in script folder
# with this prefix
#
##############################################################################

import os

def main():

	PREFIX = input('Give me a prefix to rename files: ')
	image_dir = os.getcwd()

	for image in os.listdir(image_dir):
		if str(image) != 'rename_files.py':
			image_path = os.path.join(image_dir, image)
			image_name = os.path.basename(image_path)
			os.rename(image_path, os.path.join(image_dir, f'{PREFIX}_{image_name}'))

if __name__ == "__main__":
	main()

