import cv2
import numpy as np

image_file = "./assets/bowers.jpg"

# Original
image = cv2.imread(image_file)
cv2.imshow("Original image", image)

# Grayscale
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(image)
cv2.imwrite("./temp/grayscale.jpg", gray_image)
cv2.imshow("Grayscale image", gray_image)

# Black and White
thresh, bw_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite("./temp/bw_image.jpg", bw_image)
cv2.imshow("Binary image", bw_image)

#Noise Removal
def noise_removal(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    denoised_image = cv2.medianBlur(blurred_image, 3)
    return(image)

no_noise = noise_removal(bw_image)
cv2.imwrite("./temp/no_noise.jpg", no_noise)
cv2.imshow("Noise Removal Image", no_noise)

cv2.waitKey(0)
cv2.destroyAllWindows()
