##############################################################################
#
# This script copies images from the source directory to the destination
# directory or extract the main image from folders, rename it and copy to
# the destination directory.
# It is the third stage of image pre-processing after the stage of converting
# sti files to png files
# This script solves the problem of manually moving main images from folders
# that were created by unpacking sti files.
#
##############################################################################

import os
import argparse
import shutil

def main():
	parser = argparse.ArgumentParser(description='Images Unpacker')
	parser.add_argument('image_dir_name', help="name of source directory")
	parser.add_argument('dest_dir_name', help="name of destination directory")

	args = parser.parse_args()
	image_dir = os.path.join(os.getcwd(),args.image_dir_name)
	dest_dir = os.path.join(os.getcwd(),args.dest_dir_name)
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)
	files_path = [os.path.join(image_dir, file_name) for file_name in os.listdir(image_dir)]

	for file_path in files_path:
		if os.path.isdir(file_path):
			folder_name = os.path.basename(file_path)
			main_image_path = os.path.join(file_path, '0.png')
			shutil.copy(f'{main_image_path}', os.path.join(dest_dir, folder_name))
		else:
			file_name = os.path.basename(file_path)
			shutil.copy(file_path, os.path.join(dest_dir, file_name))

if __name__ == "__main__":
	main()
