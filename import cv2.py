import cv2
import numpy as np
import mido
from mido import Message, MidiFile, MidiTrack

# 画像読み込み
img1 = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

# Cannyエッジ検出
edges1 = cv2.Canny(img1, 100, 200)
edges2 = cv2.Canny(img2, 100, 200)

# ヒストグラム作成
hist1 = np.sum(edges1, axis=0)
hist2 = np.sum(edges2, axis=0)

# ずれ度抽出
slant1 = np.argmax(hist1)
slant2 = np.argmax(hist2)

# 音階決定
notes = [60, 62, 64, 65, 67, 69, 71, 72] # C Major scale
note = notes[(slant2 - slant1) % len(notes)]

# MIDI音楽生成
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))
track.append(Message('note_on', note=note, velocity=64, time=0))
track.append(Message('note_off', note=note, velocity=64, time=100))

mid.save('output.mid')
