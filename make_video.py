import glob
import cv2
import os
from datetime import datetime

from tqdm import tqdm
from natsort import natsorted


def create_video(input_path, output_path, fps):
    img_list = natsorted(glob.glob(f"{input_path}/*.png"))

    size = None
    frame_array = []
    for idx, path in tqdm(enumerate(img_list)):
        if idx % 2 == 0 or idx % 5 == 0:
            continue
        img = cv2.imread(path)
        if size is None:
            height, width, layers = img.shape
            size = (width, height)
        frame_array.append(img)

    timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M")
    save_dir = f'./results/{timestamp}'
    os.makedirs(save_dir, exist_ok=True)
    out_path = os.path.join(save_dir, output_path)

    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for frame in frame_array:
        out.write(frame)
    out.release()


if __name__ == '__main__':
    create_video('./img_data', 'demo.mp4', 10)
    
    

