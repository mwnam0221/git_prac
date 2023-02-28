import glob
import cv2
import os
from datetime import datetime

from tqdm import tqdm
from natsort import natsorted


class ImageProcessing:
    def __init__(self):
        pass
    
    def create_video(self, input_path, output_path, fps):
        img_list = natsorted(glob.glob(f"{input_path}/*.png"))
        
        frame_array = []
        for idx, path in tqdm(enumerate(img_list)):
            if idx % 2 == 0 or idx % 5 == 0:
                continue
            img = cv2.imread(path)
            frame_array.append(img)

        size = frame_array[0].shape[:2][::-1]
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M")
        save_dir = f'./results/{timestamp}'
        os.makedirs(save_dir, exist_ok=True)
        out_path = os.path.join(save_dir, output_path)

        out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
        for frame in frame_array:
            out.write(frame)
        out.release()
    
    def read_images(self, path, save=False):
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M")
        save_dir = f"./results/{timestamp}"
        os.makedirs(save_dir, exist_ok=True)

        images = []
        for i, img in enumerate(natsorted(glob.glob(path))[:10]):
            n = cv2.imread(img)
            images.append(n)

            cv2.imshow(f"image{i}", n)
            k = cv2.waitKey()
            if k ==27: #Esc key to stop
                break

            if save:
                cv2.imwrite(f"{save_dir}/image_{i}.jpg", n)

        cv2.destroyAllWindows()
    
    def read_video_as_image(self, video_file, save=False, FLIP=False) :
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M")
        save_dir = f"./results/{timestamp}"
        os.makedirs(save_dir, exist_ok=True)

        vidcap = cv2.VideoCapture(video_file)
        count = 0
        while True:
            success, image = vidcap.read()
            if not success:
                break
            count += 1
            
            if FLIP:
                image = cv2.flip(image, -1)
            cv2.imshow('frame', image)
            # cv2.imshow(f'frame_{count}', image)
            k = cv2.waitKey(1)
            if k ==27: #Esc key to stop
                break
            
            if save:
                cv2.imwrite(f"{save_dir}/image_{count}.jpg", image)

        vidcap.release()
                
ip = ImageProcessing()

# create a video
# ip.create_video("./img_data", "PascalRaw.mp4", 5)

# # read and show up to 10 images from a directory
ip.read_images("./img_data/*.png", save=True)

# # # read a video and show each frame as an image
# ip.read_video_as_image(0, save=False)


