from depthai_sdk import Previews
from depthai_sdk.managers import PipelineManager, PreviewManager
import depthai as dai
import cv2
import numpy as np

pm = PipelineManager()
pm.createLeftCam(xout=True, res=dai.MonoCameraProperties.SensorResolution.THE_480_P)
pm.createRightCam(xout=True, res=dai.MonoCameraProperties.SensorResolution.THE_480_P)
pm.createDepth(useRectifiedLeft=True, useRectifiedRight=True)

with dai.Device(pm.pipeline) as device:
    # pv = PreviewManager(display=[Previews.rectifiedLeft.name, Previews.rectifiedRight.name])
    # pv.createQueues(device)
    # print(Previews.rectifiedLeft.name)
    # extrinsics = np.array(device.readCalibration().getCameraExtrinsics(dai.CameraBoardSocket.LEFT, dai.CameraBoardSocket.RIGHT))
    # np.save("ext_l_to_r", extrinsics)
    # extrinsics = np.array(device.readCalibration().getCameraExtrinsics(dai.CameraBoardSocket.RIGHT, dai.CameraBoardSocket.LEFT))
    # np.save("ext_r_to_l", extrinsics)
    # intrinsic_left = np.array(device.readCalibration().getCameraIntrinsics(dai.CameraBoardSocket.LEFT))
    # np.save("int_l", intrinsic_left)
    # intrinsic_right = np.array(device.readCalibration().getCameraIntrinsics(dai.CameraBoardSocket.RIGHT))
    # np.save("int_r", intrinsic_right)
    
    left_q = device.getOutputQueue(name=Previews.rectifiedLeft.name, maxSize=8, blocking=False)
    right_q = device.getOutputQueue(name=Previews.rectifiedRight.name, maxSize=8, blocking=False)

    while True:
        # left_raw : dai.ImgFrame = left_q.get()
        inLeft = left_q.tryGet()
        inRight = right_q.tryGet()

        if inLeft is not None:
            cv2.imwrite("images/out/left.png", inLeft.getCvFrame())
            cv2.imshow("left", inLeft.getCvFrame())

        if inRight is not None:
            cv2.imwrite("images/out/right.png", inRight.getCvFrame())
            cv2.imshow("right", inRight.getCvFrame())

        if cv2.waitKey(1) == ord('q'):
            break