import cv2
import glob
import os
from datetime import datetime
from natsort import natsorted

#changed
def read_images(path, save=False):
    # Generate a path for the results directory with the current timestamp
    timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M")
    save_dir = f"./results/{timestamp}"
    os.makedirs(save_dir, exist_ok=True)

    images = []
    # Read up to 10 images from the sorted path of image files
    for i, img in enumerate(natsorted(glob.glob(path))[:10]):
        n = cv2.imread(img)
        images.append(n)

        # Show the image on a window and wait for keyboard input
        cv2.imshow(f"image{i}", n)
        cv2.waitKey()

        if save:
            # Save the image as a JPEG file
            cv2.imwrite(f"{save_dir}/image_{i}.jpg", n)

    # Close all windows
    cv2.destroyAllWindows()


read_images('./img_data/*.png', True)
