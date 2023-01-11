# This is a sample Python script.

import plotly.express as px
import pandas as pd                        # pip install pandas

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
df = pd.read_csv("/Users/seven/Downloads/All_Index_Next_Year.csv", dtype={'fips': str})
print(df.head())

fig1 = px.choropleth(data_frame=df,
                     geojson=counties,
                     locations='fips',
                     scope="usa",
                     height=200,
                     color='SVI',
                     color_continuous_scale="rainbow",
                     hover_name="county",
                     labels={'SVI': 'SVI'},
                     range_color=(0.2, 0.8))
fig1.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig2 = px.choropleth(data_frame=df,
                     geojson=counties,
                     locations='fips',
                     scope="usa",
                     height=200,
                     color='MEDI',
                     color_continuous_scale="rainbow",
                     hover_name="county",
                     labels={'MEDI': 'MEDI'},
                     range_color=(0.2, 0.8))
fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig3 = px.choropleth(data_frame=df,
                     geojson=counties,
                     locations='fips',
                     scope="usa",
                     height=200,
                     color='MEDI + SVI',
                     color_continuous_scale="rainbow",
                     hover_name="county",
                     labels={'MEDI + SVI': 'MEDI + SVI'},
                     range_color=(0.2, 0.8))
fig3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig4 = px.choropleth(data_frame=df,
                     geojson=counties,
                     locations='fips',
                     scope="usa",
                     height=200,
                     color='SEDI',
                     color_continuous_scale="rainbow",
                     hover_name="county",
                     labels={'SEDI': 'SEDI'},
                     range_color=(0.2, 0.8))
fig4.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig5 = px.choropleth(data_frame=df,
                     geojson=counties,
                     locations='fips',
                     scope="usa",
                     height=200,
                     color='MEDI + SEDI',
                     color_continuous_scale="rainbow",
                     hover_name="county",
                     labels={'MEDI + SEDI': 'MEDI + SEDI'},
                     range_color=(0.2, 0.8))
fig5.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig6 = px.choropleth(data_frame=df,
                     geojson=counties,
                     locations='fips',
                     scope="usa",
                     height=200,
                     color='SuicideDeathRate',
                     color_continuous_scale="rainbow",
                     hover_name="county",
                     labels={'SuicideDeathRate': 'SuicideDeathRate'},
                     range_color=(0, 35))
fig6.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(children='Year', style={'fontSize': "24px"}, className='menu-title'),
                dcc.Dropdown(
                    id='year-filter',
                    options=[
                        {'label': Year, 'value':  Year}
                        for Year in df.Year.unique()
                    ],
                    value='2016',
                    clearable=False,
                    searchable=False,
                    className='dropdown', style={'fontSize': "24px", 'textAlign': 'center'},
                ),
            ],
            className='menu',
        ), #the dropdown function

        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id='choropleth1',
                        figure=fig1,
                    ),
                    style={'width': '50%', 'display': 'inline-block'},
                ),
                html.Div(
                    children=dcc.Graph(
                        id='choropleth2',
                        figure=fig2,
                    ),
                    style={'width': '50%', 'display': 'inline-block'},
                ),
                html.Div(
                    children=dcc.Graph(
                        id='choropleth3',
                        figure=fig3,
                    ),
                    style={'width': '50%', 'display': 'inline-block'},
                ),
                html.Div(
                    children=dcc.Graph(
                        id='choropleth4',
                        figure=fig4,
                    ),
                    style={'width': '50%', 'display': 'inline-block'},
                ),
                html.Div(
                    children=dcc.Graph(
                        id='choropleth5',
                        figure=fig5,
                    ),
                    style={'width': '50%', 'display': 'inline-block'},
                ),
                html.Div(
                    children=dcc.Graph(
                        id='choropleth6',
                        figure=fig6,
                    ),
                    style={'width': '50%', 'display': 'inline-block'},
                ),

            ],
            className='double-graph',
        ),
    ]
)  # Six graphs


@app.callback(
    Output("choropleth1", "figure"),
    [Input("year-filter", "value")],
)
def update_charts(Year):
    filtered_data = df[df["Year"] == Year]

    choropleth1 = px.choropleth(data_frame= filtered_data,
                                geojson=counties,
                                locations='fips',
                                scope="usa",
                                height=200,
                                color='SVI',
                                color_continuous_scale="rainbow",
                                hover_name="county",
                                labels={'SVI': 'SVI'},
                                range_color=(0.2, 0.8))
    choropleth1.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return choropleth1

@app.callback(
    Output("choropleth2", "figure"),
    [Input("year-filter", "value")],
)
def update_charts(Year):
    filtered_data = df[df["Year"] == Year]

    choropleth2 = px.choropleth(data_frame=filtered_data,
                                geojson=counties,
                                locations='fips',
                                scope="usa",
                                height=200,
                                color='MEDI',
                                color_continuous_scale="rainbow",
                                hover_name="county",
                                labels={'MEDI': 'MEDI'},
                                range_color=(0.2, 0.8))
    choropleth2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return choropleth2

@app.callback(
    Output("choropleth3", "figure"),
    [Input("year-filter", "value")],
)
def update_charts(Year):
    filtered_data = df[df["Year"] == Year]

    choropleth3 = px.choropleth(data_frame=filtered_data,
                                geojson=counties,
                                locations='fips',
                                scope="usa",
                                height=200,
                                color='MEDI + SVI',
                                color_continuous_scale="rainbow",
                                hover_name="county",
                                labels={'MEDI + SVI': 'MEDI + SVI'},
                                range_color=(0.2, 0.8))
    choropleth3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return choropleth3

@app.callback(
    Output("choropleth4", "figure"),
    [Input("year-filter", "value")],
)
def update_charts(Year):
    filtered_data = df[df["Year"] == Year]

    choropleth4 = px.choropleth(data_frame=filtered_data,
                                geojson=counties,
                                locations='fips',
                                scope="usa",
                                height=200,
                                color='SEDI',
                                color_continuous_scale="rainbow",
                                hover_name="county",
                                labels={'SEDI': 'SEDI'},
                                range_color=(0.2, 0.8))
    choropleth4.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return choropleth4

@app.callback(
    Output("choropleth5", "figure"),
    [Input("year-filter", "value")],
)
def update_charts(Year):
    filtered_data = df[df["Year"] == Year]

    choropleth5 = px.choropleth(data_frame=filtered_data,
                                geojson=counties,
                                locations='fips',
                                scope="usa",
                                height=200,
                                color='MEDI + SEDI',
                                color_continuous_scale="rainbow",
                                hover_name="county",
                                labels={'MEDI + SEDI': 'MEDI + SEDI'},
                                range_color=(0.2, 0.8))
    choropleth5.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return choropleth5

@app.callback(
    Output("choropleth6", "figure"),
    [Input("year-filter", "value")],
)
def update_charts(Year):
    filtered_data = df[df["Year"] == Year]

    choropleth6 = px.choropleth(data_frame=filtered_data,
                                geojson=counties,
                                locations='fips',
                                scope="usa",
                                height=200,
                                color='SuicideDeathRate',
                                color_continuous_scale="rainbow",
                                hover_name="county",
                                labels={'SuicideDeathRate': 'SuicideDeathRate'},
                                range_color=(0, 35))
    choropleth6.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return choropleth6

# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8080)
