# This is a Dash app to show 2014-2018 the trend of each index

# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd                        # pip install pandas
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
df = pd.read_csv("/Users/seven/Downloads/All_Index_Next_Year.csv", dtype={'fips': str})
print(df.head())

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(children='')
mygraph = dcc.Graph(figure={})
col_list = df.columns.values[4:-1]
dropdown = dcc.Dropdown(options=col_list,
                        value='MEDI',  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([mygraph], width=12)
    ]),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),

], fluid=True)

# Callback allows components to interact
@app.callback(
    Output(mygraph, 'figure'),
    Output(mytitle, 'children'),
    Input(dropdown, 'value')
)
def update_graph(column_name):  # function arguments come from the component property of the Input

    print(column_name)
    print(type(column_name))
    # https://plotly.com/python/choropleth-maps/
    if column_name == 'SuicideDeathRate':
        fig = px.choropleth(data_frame=df,
                            geojson=counties,
                            locations='fips',
                            scope="usa",
                            height=600,
                            color=column_name,
                            color_continuous_scale="rainbow",
                            hover_name="county",
                            labels={column_name: column_name},
                            range_color=(0, 35),
                            animation_frame='Year')
    elif column_name == 'Suicide_Rate_Percentile':
        fig = px.choropleth(data_frame=df,
                            geojson=counties,
                            locations='fips',
                            scope="usa",
                            height=600,
                            color=column_name,
                            color_continuous_scale="rainbow",
                            hover_name="county",
                            labels={column_name: column_name},
                            range_color=(0, 0.2),
                            animation_frame='Year')
    else:
        fig = px.choropleth(data_frame=df,
                            geojson=counties,
                            locations='fips',
                            scope="usa",
                            height=600,
                            color=column_name,
                            color_continuous_scale="rainbow",
                            hover_name="county",
                            labels={column_name: column_name},
                            range_color=(0.2, 0.8),
                            animation_frame='Year')

    return fig, '# '+column_name  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8054)