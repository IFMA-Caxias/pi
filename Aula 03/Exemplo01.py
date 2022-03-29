import cv2
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("WIDTH: '{}'".format(frame_width))
print("HEIGHT : '{}'".format(frame_height))

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            cv2.imshow('Input', frame)
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            cv2.imshow('Cinza', gray)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            if cv2.waitKey(20) & 0xFF == ord('w'):
                print("Salvando frame...")
                cv2.imwrite('print.jpg',frame)
                cv2.imwrite('gray.jpg',gray)
        else: break

capture.release()
cv2.destroyAllWindows()
