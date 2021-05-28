import dash
import dash_core_components as dcc
from dash_core_components.Graph import Graph
import dash_html_components as html
from dash.dependencies import Output, Input
from future.utils import with_metaclass
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime

""" start=datetime.datetime(2020,1,1)
end = datetime.date(2020,12,3)
df = web.DataReader(['AMZN','GOOGL','FB','PFE','BNTX','MRNA'],
                    'stooq',start=start,end=end)

df=df.stack().reset_index()
df.to_csv('mystocks.csv',index=False) """    

df= pd.read_csv('mystocks.csv')

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout section : Bootstrap
# --------------------------------------------------------

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Stock Market Dashboard',
                        className='text-center text-primary, mb-4'),
                width=12)        
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='my-dropdown',multi=False,value='AMZN',
                        options=[{'label':x,'value':x} 
                        for x in sorted(df['Symbols'].unique())]),
            dcc.Graph(id='line-fig')
                
        ],width={'size':6,'offset':0, 'order':1}),#size of columns, ofset is how many columns from the left de object starts, order is which object shows first
        
         
        dbc.Col([
            dcc.Dropdown(id='my-dropdown2',multi=False,value='AMZN',
                        options=[{'label':x,'value':x} 
                        for x in sorted(df['Symbols'].unique())]),
            dcc.Graph(id='line-fig2')
                
        ],width={'size':6,'offset':0, 'order':2})
        
    ],no_gutters=False,justify='around'), # no_gutters False make a space between de columns,
                                          # justify: start,center,end,between, around

    dbc.Row([

    ]),

])


if __name__ == '__main__':
    app.run_server(debug=True,port=3000)