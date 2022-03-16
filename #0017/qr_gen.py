import qrcode

if __name__ == '__main__':
    print("書き込む文字列を入力：")
    x = input()

    outqrimg = qrcode.make(str(x))
    outqrimg.save('./export_qr.png')
    print("書き出し完了")