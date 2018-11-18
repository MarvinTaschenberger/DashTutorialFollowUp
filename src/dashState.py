import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-1", type="text", value="Los Angeles"),
    dcc.Input(id="input-2", type="text", value="Germany"),
    html.Button(id="submit-button", n_clicks=0, children="Submit"),
    html.Div(id="out-div")
    ])

@app.callback(Output("out-div", "children"),
              [Input("submit-button", "n_clicks")],
             [State("input-1", "value"),
              State("input-2", "value")])
def update_text(n_clicks, in1, in2):
    return f""" Input 1 is {in1} and Input 2 is {in2}"""

if __name__ == "__main__":
    app.run_server(debug=True)