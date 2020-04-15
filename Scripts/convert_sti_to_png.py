#!/usr/bin/env python3

##############################################################################
#
# This script convert sti files from passed folder to png files
#
##############################################################################

import argparse
import os
import sys

sys.path.append(os.getcwd())

from ja2py.fileformats.Sti import load_8bit_sti, load_16bit_sti, is_8bit_sti, is_16bit_sti

def write_image(output_file, image, transparency=0, verbose=False):
    if verbose:
        print("Writing:  {}".format(output_file))
    image.save(output_file, transparency=transparency)

def write_sequence_of_8bit_images_to_target_directory(sequence, target_directory, verbose=False):
    for image_index, sub_image in enumerate(sequence):
        image_file = os.path.join(target_directory, '{}.png'.format(image_index))
        write_image(image_file, sub_image.image, verbose=verbose)


def write_24bit_png_from_sti(output_file, sti, verbose=False):
    return write_image(output_file, sti.image, transparency=None, verbose=verbose)


def write_8bit_png_from_sti(output_file, sti, verbose=False):
    if len(sti.images) > 1:
        base_dir = output_file
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        if sti.animated:
            for i, animation in enumerate(sti.animations):
                animation_dir = os.path.join(base_dir, 'ANI{}'.format(i))
                if not os.path.exists(animation_dir):
                    os.makedirs(animation_dir)
                write_sequence_of_8bit_images_to_target_directory(animation, animation_dir, verbose=verbose)
        else:
            write_sequence_of_8bit_images_to_target_directory(sti.images, base_dir, verbose=verbose)
    else:
        write_image(output_file, sti.images[0].image, verbose=verbose)


def main():

	parser = argparse.ArgumentParser(description='Sti converter')
	parser.add_argument('image_dir_name', help="name of source directory")
	parser.add_argument('dest_dir_name', help="name of destination directory")

	args = parser.parse_args()
	image_dir = os.path.join(os.getcwd(),args.image_dir_name)
	dest_dir = os.path.join(os.getcwd(),args.dest_dir_name)
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)

	files_path = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

	for file_path in files_path:

	    output_file = None
	    verbose = False	

	    sti_file = file_path
	    sti_file = os.path.expanduser(os.path.expandvars(sti_file))
	    sti_file = os.path.normpath(os.path.abspath(sti_file))

	    if not output_file:
	        output_file = os.path.join(dest_dir,
	                                   os.path.splitext(os.path.basename(sti_file))[0] + '.png')
	    output_file = os.path.expanduser(os.path.expandvars(output_file))
	    output_file = os.path.normpath(os.path.abspath(output_file))

	    if verbose:
	        print("Input file:  {}".format(sti_file))
	        print("Output file: {}".format(output_file))

	    with open(sti_file, 'rb') as file:
	        if is_8bit_sti(file):
	            sti = load_8bit_sti(file)
	            if verbose:
	                print("File Details: ")
	                print("Data Type: indexed 8bit")
	                print("Number of single images: {}".format(len(sti)))
	                for i, sub_image in enumerate(sti.images):
	                    print("Subimage {}: Size {}x{}, Shift +{}+{}".format(
	                        i+1,
	                        sub_image.image.size[0],
	                        sub_image.image.size[1],
	                        sub_image.offsets[0],
	                        sub_image.offsets[1]
	                    ))
	            write_8bit_png_from_sti(output_file, sti, verbose=verbose)
	        elif is_16bit_sti(file):
	            sti = load_16bit_sti(file)
	            if verbose:
	                print("File Details: ")
	                print("Data Type: RGB 16bit")
	                write_24bit_png_from_sti(output_file, sti, verbose=verbose)

	        if verbose:
	            print("Done")

if __name__ == "__main__":
    main()
