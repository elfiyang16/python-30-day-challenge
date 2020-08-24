from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
import os

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")

clip = VideoFileClip(source_path)

print(clip.reader.fps)
print(clip.reader.nframes)
print(clip.duration)
