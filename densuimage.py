import cv2
import numpy as np

# 画像の読み込み
img1 = cv2.imread('画像1.jpg', 0)
img2 = cv2.imread('画像2.jpg', 0)

# 画像の前処理
threshold1, img1_bin = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
threshold2, img2_bin = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)

# 輪郭抽出
contours1, hierarchy1 = cv2.findContours(img1_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv2.findContours(img2_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 各輪郭について処理
for cnt1, cnt2 in zip(contours1, contours2):
    # 各輪郭から矩形を抽出
    x, y, w, h = cv2.boundingRect(cnt1)
    x2, y2, w2, h2 = cv2.boundingRect(cnt2)

    # 各輪郭からROIを取得
    roi1 = img1_bin[y:y+h, x:x+w]
    roi2 = img2_bin[y2:y2+h2, x2:x2+w2]

    # 画像間の差分を計算
    diff = cv2.absdiff(roi1, roi2)
    diff_sum = np.sum(diff)

    # 差分が閾値以下の場合はずれ度が大きいと判定
    if diff_sum <= threshold:
        print("ずれ度が大きい")
    else:
        print("ずれ度が小さい")
