import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.graph_objs as go
#
# app=dash.Dash()
#
# nsdq=pd.read_csv('D:/Plotly-Dashboards-with-Dash-master/Plotly-Dashboards-with-Dash-master/Data/NASDAQcompanylist.csv')
# nsdq.set_index('Symbol',inplace=True)
# options=[]
#
# for tic in nsdq.index:
#     mydict={}
#     mydict['label']=str(nsdq.loc[tic]['Name'])+' '+tic
#     mydict['value']=tic
#     options.append(mydict)


# app.layout= html.Div([
#                     html.H1('Stock Ticker Dashboard'),
#                     html.Div([html.H3('Enter a stock symbol:',style={'paddingRight':'30px'}),
#                     dcc.Dropdown(
#                         id='my_stock_picker',
#                         options=options,
#                         value=['TSLA'],
#                         multi=True,
#                         )],style={'display':'inline-block','verticalAlign':'top','width':'30%'}),
#                       html.Div([html.H3('Select start and end date:'),
#                                 dcc.DatePickerRange(id='my_date_picker',
#                                         min_date_allowed=datetime(2015,1,1),
#                                         max_date_allowed=datetime.today(),
#                                         start_date=datetime(2019,1,1),
#                                         end_date=datetime.today()
#                                         )],style={'display':'inline-block'}),
#                                         html.Div([
#                                             html.Button(id='submit-button',
#                                                         n_clicks=0,
#                                                         children='Submit',
#                                                         style={'fontSize':24,'marginLeft':'30px'}
#                                                         )
#                                         ],style={'display':'inline-block'}),
#                       dcc.Graph(id='my_graph',
#                                 figure={'data':[{'x':[1,2],'y':[3,1]}],'layout':{'title':'default title'}}
#                                 )
#                       ])
# @app.callback(Output('my_graph','figure'),[Input('submit-button','n_clicks')],[State('my_stock_picker','value'),State('my_date_picker','start_date'),State('my_date_picker','end_date')])
# def update_graph(n_clicks,stock_ticker,start_date,end_date):
#     start=datetime.strptime(start_date[:10],'%Y-%m-%d')
#     end=datetime.strptime(end_date[:10],'%Y-%m-%d')
#     traces=[]
#     for tic in stock_ticker:
#         df=web.get_data_yahoo(tic,start,end)
#         traces.append({'x': df.index , 'y': df['High'],'name':tic})
#     fig = {'data': traces , 'layout': {'title':stock_ticker}}
#     return fig


# np.random.seed(42)
# rand_x=np.random.randint(1,101,100)
# rand_y=np.random.randint(1,101,100)
#
# app.layout=html.Div([dcc.Graph(id='scatterplot',figure={'data':[go.Scatter(x=rand_x,y=rand_y,mode='markers')],'layout':go.Layout(
#                             title='My Scatterplot')}),dcc.Graph(id='scatterplot 2',figure={'data':[go.Scatter(x=rand_x,y=rand_y,mode='markers')],'layout':go.Layout(
#                             title='My Scatterplot2')})])

# if __name__ == '__main__':
#     app.run_server()
