import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1("Hello Dash"),
    html.Div(children=[
        """ Dash: A web application framework with python 
        based on flask and react - woot """
        ]),
    dcc.Graph(
        id = "example-graph",
        figure = {
            "data": [
                {"x": [1,2,3,4], "y": [4,2,2,3], "type":"bar", "name":"SF"},
                {"x": [1,2,3,4], "y": [2,5,4,3], "type":"bar", "name": "LAX"}
                ],
            "layout" : {
                "title": "Dash Data Visualization"
                }
            }
        )
    ])
if __name__ == "__main__":
    app.run_server(debug = True)
