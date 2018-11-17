import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    "background":"#111111",
    "paper":"FF00FF",
    "text": "#7FDBFF"
    }
textStyle = {"textAligne": "center",
                   "color": colors["text"]}
app.layout = html.Div(style = { "backgroundColor": colors["background"]},children=[
    html.H1(children="Hello Dash",
            style=textStyle),
    html.Div(children=[
        """ Dash: A web application framework with python 
        based on flask and react - woot """
        ], style= textStyle),
    dcc.Graph(
        id = "example-graph",
        figure = {
            "data": [
                {"x": [1,2,3,4], "y": [4,2,2,3], "type":"bar", "name":"SF"},
                {"x": [1,2,3,4], "y": [2,5,4,3], "type":"bar", "name": "LAX"}
                ],
            "layout" : {
                "plot_bgcolor": colors["background"],
                "paper_bgcolor": colors["paper"],
                "title": "Dash Data Visualization"
                }
            }
        )
    ])
if __name__ == "__main__":
    app.run_server(debug = True)
