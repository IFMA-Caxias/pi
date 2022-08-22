import cv2

capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

if not capture.isOpened():
    print("Erro ao abrir o arquivo")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            cv2.imshow('Original', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            canny = cv2.Canny(frame,100,200)
            cv2.imshow('Canny', canny)
            
            k = cv2.waitKey(20)
            if k == 27:  # esc
                break
        else:
            break

capture.release()
cv2.destroyAllWindows()