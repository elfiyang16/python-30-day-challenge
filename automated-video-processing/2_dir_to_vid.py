from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

import os

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
# make a dir to store the images we got
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail_per_half_seond_dir = os.path.join(
    SAMPLE_OUTPUTS, "thumbnails_per_half_seond")
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

# list of all files and directories
this_dir = os.listdir(thumbnail_per_half_seond_dir)
# get all the filenames ends with jpg and join with thumbnaoil_dir
filepaths = [os.path.join(thumbnail_per_half_seond_dir, fname)
             for fname in this_dir if fname.endswith("jpg")]

# filepaths = []
# for fname in this_dir:
#     if fname.endswith("jpg"):
#         path = os.path.join(thumbnail_dir, fname)
#         filepaths.append(path)

print(filepaths)
clip = ImageSequenceClip(filepaths, fps=1)  # each image last 1 s
clip.write_videofile(output_video)
