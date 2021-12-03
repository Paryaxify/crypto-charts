import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.title='CCA'

app.layout = html.Div([ 
    html.Div([
        html.Div([
            html.H1("Cryptocurrency Chart Analysis", className='title'),
            html.H2("Select a coin"), 
            dcc.Dropdown(
                id='coin-dropdown',
                options=[
                    {'label': 'Aave', 'value': 'Aave'},
                    {'label': 'BinanceCoin', 'value': 'BinanceCoin'},
                    {'label': 'Bitcoin', 'value': 'Bitcoin'},
                    {'label': 'Cardano', 'value': 'Cardano'},
                    {'label': 'ChainLink', 'value': 'ChainLink'},
                    {'label': 'Dogecoin', 'value': 'Dogecoin'},
                    {'label': 'Ethereum', 'value': 'Ethereum'},
                    {'label': 'Monero', 'value': 'Monero'},
                    {'label': 'Solana', 'value': 'Solana'},
                    {'label': 'Stellar', 'value': 'Stellar'},
                    {'label': 'Tether', 'value': 'Tether'},
                ],
                value='Bitcoin', 
                className='dropdown-list'          
            )
        ],
        className='text-display'),
        html.Div([
            dcc.Graph(id="coin-vs-date", 
            config={
                'scrollZoom': True,
                'doubleClick':'reset',
                }
            ),
            html.Div([
                dcc.RangeSlider(
                    id='year_chosen',
                    marks={
                        2013: '2013',
                        2014: '2014',
                        2015: '2015',
                        2016: '2016',
                        2017: '2017',
                        2018: '2018',
                        2019: '2019',                                        
                        2020: '2020',
                        2021: '2021',
                        2022: '2022',
                    },
                    min=2013,
                    max=2022,
                    value=[2021, 2022],
                ),
            ])
        ], 
        className='graph-display'),
    ],
    className='app',
    ),
    html.Div([
        html.Label('© 2021 : PrXfy', className='footer')
    ])
])

colors = {"background":"#E5ECF6", "text": "#636EFA"}

@app.callback(
    Output('coin-vs-date', 'figure'),
    [
        Input('coin-dropdown', 'value'),
        Input('year_chosen', 'value')
    ]
)

def update_figure(selected_coin, year_chosen):
    if selected_coin:
        filename = 'coin_'+selected_coin+'.csv'
        data = pd.read_csv(filename)
    else:
        data = pd.read_csv('coin_Bitcoin.csv')
        
    data['Date'] = pd.to_datetime(data['Date'])
    data['Year'] = data['Date'].dt.year
    data.set_index=('Year')

    data=data[(data['Year']>=year_chosen[0])&(data['Year']<=year_chosen[1])]

    fig = px.line(
    data,
    title = f'{selected_coin} Price Chart',
    x='Date',
    y='High',
    labels = {
        'High': 'Price'
        }
    )
    fig.update_layout(
        paper_bgcolor=colors["background"],
        font_color=colors["text"]
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8000)
