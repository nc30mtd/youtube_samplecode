import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

DEVICE_ID = 0
font = cv2.FONT_HERSHEY_SIMPLEX

def detect_and_read_pyzbar(frame):
    # デコード
    value = decode(frame, symbols=[ZBarSymbol.QRCODE])

    retarray = []

    if value:
        for qrcode in value:
            # QRコード座標
            x, y, w, h = qrcode.rect

            # QRコードデータ
            dec_inf = qrcode.data.decode('utf-8')
            retarray.append(dec_inf)
            frame = cv2.putText(frame, dec_inf, (x, y-6), font, .3, (255, 0, 0), 1, cv2.LINE_AA)

            # バウンディングボックス
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
    return retarray

if __name__ == '__main__':
    # VideoCapture オブジェクトを取得します
    capture = cv2.VideoCapture(DEVICE_ID)

    while(True):
        ret, frame = capture.read()

        cv2.imshow('title', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # pyzbar読み込み
        ret = detect_and_read_pyzbar(frame)
        print(ret)

    capture.release()
    cv2.destroyAllWindows()