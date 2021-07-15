import pathlib
import subprocess

for scr_file in pathlib.Path("./scr/").rglob('*.mov'):
    print(scr_file)
    out_file="./out/" + str(scr_file.stem) + ".mp4"
    subprocess.run(["ffmpeg", "-i", str(scr_file),"-vcodec","libx265", str(out_file)])