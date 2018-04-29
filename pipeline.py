#!env python3

from os import walk
from os.path import isfile, join, basename
import pathlib

import cv2
import glob

import numpy as np

from tqdm import tqdm


def camera_calibration(root_dir='camera_cal',
                       calibrated_dir='calibrated_dir', nx=9, ny=6):
    # read each pathname in camera_cal folder
    images = glob.glob('camera_cal/calibration*.jpg')

    pathlib.Path(calibrated_dir).mkdir(parents=True, exist_ok=True)
    # mkdir for outputting to calibration_complete_dir

    objpoints = []
    imgpoints = []
    objp = np.zeros((nx*ny,3), np.float32)
    objp[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2)


    for img_file_name in tqdm(images, desc="finding corners"):

        img = cv2.imread(img_file_name)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
        if ret == True:
            imgpoints.append(corners)
            objpoints.append(objp)

    for img_file_name in tqdm(images, desc="calibrating cameras"):
        img = cv2.imread(img_file_name)
        img_size = (img.shape[1], img.shape[0])

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints,
                                                           imgpoints,
                                                           gray.shape[::-1],
                                                           None, None)
        img = cv2.undistort(img, mtx, dist)
        img_path_out = join(calibrated_dir, basename(img_file_name))
        cv2.imwrite(img_path_out,img)


def pipeline(img=None):
    """Find lane lines in an input image

    Each stage of the pipeline transforms until we paint lines where the lane
    lines are.
    """
    # cut out polygon of image

    # flatten and scale image

    # sobel operator threshold

    # mag_thresh threshold

    # dir_threshold threshold

    # combine previous 3 thresholds

    # find histograms

    # sliding window search

    # Measure curvature with f(y)=Ay^2 + By + C

    # paint lines on image
    pass

def pipeline_test_images():
    pipeline()
    pass

# camera_calibration()
