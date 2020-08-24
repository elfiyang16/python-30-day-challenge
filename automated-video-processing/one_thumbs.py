from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

import os

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnail_dir = os.path.join(SAMPLE_INPUTS, "thumbnails")
# make a dir to store the images we got
os.makedirs(thumbnail_dir, exist_ok=True)

clip = VideoFileClip(source_path)

print(clip.reader.fps)
print(clip.reader.nframes)
print(clip.duration)

duration = clip.duration
max_duration = int(duration) + 1
# convert to a int
for i in range(0, max_duration):
    print(f"frame at {i} seconds")
    frame = clip.get_frame(int(i))
    # print(frame)  # np.array
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    # save image per frame as jpg using Image lib
    new_image = Image.fromarray(frame)
    new_image.save(new_img_filepath)

"""
 [[172 116  77]
  [178 122  83]
  [174 121  79]
  ...
  [ 53  35  24]
  [ 55  37  26]
  [ 57  39  28]]]
 """
