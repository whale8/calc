import numpy as np
import pandas as pd


#-----------------check test---------------------
numpy_data = np.array([0.123456, 0.654321, 0.987654321])

# numpy配列をPandasのDataFrameに変換
panda_data = pd.DataFrame(numpy_data)

# 有効数字3桁で丸める
panda_data = panda_data.round(3)

# 必要な場合は， Numpy形式に戻す
numpy_data2 = np.array(panda_data.values)

print(numpy_data2) #--> [0.123, 0.654, 0.988]
