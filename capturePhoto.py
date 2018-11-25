import cv2
from PIL import Image
from pyzbar.pyzbar import decode


video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("qrcode.jpg",frame);
        break


video_capture.release()
cv2.destroyAllWindows()

data=decode(Image.open('./qrcode.jpg'))
print(data);
