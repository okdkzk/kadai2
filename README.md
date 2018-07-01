# kadai2
実装の内容
cv2.createTrackbarでトラックバーを作成
今回はgamma,red,green,blue,on or off(フィルタのオンオフ),を採用
cv2.getTrackbarPosでトラックバーの値を変更するごとに画像を生成
ガウシアンフィルタを適用する際のkernelを生成
R = frame[:,:,2]
G = frame[:,:,1]
B = frame[:,:,0]と置き、
RGBそれぞれの値を255で割る
RGBそれぞれをガンマ変換
また、Rはr、Gはg、Bはbの値が大きくなるほどR,G,Bのそれぞれの色が強調されるように設定

on or offバーで値が1の時、ガウシアンフィルタがかかるように設定

使い方
ターミナルを開き、python.kadai2.pyと打ち込むことでフレームが出てくるので、表示されているバーを動かすことで実装された内容がわかる.

参考にしたサイト
https://algorithm.joho.info/programming/python/opencv-gaussian-filter-py/
主にソースコード方法１を参考

動画のリンク
https://youtu.be/iJb8oWanLdc
