import cv2
import numpy as np


extrinsics = np.load("ext_r_to_l.npy") 
intrinsic_left = np.load("int_l.npy")
intrinsic_right = np.load("int_r.npy") 

right = cv2.imread("images/mac126/right.png")
left = cv2.imread("images/mac126/left.png")
default_rect_r = cv2.imread("images/mac126/rect_right.png")
default_rect_l = cv2.imread("images/mac126/rect_left.png")

right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)

def rectify(right, left, extrinsics, intrinsic_left, intrinsic_right):
    R = extrinsics[0:3, 0:3]
    T = extrinsics[0:3,3]

    e_1 = T/np.linalg.norm(T)
    e_2 = np.array([-T[1], T[0],0])/np.linalg.norm(T[0:2])
    e_3 = np.cross(e_1, e_2)
    R_rect = np.array([e_1, e_2, e_3])
    f_l = intrinsic_left[0][0]
    f_r = intrinsic_right[0][0]
    h,w = right.shape
    rect_l = -np.ones_like(left)
    rect_r = -np.ones_like(right)
    R_1 = R_rect
    R_2 = np.matmul(R,R_rect)

    for y in range(h):
        for x in range(w):
            p_l = np.matmul(R_1, [x, y, f_l])
            x_r = int(p_l[0])
            y_r = int(p_l[1])
            if 0 <= x_r < w and 0 <= y_r < h:
                rect_l[y_r][x_r] = left[y][x]
            p_r = np.matmul(R_2, [x, y, f_r])
            x_r = int(p_r[0])
            y_r = int(p_r[1])
            if 0 <= x_r < w and 0 <= y_r < h:
                rect_r[y_r][x_r] = right[y][x]
    return rect_r, rect_l
rect_r, rect_l = rectify(right, left, extrinsics, intrinsic_left, intrinsic_right)
cv2.imshow("stereo", np.concatenate((left, right), axis=1))
cv2.imshow("rect", np.concatenate((rect_l, rect_r), axis=1))
cv2.imwrite(f"rect_l.png", rect_l)
cv2.imwrite(f"rect_r.png", rect_r)
cv2.waitKey()