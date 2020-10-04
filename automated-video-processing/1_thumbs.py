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

os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
os.makedirs(thumbnail_per_half_seond_dir, exist_ok=True)

clip = VideoFileClip(source_path)

print(clip.reader.fps)
print(clip.reader.nframes)
print(clip.duration)

duration = clip.duration
max_duration = int(duration) + 1
# convert to a int
fps = clip.reader.fps
nframes = clip. reader.nframes
seconds = nframes/(fps*1.)
# for i in range(0, max_duration):
#     print(f"frame at {i} seconds")
#     #  turn the frames into a enumerate
#     for i, frame in enumerate(clip.iter_frames()):
#         # frame = clip.get_frame(int(i))
#         if i % fps == 0:
#             current_ms = (i/fps) * 1000
#             # print(frame)  # np.array
#             # new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")

#             new_img_filepath = os.path.join(
#                 thumbnail_per_frame_dir, f"{i}.jpg")
#             # save image per frame as jpg using Image lib
#             new_image = Image.fromarray(frame)
#             new_image.save(new_img_filepath)


"""
 [[172 116  77]
  [178 122  83]
  [174 121  79]
  ...
  [ 53  35  24]
  [ 55  37  26]
  [ 57  39  28]]]
 """
for i, frame in enumerate(clip.iter_frames()):
    # frame = clip.get_frame(int(i))
    fps_half = int(fps/2.0)
    if i % fps_half == 0:
        current_ms = int((i/fps_half) * 1000)
        # print(frame)  # np.array
        # new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")

        new_img_filepath = os.path.join(
            thumbnail_per_half_seond_dir, f"{i}.jpg")
        # save image per frame as jpg using Image lib
        new_image = Image.fromarray(frame)
        new_image.save(new_img_filepath)
