# Run this app with `python app.py` and
# visit http://localhost:8000/ in your web browser.

import dash 
# dash.html : used to generate html components for the web application. dcc :  used for high level interactive components using react.js
from dash import dcc, html
# pandas : data analysis tool
import pandas as pd
# plotly express : module to create entire figures at once
import plotly.express as px
from dash.dependencies import Input, Output

#initialize application
app = dash.Dash(__name__)
#set dashboard title
app.title='CCA'
#html+css layout of the dashboard
app.layout = html.Div([ 
    html.Div([
        html.Div([
            html.H1("Cryptocurrency Chart Analysis", className='title'),
            html.H2("Select a coin"), 
            #dash dropdown for selecting coins
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
                value='Bitcoin',  #default value for dropdown menu
                className='dropdown-list'          
            )
        ],
        className='text-display'),
        #dash graph for displaying dataset 
        html.Div([
            dcc.Graph(id="coin-vs-date",    
            config={
                'scrollZoom': True,         # allow scroll zoom on graph
                'doubleClick':'reset',      # double click on graph to reset
                }
            ),
            html.Div([
                dcc.RangeSlider(            # range slider element to set graph's time period
                    id='year_chosen',       # function identifier
                    marks={                 # marks on slider           
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
                    min=2013,               # minimum mark
                    max=2022,               # maximum mark
                    value=[2021, 2022],     # default mark period
                ),
            ])
        ], 
        className='graph-display'),
    ],
    className='app',
    ),
    html.Div([
        html.Label('© 2021 : PrXfy', className='footer')    #unnecessary footer
    ])
])

colors = {"background":"#E5ECF6", "text": "#636EFA"}

# dash decorator to call function when input changes to update output
@app.callback(                               
    Output('coin-vs-date', 'figure'),       # graph output 
    [
        Input('coin-dropdown', 'value'),    # select coin from dropdown
        Input('year_chosen', 'value')       # select year range through slider
    ]
)

# function to update graph when dashboard input changes 
def update_figure(selected_coin, year_chosen):
    # when coin is selected, load its dataset, otherwise default to bitcoin dataset if no option is selected.
    if selected_coin:
        filename = 'coin_'+selected_coin+'.csv'
        data = pd.read_csv(filename)
    else:
        data = pd.read_csv('coin_Bitcoin.csv')

    # adjust date format of dataset
    data['Date'] = pd.to_datetime(data['Date'])     
    # create a year column from the date column
    data['Year'] = data['Date'].dt.year   
    # replace the existing dataset index with year index          
    data.set_index=('Year')
    # filter the dataset as per the range selected from the range slider element
    data=data[(data['Year']>=year_chosen[0])&(data['Year']<=year_chosen[1])]

    # create a plotly express line graph of the filtered dataset
    fig = px.line(
    data,
    title = f'{selected_coin} Price Chart',     # title of the chart
    x='Date',       # x axis column
    y='High',       # y axis column
    labels = {
        'High': 'Price'     # rename graph label
        }
    )

    #customize layout of the graph
    fig.update_layout(
        paper_bgcolor=colors["background"],
        font_color=colors["text"]
    )
    #update graph with changes
    return fig

#run application 
if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8000)
