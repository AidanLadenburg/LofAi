import subprocess
import os
from tqdm import tqdm

infile = "FOLDER TO BE PROCESSED"
outfile = "FOLDER TO OUTPUT MP3s"
i=0

for file in tqdm(os.listdir(infile)):
    i+=1
    subprocess.call(["ffmpeg", "-i", f"{infile}/{file}", f"{outfile}/{i}.mp3"])