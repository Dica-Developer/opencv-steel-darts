import cv2
import numpy as np
from skimage.measure import compare_ssim
import imutils
from time import sleep

from darts_ui.darts_recognition.Calibration import getCalibrationData

cap = cv2.VideoCapture('./darts_ui/darts_recognition/test_images/output.mkv')
cap.set(cv2.CAP_PROP_FPS, 10)

circle_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (32, 32))


def testBGSubtractor():
    fgbg = cv2.createBackgroundSubtractorMOG2(history=50, detectShadows=True, varThreshold=64)
    # fgbg = cv2.createBackgroundSubtractorKNN(history=100, dist2Threshold=600, detectShadows=True)
    # fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    cal_data_l, cal_data_r = getCalibrationData()
    dst_points = np.array(cal_data_l.points, np.float32)
    src_points_l = np.array(cal_data_l.transformation_matrix, np.float32)
    src_points_r = np.array(cal_data_r.transformation_matrix, np.float32)
    matrix_l = cv2.getPerspectiveTransform(src_points_l, dst_points)
    while(cap.isOpened()):
        _, frame = cap.read()
        frame = cv2.warpPerspective(frame, matrix_l, (800, 800))
        blur = cv2.GaussianBlur(frame, (3, 3), 0, 0)
        mask = fgbg.apply(blur)

        _, thresh = cv2.threshold(mask, 200, 255, cv2.THRESH_TOZERO)
        dilated = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, circle_kernel)
        _, contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if 1000 < area < 50000:
                '''
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(frame, [contour], 0, (0, 255, 0), 1)
                cv2.drawContours(frame, [box], 0, (255, 255, 0), 1)
                _, cols = frame.shape[:2]
                [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
                lefty = int((-x*vy/vx) + y)
                righty = int(((cols-x)*vy/vx)+y)
                cv2.line(frame, (cols-1, righty), (0, lefty), (0, 255, 255), 1)
                ellipse = cv2.fitEllipse(contour)
                cv2.ellipse(frame, ellipse, (255, 0, 255), 1)

                extRight = tuple(contour[contour[:, :, 0].argmax()][0])
                extTop = tuple(contour[contour[:, :, 1].argmin()][0])
                extBot = tuple(contour[contour[:, :, 1].argmax()][0])

                # cv2.circle(frame, extLeft, 8, (0, 0, 255), -1)
                # cv2.circle(frame, extTop, 8, (255, 0, 0), -1)
                # cv2.circle(frame, extBot, 8, (255, 255, 0), -1)
                '''
                extLeft = tuple(contour[contour[:, :, 0].argmin()][0])
                cv2.circle(frame, extLeft, 5, (0, 255, 0), cv2.FILLED)


        cv2.imshow('frame', frame)
        cv2.imshow('features', dilated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    testBGSubtractor()
