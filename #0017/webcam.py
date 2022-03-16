import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

# DEVICE_IDを変更するとカメラの切り替えができる
# わからない場合は-1を指定しておく
DEVICE_ID = 0 
font = cv2.FONT_HERSHEY_SIMPLEX

if __name__ == '__main__':
    capture = cv2.VideoCapture(DEVICE_ID)

    while(True):
        ret, frame = capture.read()

        cv2.imshow('title', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()