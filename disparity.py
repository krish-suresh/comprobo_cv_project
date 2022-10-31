import cv2
import numpy as np

folder = "mac126"
RECTIFIED = True

## Load in camera intrinsics and extrinsics
extrinsics = np.load("ext_l_to_r.npy") 
intrinsic_left = np.load("int_l.npy")
intrinsic_right = np.load("int_r.npy") 

## Read saved image stills
if RECTIFIED:
    right = cv2.imread(f"images/{folder}/rect_right.png")
    left = cv2.imread(f"images/{folder}/rect_left.png")
else: 
    right = cv2.imread("right.png")
    left = cv2.imread("left.png")

## Convert to monocolor
right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)

h,w = right.shape
disparity_map = np.zeros_like(right)
kernel_size = 10 # kernel size NxN correspondence matching for SSD
max_offset = 80 # Maximum search offset

k_h = kernel_size//2 # Half of kernel

for y in range(k_h, h-k_h):
    for x in range(k_h, w-k_h):
        # Get left image pixel window
        left_window = left[y-k_h:y+k_h, x-k_h:x+k_h]
        # Left and right offset search bounds
        offset_left = max(k_h, x-max_offset)
        offset_right = x
        best_offset = 0
        best_ssd = 9999999
        # Iterate through offset values to get best matching correspondence
        for offset in range(offset_left, offset_right,2):
            right_window = right[y-k_h:y+k_h, offset-k_h:offset+k_h]
            diff = left_window - right_window # compute window difference
            ssd = np.sum(np.square(diff)) # calculate sum of squared difference
            if ssd < best_ssd: # minimize
                best_offset = offset
                best_ssd = ssd
        disparity_map[y,x] = (255/max_offset)*(x-best_offset) # Save disparity as a distance proportional to left image
    print(f"row: {y}/{h-k_h}")
cv2.imwrite(f"images/{folder}/disp.png", disparity_map)
cv2.imshow("stereo", np.concatenate((left, right), axis=1))
cv2.imshow("disp",disparity_map)
cv2.waitKey()