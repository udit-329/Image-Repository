import numpy as np
import cv2
import imutils

class colour_descriptors:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	    
        features = []

        height = image.shape[0]
        centre_Y = int(height / 2)

        width = image.shape[1]
        centre_X = int(width / 2)

        #4 regions as startX, endX, startY, endY
        #top-left, top-right, bottom-right, bottom-left
        segments = [(0, centre_X, 0, centre_Y), (centre_X, width, 0, centre_Y), (centre_X, width, centre_Y, height),(0, centre_X, centre_Y, height)]

        #ellipse
        axes_X = int(width * 0.75) // 2
        axes_Y = int(height * 0.75) // 2

        ellip_mask = np.zeros(image.shape[:2], dtype = "uint8")

        cv2.ellipse(ellip_mask, (centre_X, centre_Y), (axes_X, axes_Y), 0, 0, 360, 255, -1)

        for (start_X, end_X, start_Y, end_Y) in segments:

            corner_mask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(corner_mask, (start_X, start_Y), (end_X, end_Y), 255, -1)
            corner_mask = cv2.subtract(corner_mask, ellip_mask)

            #extract a colour histogram for corners
            hist = self.histogram(image, corner_mask)
            features.extend(hist)
        
        #extract a colour histogram for corners
        hist = self.histogram(image, ellip_mask)
        features.extend(hist)

        return features

    def histogram(self, image, mask):

        hist = cv2.calcHist([image], [0,1,2], mask, self.bins, [0, 180, 0, 256, 0, 256])

        hist = cv2.normalize(hist, hist).flatten()

        return hist