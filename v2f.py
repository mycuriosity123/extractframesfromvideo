# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import youtube_dl
import argparse
from threading import *
import time
import os


parser = argparse.ArgumentParser(description='video processing.....')
parser.add_argument("-url", "--video_url", type=str, help="url of the video whose frames need to be extracted",required=True)
args = parser.parse_args()

class vTf:
    def __init__(self,link):
        self.link = link

    def v2f(self):
        ydl_opts = {}
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(self.link, download=False)
        path=os.path.join(os.path.dirname(os.getcwd()), "frames")
        if not os.path.exists(path):
            os.makedirs(path)
        formats = info_dict.get('formats', None)
        for f in formats:
            url = f.get('url', None)
            vidcap = cv2.VideoCapture(url)
            frame=0
            vidcap.set(cv2.CAP_PROP_POS_MSEC , frame)
            success, image = vidcap.read()
            count = 0
            while success:
                cv2.imwrite(path+"\\"+"frame%d.jpg" % count, image)
                frame+=2
                vidcap.set(cv2.CAP_PROP_POS_MSEC, int(frame*1000))
                success, image = vidcap.read()
                count += 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cvf=vTf(args.video_url)
    start_time = time.time()
    t1=Thread(target=cvf.v2f)
    t1.start()
    t1.join()
    end_time = time.time()
    print("successfully extracted frames from video")
    print("total time :",end_time-start_time , "seconds")
