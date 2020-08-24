from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *  # ImageClip
from PIL import Image
from moviepy.video.fx.all import crop
import os


source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)

output_path1 = os.path.join(GIF_DIR, 'sample1.gif')
output_path2 = os.path.join(GIF_DIR, 'sample2.gif')

clip = VideoFileClip(source_path)
fps = clip.reader.fps
# note that you need to overwrite the original object
subclip = clip.subclip(10, 20)  # the timeperiod we want the clip
subclip = subclip.resize(width=320)
# RUN:
subclip.write_gif(output_path1, fps=fps, program='ffmpeg')
