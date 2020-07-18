# import pandas as pd
import numpy as np
# # np.random.seed(101)
# # mat= np.random.randint(1,101,(100,5))
# # print(mat)
# # df=pd.DataFrame(mat,columns=['f1','f2','f3','f4','label'])
# # print(df)
#
# mat1=np.random.randint(0,100,(50,4))
# df1=pd.DataFrame(data=mat1,columns=['A','B','C','D'])
# df1.to_excel('D:/ik.xlsx',index=False)


import plotly.graph_objs as go
import plotly.offline as o

np.random.seed(42)
rand_x = np.random.randint(1, 101, 100)
rand_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=rand_x, y=rand_y, mode='markers')]
layout = go.Layout(title='Hello First Plot', xaxis=dict(title='My X Axis'), yaxis=dict(title='My Y Axis'),
                   hovermode='closest')
fig = go.Figure(data=data, layout=layout)
o.plot(fig, filename='scatter.html')
