import os

ABS_PATH = os.path.abspath(__file__)
#/Documents/30-day/automated-video-processing/conf.py
BASE_DIR = os.path.dirname(ABS_PATH)
# /Documents/30-day/automated-video-processing
DATA_DIR = os.path.join(BASE_DIR, "data")
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "inputs")
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, 'outputs')
