import cv2
import numpy as np

# 開啟相機
left_camera = cv2.VideoCapture(1)
right_camera = cv2.VideoCapture(2)

# 設置攝像機的解析度
left_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
left_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
right_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
right_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# 讀取標定檔案
# with np.load('stereo_calibration.npz') as data:
#     mtx_left = data['mtx_left']
#     dist_left = data['dist_left']
#     mtx_right = data['mtx_right']
#     dist_right = data['dist_right']
#     R = data['R']
#     T = data['T']
#     E = data['E']
#     F = data['F']
#
# # 設置視差計算的參數
# window_size = 5
# min_disp = 0
# num_disp = 128 - min_disp
# stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
#                                numDisparities=num_disp,
#                                blockSize=window_size,
#                                uniquenessRatio=10,
#                                speckleWindowSize=100,
#                                speckleRange=32,
#                                disp12MaxDiff=1,
#                                P1=8 * 3 * window_size ** 2,
#                                P2=32 * 3 * window_size ** 2)

while True:
    # 讀取左右兩張影像
    ret_left, left_image = left_camera.read()
    ret_right, right_image = right_camera.read()

    # if ret_left and ret_right:
    #     # 校正左右影像
    #     map1, map2 = cv2.initUndistortRectifyMap(mtx_left, dist_left, R, mtx_left, left_image.shape[:2], cv2.CV_16SC2)
    #     left_image = cv2.remap(left_image, map1, map2, cv2.INTER_LINEAR)
    #
    #     map1, map2 = cv2.initUndistortRectifyMap(mtx_right, dist_right, R, mtx_right, right_image.shape[:2],
    #                                              cv2.CV_16SC2)
    #     right_image = cv2.remap(right_image, map1, map2, cv2.INTER_LINEAR)
    #
    #     # 計算視差
    #     disparity = stereo.compute(cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY),
    #                                cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY))
    #
    #     # 轉換為三維點雲
    #     points_3d = cv2.reprojectImageTo3D(disparity, Q)

        # 顯示影像
    cv2.imshow('left', left_image)
    cv2.imshow('right', right_image)
    if cv2.waitKey(1) == ord('q'):
        break
    # else:
    #     break

# 關閉相機與視窗
left_camera.release()
right_camera.release()
cv2.destroyAllWindows()