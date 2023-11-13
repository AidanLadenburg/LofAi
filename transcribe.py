import whisper
import time
import os
import shutil
from tqdm import tqdm

def transcribe_folder(folder):
    """
    Finds vocals in folder of files
    Writes outputs to "output.txt" in input folder
    """
    start = time.time()
    size = "base.en"
    model = whisper.load_model(size)
    filepath = folder
    try:
        os.remove(filepath+"/output.txt")
    except:
        pass
    try:  
        f = open(filepath+"/output.txt", "x", encoding="utf-8")
    except:
        pass
    f = open(filepath+"/output.txt", "w", encoding="utf-8")
    for file in tqdm(os.listdir(filepath)):
        if file[-3:-1] == "mp":
            sections = 0
            result = model.transcribe(filepath+"/"+file)
            res = result["segments"]
            for seg in res:
                if (seg['no_speech_prob'] < 0.35) and (not seg['text'] == ".") and len(seg['text'].split(" ")) > 3:
                    sections += 1
                else:
                    pass
            f.write(f"{file}: {sections}\n")

    f.close()
    print("Time:",(int((time.time()-start)*100))/100)

def find_files(limit):
    """
    Find all files that exceed the limit and copys them to a new folder "flagged_songs" for review
    Higher limits act as a higher % of vocals tolerated
    """
    try:
        shutil.rmtree(f"{base_folder}/musika/flagged_songs")
    except:
        pass
    os.makedirs(f"{base_folder}/musika/flagged_songs", exist_ok=True)
    scores = open(f"{base_folder}/musika/mp3ed/output.txt", "r", encoding="utf-8")
    data = scores.read()
    files = data.split("\n")
    scores.close()
    for item in files:
        x = item.split(": ")
        if len(x) > 1:
            ratio = int(x[1])/(os.path.getsize(f"{base_folder}/musika/mp3ed/{x[0]}")/500000)
            if (ratio >= limit) or int(x[1]) >= 150:
                print(x)
                print(int(x[1])/(os.path.getsize(f"{base_folder}/musika/mp3ed/{x[0]}")/500000))
                #shutil.copyfile(f"{base_folder}/musika/mp3ed/{x[0]}", f"{base_folder}/musika/flagged_songs/({x[1]})-{x[0]}")
                g = "{:.2f}".format(ratio)
                shutil.copyfile(f"{base_folder}/musika/mp3ed/{x[0]}", f"{base_folder}/musika/flagged_songs/({g, x[1]})-{x[0]}")



if __name__ == '__main__':
    base_folder = "ENTER BASE FOLDER HERE"
    transcribe_folder(f"{base_folder}/musika/mp3ed")
    find_files(1)