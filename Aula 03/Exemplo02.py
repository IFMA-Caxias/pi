import cv2
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("video_cinza.avi", fourcc, int(fps), (int(frame_width), int(frame_height)), False)
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            output.write(gray)

            cv2.imshow('Cinza', gray)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            if cv2.waitKey(20) & 0xFF == ord('w'):
                print("Salvando frame...")
                cv2.imwrite('print.jpg',gray)
            
        else: break

capture.release()
output.release()
cv2.destroyAllWindows()
