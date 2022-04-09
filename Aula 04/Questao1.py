import cv2
import numpy as np
import random

capture = cv2.VideoCapture(0)

def noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def reduce_noise():
    global noise_prob
    noise_prob -= 0.002

def increase_noise():
    global noise_prob
    noise_prob += 0.002

def stop_capture():
    capture.release()

noise_prob = 0.01

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:

            gray = noise(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), noise_prob)

            cv2.imshow('Cinza', gray)

            options = {
                # up arrow key
                ord('c'): increase_noise,
                # down arrow key
                84: reduce_noise,
                # Q key
                113: stop_capture
            }

            pressed_key = cv2.waitKey(20)
            if pressed_key in options.keys():
                options[pressed_key].__call__()
        else:
            break

capture.release()
cv2.destroyAllWindows()