import cv2, numpy as np, random, win32api

# 透過pngを黒背景に表示して読み込む
def read_alpha(filename):
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    width, height = img.shape[:2]
    bg = np.array(width*[height*[[0,0,0]]], np.float64)
    mask = img[:,:,3]
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR )
    mask = mask / 255.0
    img = img[:,:,:3]
    bg += img * mask/255 
    return bg

#画像読み込み
shorichu = read_alpha("data/shorichu_s.png")
sumi = read_alpha("data/sumi_s.png")

#画面サイズ取得
displayWidth = win32api.GetSystemMetrics(0)
displayHeight = win32api.GetSystemMetrics(1)

quitKey = {ord('q'),27} #終了キー
auto = False

while(1):
    windowX,windowY = random.randrange(0,displayWidth - shorichu.shape[1]),random.randrange(0,displayHeight - sumi.shape[0]) # ウィンドウ出現位置
    cv2.imshow("popup",shorichu)
    cv2.moveWindow("popup",windowX,windowY)
    if auto == False:
        pressedKey = cv2.waitKey(0)
        if pressedKey == ord('a'): auto = True # オートモード有効化
    else: 
        pressedKey = cv2.waitKey(80+random.randrange(80))
        if pressedKey == ord('a'): auto = False # オートモード解除
    if pressedKey in quitKey: break # qキーまたはESCキー押下でループ脱出
    cv2.imshow("popup",sumi)
    cv2.moveWindow("popup",windowX+int(shorichu.shape[1]/2 - sumi.shape[1]/2),windowY+int(shorichu.shape[0]/2 - sumi.shape[0]/2))
    cv2.waitKey(80)
    cv2.destroyWindow("popup")

# 最後は「済」を長めに表示して終了
cv2.moveWindow("popup",windowX+int(shorichu.shape[1]/2 - sumi.shape[1]/2),windowY+int(shorichu.shape[0]/2 - sumi.shape[0]/2))
cv2.imshow("popup",sumi)
cv2.waitKey(180)
cv2.destroyWindow("popup")

# 念のため
cv2.destroyAllWindows()