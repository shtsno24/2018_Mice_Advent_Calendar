#-*-coding:utf-8-*-
"""
参考 http://b4rracud4.hatenadiary.jp/entry/20181207/1544129263
"""

import numpy as np
import matplotlib.pyplot as plt

gridSize = 2 #マスの数を指定

if __name__ == "__main__":
    try:
        plt.gca().set_aspect('equal', adjustable='box')
        gridSize = (gridSize * 2 + 1) #半区画の区切りを算出t


        #区画の描画
        for i in np.array(range(gridSize)) * 90.0:
            plt.plot(np.array([i, i]), np.array([0.0, (gridSize - 1) * 90]), color="gray", linestyle="dashed")
            plt.plot(np.array([0.0, (gridSize - 1) * 90]), np.array([i, i]), color="gray", linestyle="dashed")

            #斜めの線の描画
            if (i / 90.0) % 2 == 1:
                plt.plot(np.array([0.0, i]), np.array([(gridSize - 1) * 90 - i, (gridSize - 1) * 90]), color="gray", linestyle="dashed")
                plt.plot(np.array([(gridSize - 1) * 90 - i, (gridSize - 1) * 90]), np.array([0.0, i]), color="gray", linestyle="dashed")

                plt.plot(np.array([(gridSize - 1) * 90, i]), np.array([i, (gridSize - 1) * 90]), color="gray", linestyle="dashed")
                plt.plot(np.array([i, 0.0]), np.array([0.0, i]), color="gray", linestyle="dashed")
       
        plt.show()
    except:
        import traceback
        traceback.print_exc()
    finally:
        input(">>")
