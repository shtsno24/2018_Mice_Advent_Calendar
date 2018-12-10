#-*-coding:utf-8-*-
"""
参考
    http://b4rracud4.hatenadiary.jp/entry/20181207/1544129263
    https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html
"""

import numpy as np
import tkinter
import matplotlib.pyplot as plt
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_tkagg  import FigureCanvasTkAgg

gridSize = 2 #マスの数を指定

if __name__ == "__main__":
    try:
        #GUIの生成
        root = tkinter.Tk()
        root.title("にゃーん")

        #グラフの設定
        fig,ax = plt.subplots()
        fig.gca().set_aspect('equal', adjustable='box')#グラフ領域の調整
        gridSize = (gridSize * 2 + 1) #半区画の区切りを算出t

        #キャンバスの生成
        Canvas = FigureCanvasTkAgg(fig, master=root)
        Canvas.get_tk_widget().grid(row=0, column=0, rowspan=10)

        #区画の線を引く
        for i in np.array(range(gridSize)) * 90.0:
            ax.plot(np.array([i, i]), np.array([0.0, (gridSize - 1) * 90]), color="gray", linestyle="dashed")
            ax.plot(np.array([0.0, (gridSize - 1) * 90]), np.array([i, i]), color="gray", linestyle="dashed")

            #斜めの線を引く
            if (i / 90.0) % 2 == 1:
                ax.plot(np.array([0.0, i]), np.array([(gridSize - 1) * 90 - i, (gridSize - 1) * 90]), color="gray", linestyle="dashed")
                ax.plot(np.array([(gridSize - 1) * 90 - i, (gridSize - 1) * 90]), np.array([0.0, i]), color="gray", linestyle="dashed")

                ax.plot(np.array([(gridSize - 1) * 90, i]), np.array([i, (gridSize - 1) * 90]), color="gray", linestyle="dashed")
                ax.plot(np.array([i, 0.0]), np.array([0.0, i]), color="gray", linestyle="dashed")
        
        Canvas.draw()  #キャンバスの描画
        root.mainloop()#描画し続ける
    except:
        import traceback
        traceback.print_exc()
    finally:
        input(">>")
