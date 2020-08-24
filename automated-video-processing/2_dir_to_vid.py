from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *  # ImageClip
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

# RUN:
# clip = ImageSequenceClip(filepaths, fps=1)  # each image last 1 s
# clip.write_videofile(output_video)


directory = {}
# generates the file names in a directory tree by walking the tree either top-down or bottom-up.
for root, dirs, files in os.walk(thumbnail_per_half_seond_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        # key-value pair for each filet:
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath  # 1000 : ./temp/1000

new_paths = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_paths.append(filepath)
    # print(k)  # 220000.0

# RUN:
# clip = ImageSequenceClip(new_paths, fps=10)
# clip.write_videofile(output_video)

#  turn each filepath to a file itself
my_clips = []
for path in list(new_paths):
    frame = ImageClip(path)
    print(frame.img)  # numpy array
    my_clips.append(frame.img)

# RUN:
clip = ImageSequenceClip(my_clips, fps=22)
clip.write_videofile(output_video)
