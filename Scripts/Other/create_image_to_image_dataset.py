##############################################################################
#
# This script copies images from the source directory, present in target
# folder/folders to the newly created folder/folders. This script can be
# use to create datasets in image to image problems
#
##############################################################################

import os
import shutil

def main():

	raw_dir_name = 'Faces_Raw'
	raw_dir_path = os.path.join(os.getcwd(), raw_dir_name)
	
	target_dir_names = ['Urban_Camo_Target', 'Wood_Camo_Target', 'Desert_Camo_Target']

	for target_dir_name in target_dir_names:
		
		source_dir_name = target_dir_name.replace('Target', 'Source')
		source_dir_path = os.path.join(os.getcwd(), source_dir_name)
		os.makedirs(source_dir_path)
		
		target_dir_path = os.path.join(os.getcwd(), target_dir_name)
		images = os.listdir(target_dir_path)
		
		for image in images:

			raw_image_path = os.path.join(raw_dir_path, image)
			source_image_path = os.path.join(source_dir_path, image)
			try:
				shutil.copy(raw_image_path, source_image_path)
			except FileNotFoundError:
				print(f'Image {image} not found in raw folder')

if __name__ == "__main__":
	main()
