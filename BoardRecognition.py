from math import atan2

import cv2
import numpy as np

from utils.ReferenceImages import loadReferenceImages

GREEN = 60
SENSITIVITY = 20

LOWER_GREEN = np.array([GREEN - SENSITIVITY, 100, 100])
UPPER_GREEN = np.array([GREEN + SENSITIVITY, 255, 255])
LOWER_RED_0 = np.array([0, 100, 100])
UPPER_RED_0 = np.array([SENSITIVITY, 255, 255])
LOWER_RED_1 = np.array([180 - SENSITIVITY, 100, 100])
UPPER_RED_1 = np.array([180, 255, 255])


SEGMENT_COUNT = 49


def _lineIntersect(line_1, line_2):
    p0_x, p0_y, p1_x, p1_y = line_1[0]
    p2_x, p2_y, p3_x, p3_y = line_2[0]

    s1_x = p1_x - p0_x
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x
    s2_y = p3_y - p2_y
    s3 = (-s2_x * s1_y + s1_x * s2_y)

    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / s3
    t = (s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / s3

    if (0 <= s <= 1 and 0 <= t <= 1):
        i_x = p0_x + (t * s1_x)
        i_y = p0_y + (t * s1_y)

        return (int(i_x), int(i_y))

    return


def _findSegments(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(
        gray, 125, 255, cv2.THRESH_BINARY * cv2.THRESH_OTSU)
    canny = cv2.Canny(thresh, 180, 255)
    # lines = cv2.HoughLines(canny, 0.5, np.pi / 45, 100)
    lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 200,
                            minLineLength=400, maxLineGap=100)
    line_1 = lines[0]
    line_2 = lines[-1]
    interscect = _lineIntersect(line_1, line_2)

    print(interscect)
    if interscect:
        cv2.circle(img, interscect, 3, (0, 255, 0), 1)

    x1, y1, x2, y2 = line_1[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1, cv2.LINE_AA)
    x1, y1, x2, y2 = line_2[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1, cv2.LINE_AA)

    return img


def _getCentroid(contour):
    M = cv2.moments(contour)
    M0 = M['m00']

    if M0 == 0.0:
        return (0, 0)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    return (cx, cy)


def _getGreeAndRedMask(img):
    black = np.ones(img.shape, np.uint8)
    working_copy = img.copy()
    hsv = cv2.cvtColor(working_copy, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv, LOWER_GREEN, UPPER_GREEN)
    red_mask_1 = cv2.inRange(hsv, LOWER_RED_0, UPPER_RED_0)
    red_mask_2 = cv2.inRange(hsv, LOWER_RED_1, UPPER_RED_1)
    red_mask = cv2.bitwise_or(red_mask_1, red_mask_2)
    _, green_contours, _ = cv2.findContours(
        green_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    _, red_contours, _ = cv2.findContours(
        red_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    green = cv2.drawContours(black, green_contours, -1,
                             (255, 255, 255), cv2.FILLED, cv2.LINE_AA)
    red = cv2.drawContours(black, red_contours, -1,
                           (255, 255, 255), cv2.FILLED, cv2.LINE_AA)

    return green, red


def _splitImage(img):
    red = img[:, :, 2]
    green = img[:, :, 1]
    blue = img[:, :, 0]
    channels = []
    for values, channel in zip((red, green, blue), (2, 1, 0)):
        image = np.zeros((values.shape[0], values.shape[1], 3),
                         dtype=values.dtype)
        image[:, :, channel] = values
        channels.append(image)

    return channels[0], channels[1]


def _findBoundary(mask):
    ellipseNotFound = True
    kernel = np.ones((4, 4), np.uint8)
    morph = cv2.Canny(mask, 125, 255)
    while (ellipseNotFound):
        _, contours, _ = cv2.findContours(
            morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if len(contour) > 4:
                area = cv2.contourArea(contour)
                if area > 155000 < area:  # threshold important make accessable
                    ellipse = cv2.fitEllipse(contour)
                    ellipseNotFound = False
                    break
        morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)

    return contour, ellipse


def _getMainZones(ellipse):
    black = np.ones(img2.shape, np.uint8)
    score_zone_ellipse = cv2.ellipse(black, ellipse, (255, 255, 255),
                                     cv2.FILLED,
                                     cv2.LINE_AA)  # mask of boards actual score zone
    _, score_zone = cv2.threshold(
        score_zone_ellipse, 127, 255, cv2.THRESH_BINARY)
    no_score_zone = 255 - score_zone  # mask of no score zone

    return score_zone, no_score_zone


def _finishZones(score_zone, green_red_mask):
    cropped_mask = cv2.bitwise_and(green_red_mask, score_zone)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
    morphed_mask = cv2.morphologyEx(cropped_mask, cv2.MORPH_CLOSE, kernel)
    rings = cv2.Canny(morphed_mask, 125, 255, cv2.THRESH_BINARY)
    _, ring_contours, _ = cv2.findContours(
        rings, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    ellipses = []
    black = np.ones(score_zone.shape, np.uint8)

    for contour in ring_contours:
        ellipse = cv2.fitEllipse(contour)
        ellipses.append(ellipse)

    multi_2 = cv2.ellipse(
        black.copy(), ellipses[0], (255, 255, 255), cv2.FILLED, cv2.LINE_AA)
    multi_2 = cv2.ellipse(
        multi_2, ellipses[2], (0, 0, 0), cv2.FILLED, cv2.LINE_AA)

    multi_3 = cv2.ellipse(
        black.copy(), ellipses[4], (255, 255, 255), cv2.FILLED, cv2.LINE_AA)
    multi_3 = cv2.ellipse(
        multi_3, ellipses[6], (0, 0, 0), cv2.FILLED, cv2.LINE_AA)

    single_bull = cv2.ellipse(
        black.copy(), ellipses[8], (255, 255, 255), cv2.FILLED, cv2.LINE_AA)

    cropped_mask = cv2.bitwise_and(green_red_mask, single_bull)
    bull = cv2.Canny(cropped_mask, 125, 255, cv2.THRESH_BINARY)
    _, bull_contours, _ = cv2.findContours(
        bull, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bull_ellipse = cv2.fitEllipse(bull_contours[-1])
    double_bull = cv2.ellipse(
        black.copy(), bull_ellipse, (255, 255, 255), cv2.FILLED, cv2.LINE_AA)

    single = score_zone.copy()
    single = cv2.bitwise_xor(single, multi_2)
    single = cv2.bitwise_xor(single, multi_3)
    single = cv2.bitwise_xor(single, single_bull)

    single_bull = cv2.bitwise_xor(double_bull, single_bull)
    return single, multi_2, multi_3, single_bull, double_bull


def kickoff(img1, im2):
    blur = cv2.GaussianBlur(img1, (5, 5), 0)
    red, green = _splitImage(blur)  # split image in RGB channels
    green_red = cv2.bitwise_or(red, green)  # combine RG channels
    green_mask, red_mask = _getGreeAndRedMask(
        green_red)  # create mask of combined channels
    green_red_mask = cv2.bitwise_or(red_mask, green_mask)  # combine masks
    # find outer ellipse of board w/o numbers
    _, ellipse = _findBoundary(green_red_mask)
    score_zone, no_score_zone = _getMainZones(ellipse)

    single, multi_2, multi_3, single_bull, double_bull = _finishZones(
        score_zone, green_red_mask)
    stack1 = np.hstack((no_score_zone, single, multi_2))
    stack2 = np.hstack((multi_3, single_bull, double_bull))
    stack3 = np.vstack((stack1, stack2))

    segments = _findSegments(blur)

    cv2.imshow('Org', segments)

    # cv2.imshow('Thresh', thresh)
    # cv2.imshow('Mask', test)

    while(1):
        kill = cv2.waitKey(1) & 0xFF

        if kill == 13 or kill == 27:
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    img1, img2 = loadReferenceImages()
    kickoff(img1, img2)
