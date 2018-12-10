#-*-coding:utf-8-*-
"""
参考
    http://b4rracud4.hatenadiary.jp/entry/20181207/1544129263
    https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html
    https://pg-chain.com/python-tkinter-entry
"""
import numpy as np

import tkinter
import tkinter.messagebox as tkmsg

import matplotlib.pyplot as plt
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_tkagg  import FigureCanvasTkAgg

from functools import partial

def quit():
       root.quit()
       root.destroy()

def DrawCanvas(canvas, ax, colors = "gray"):
    value = EditBox.get()
    if value != '':
        print(value)
        EditBox.delete(0, tkinter.END)
        ax.cla()#前の描画データの消去
        gridSize = int(value)
        gridSize = (gridSize * 2 + 1) #半区画の区切りを算出
        
        #区画の線を引く
        for i in np.array(range(gridSize)) * 90.0:
            ax.plot(np.array([i, i]), np.array([0.0, (gridSize - 1) * 90]), color=colors, linestyle="dashed")
            ax.plot(np.array([0.0, (gridSize - 1) * 90]), np.array([i, i]), color=colors, linestyle="dashed")

            #斜めの線を引く
            if (i / 90.0) % 2 == 1:
                ax.plot(np.array([0.0, i]), np.array([(gridSize - 1) * 90 - i, (gridSize - 1) * 90]), color=colors, linestyle="dashed")
                ax.plot(np.array([(gridSize - 1) * 90 - i, (gridSize - 1) * 90]), np.array([0.0, i]), color=colors, linestyle="dashed")

                ax.plot(np.array([(gridSize - 1) * 90, i]), np.array([i, (gridSize - 1) * 90]), color=colors, linestyle="dashed")
                ax.plot(np.array([i, 0.0]), np.array([0.0, i]), color=colors, linestyle="dashed")
           
        canvas.draw()  #キャンバスの描画

if __name__ == "__main__":
    try:
        #GUIの生成
        root = tkinter.Tk()
        root.title("あー、てすてす")

        #グラフの設定
        fig,ax1 = plt.subplots()
        fig.gca().set_aspect('equal', adjustable='box')#グラフ領域の調整

        #キャンバスの生成
        Canvas = FigureCanvasTkAgg(fig, master=root)
        Canvas.get_tk_widget().grid(row=0, column=0, rowspan=10)

        #テキストボックスに関する諸々の設定
        EditBox = tkinter.Entry(width=5)#テキストボックスの生成
        EditBox.grid(row=1, column=2)

        #ラベルに関する諸々の設定
        GridLabel = tkinter.Label(text="ますめ")
        GridLabel.grid(row=1, column=1)

        #ボタンに関する諸々の設定
        ReDrawButton = tkinter.Button(text="こうしん", width=15, command=partial(DrawCanvas, Canvas, ax1))#ボタンの生成
        ReDrawButton.grid(row=2, column=1, columnspan=2)#描画位置(テキトー)

        QuitButton = tkinter.Button(text="やめる", width=15, command=quit)#ボタンの生成
        QuitButton.grid(row=7, column=1, columnspan=2)#描画位置(テキトー)
        
        DrawCanvas(Canvas,ax1)
        root.mainloop()#描画し続ける
    except:
        import traceback
        traceback.print_exc()
    finally:
        pass