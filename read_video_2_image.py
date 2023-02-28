import cv2
import glob
import os
from datetime import datetime
from natsort import natsorted


def read_video_as_image(video_file, save=False):
    
    # Generate a path for the results directory with the current timestamp
    timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M")
    save_dir = f"./results/{timestamp}"
    os.makedirs(save_dir, exist_ok=True)
    
    vidcap = cv2.VideoCapture(video_file)
    success, image = vidcap.read()
    count = 0
    while success:
        count +=1
        cv2.imshow('frame', image)  # show frame as image
        cv2.waitKey()
        if save:
            cv2.imwrite(f"{save_dir}/image_{count}.jpg", image)

        success, image = vidcap.read()  # get next frame

    vidcap.release()  # release the video capture object
    
    
read_video_as_image('./test.mp4', True)