
import cv2 
import os
from datetime import datetime

def video_to_image(video_file, save=False): 
    # Generate a path for the results directory with the current timestamp
    timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M")
    save_dir = f"./results/{timestamp}"
    os.makedirs(save_dir, exist_ok=True)
    
    # capture the video 
    vidObj = cv2.VideoCapture(video_file) 
    
    # Used as counter variable 
    count = 0

    # checks whether frames were extracted 
    success = 1

    while success: 
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        cv2.imshow('frame', image)  # show frame as image
        cv2.waitKey(1)

        if save:
            # Saves the frames with frame-count 
            cv2.imwrite(f"{save_dir}/frame%d.jpg" % count, image) 

        count += 1
        
    
video_to_image(0, True)