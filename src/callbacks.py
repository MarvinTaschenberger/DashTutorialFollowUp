import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="my-id", value="initial value", type="text"),
    html.Div(id="my-div"),

    dcc.Graph(id="graph-with-slider"),
    dcc.Slider(
        id="year-slider",
        min=df.year.min(),
        max=df.year.max(),
        value=df.year.min(),
        step=5,
        marks={str(year):str(year) for year in df.year.unique()
               }
        ),
    html.Br(),
    html.Label("X-Scale"),
    dcc.RadioItems(
        id="scale-radio",
        options=[{"label": "Linear", "value": "linear"},
                 {"label": "Log", "value": "log"}],
        value="Log",
        labelStyle={"display":"inline-block"}
        )
    ])
@app.callback(
    Output("graph-with-slider","figure"),
    [Input("year-slider", "value"),
     Input("scale-radio", "value")]
    )
def update_figure(selected_year, scale):
    filtered_df = df[df.year == selected_year]
    traces = list()
    for i in filtered_df.continent.unique():
        sub_df = filtered_df[filtered_df.continent == i ]
        traces.append(go.Scatter(
            x=sub_df.gdpPercap,
            y=sub_df.lifeExp,
            text=sub_df.country,
            mode="markers",
            opacity=0.7,
            marker={
                "size":15,
                "line": {"width":0.5, "color":"white"}
                },
            name=i
            ))
    return {
        "data":traces,
        "layout": go.Layout(
            xaxis={"type":scale.lower(), "title":"GDP per Capita"},
            yaxis={"title":"Life Expectancy", "range":[20,90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode="closest"
            )
        }

@app.callback(
    Output(component_id="my-div", component_property="children"),
    [Input(component_id="my-id", component_property="value")]
    )
def update_output(input_value):
    return f"You have entered {input_value}!"

if __name__ == "__main__":
    app.run_server(debug=True)