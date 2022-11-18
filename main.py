# Центр контура https://www.geeksforgeeks.org/python-opencv-find-center-of-contour/

import cv2 as cv
import time
import numpy as np
from math import sqrt, pi, sin, cos, atan2

def Affine(IMage, name):
    print(f"\n{name}:")
    # Порог изображения https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
    ret, thresh = cv.threshold(IMage, 0, 255, cv.THRESH_TOZERO)

    M = cv.moments(thresh)
    xc = int(M['m10'] / M['m00'])
    yc = int(M['m01'] / M['m00'])
    print(f"x: {xc} y: {yc}")

    w, h = IMage.shape[::-1]
    B, C, D = np.float64(0), np.float64(0), np.float64(0)
    for y, line in enumerate(IMage):
        for x, T in enumerate(line):
            if T != 0:
                B += T * ((x - xc) ** 2 - (y - yc) ** 2)
                C += T * 2 * (x - xc)*(y - yc)
                D += T * ((x - xc) ** 2 + (y - yc) ** 2)
    # Alt 0181
    µ = sqrt((D + sqrt(C ** 2 + B ** 2)) / (D - sqrt(C ** 2 + B ** 2)))

    teta = 0.5 * atan2(C, B) + pi

    print("Направление (teta) сжатия изображения:  " + str("{0:.2f}".format(teta)))
    print("Величина (µ) сжатия изображения: " + str("{0:.3f}".format(µ)))

    cIM = np.zeros((w, h), dtype='uint8')
    Mdivisible, Mdivider = 0, 0
    for y, line in enumerate(IMage):
        for x, T in enumerate(line):
            if T != 0:
                xPlus, yPlus = (
                (1 / µ) * ((x - xc) * cos(-teta) - (y - yc) * sin(-teta))
                        * cos(teta) - ((x-xc) * sin(-teta) + (y-yc) * cos(-teta)) * sin(teta) ),(

                (1 / µ) * ((x - xc) * cos(-teta) - (y - yc) * sin(-teta))
                        * sin(teta) + ((x-xc) * sin(-teta) + (y-yc) * cos(-teta)) * cos(teta) )

                xZv, yZv = int(xPlus - xc), int(yPlus - yc)

                cIM[xZv][yZv] = T

                Mdivisible += T * sqrt(xPlus ** 2 + yPlus ** 2)
                Mdivider += T
    # эталонное положение
    K = 10
    # коэффициент равномерного масштабирования изображения
    M = Mdivisible / (K * Mdivider)
    scale = 1 / M
    print("Коэф. равномерного масшт. изображения (M): " + str("{0:.3f}".format(M)))

    center = (w / 2, h / 2)

    matrix = cv.getRotationMatrix2D(center, 0, scale)
    normaledIm1 = cv.warpAffine(cIM, matrix, (w, h))
    #translation https://subscription.packtpub.com/book/application-development/9781785283932/1/ch01lvl1sec11/image-translation
    xTran, yTran = centering(normaledIm1)
    translation_matrix = np.float32([[1, 0, xTran], [0, 1, yTran]])
    normaledIm = cv.warpAffine(normaledIm1, translation_matrix, (w, h))

    cv.imwrite("Result\\normaled_" + name + ".png", normaledIm)

def centering(IMage):
    ret, thresh = cv.threshold(IMage, 0, 255, cv.THRESH_TOZERO)

    M = cv.moments(thresh)
    xcen, ycen = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
    w, h = IMage.shape[::-1]
    yIMcen, xIMcen = w/2, h/2

    xFind, yFind = xIMcen - xcen,yIMcen - ycen
    print("sizewh" + str(xFind) + "    " + str(yFind))
    return xFind, yFind


if __name__ == '__main__':

    start_time = time.time()

    Affine(cv.imread("image_1_2.png", cv.IMREAD_GRAYSCALE), "image_1")
    Affine(cv.imread("image_2_2.png", cv.IMREAD_GRAYSCALE), "image_2")
    Affine(cv.imread("image_3_2.png", cv.IMREAD_GRAYSCALE), "image_3")

    print("--- Время работы: %s ---" % (time.time() - start_time))