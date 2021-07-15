
import numpy as np  #opencvを使用するのに必要
import cv2  #画像を扱う
import glob #多分いらない
from PIL import Image, ImageTk  #cv2の画像をtkinterで使用するための仲介役
import tkinter as tk    #GUI関連

f=open(input("ファイルのパスを入力："))

#ファイルからデータ(画像以外)を読み込む
magic_num=f.readline()
_,w,h=f.readline().split()
_,selectable=f.readline().split()
_,rate_select,rate_move=f.readline().split()
pixel_w,pixel_h=f.readline().split()
rgb_max=f.readline()

#文字列から数字に変換
w=int(w)
h=int(h)
selectable=int(selectable)
rate_select=int(rate_select)
rate_move=int(rate_move)
pixel_w=int(pixel_w)
pixel_h=int(pixel_h)
rgb_max=int(rgb_max)

#base:正方形の一辺の長さ
base=pixel_w//w

#cv2の画像を格納する
img=[[[[]for k in range(base)]for j in range(w)]for i in range(h)]

#画像データ読み込み
for i in range(pixel_h):
    for j in range(pixel_w):
        img[i//base][j//base][i%base].append(list(map(int,f.readline().split())))

f.close()

#画像として扱えるようにする
img=np.array(img)
img=img.astype(np.uint8)

cv2.imshow(img) #画像を表示
cv2.waitKey()   #キー入力を待つ
cv2.destroyAllWindows() #ウィンドウを消去


#
#以下guiとかいろいろ
#



root=tk.Tk()    #メインウィンドウを作成,表示

canvas=tk.Canvas(root,width=pixel_w+200,height=pixel_h,bg="white") #キャンバスを作成
canvas.pack()   #キャンバスをメインウィンドウの中に表示

tkimg=[[[]for j in range(w)]for i in range(h)]  #画像を格納するリスト
#問題で与えられた時の画像から回転させた角度と位置を記憶しておく←画像復元のプログラムをこのソリューションに書くのか書かないのか要相談

#opencvの画像をtkinterで使用可能なように変換する
for i in range(h):
    for j in range(w):
        tkimg[i][j].append(ImageTk.PhotoImage(Image.fromarray(img[i][j])))
        tkimg[i][j].append([i,j])
        tkimg[i][j].append(0)

# tkimg[y][x][0] : 画像
# tkimg[y][x][1] : 問題で与えられた時のその画像の位置[y座標,x座標]
# tkimg[y][x][2] : 問題で与えられてから回転させた角度/90

#キャンバスに画像を表示する
for i in range(h):
    for j in range(w):
        canvas.create_image(j*base,i*base,image=tkimg[i][j][0],anchor='nw')



root.mainloop() #上記のguiの処理を繰り返す(これがないとウィンドウが表示され続けない)
#変更の検証