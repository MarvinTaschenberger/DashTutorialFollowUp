import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
opts = [
        {"label": "New York City", "value": "NYC"},
        {"label": "Lay Angeles", "value": "LAX"},
        {"label":"San Francisco","value": "SF"}
    ]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Label("Dropdown"),
    dcc.Dropdown(
        options=opts,
        value="LAX"
        ),
    html.Label("Multi-Select-Dropdown"),
    dcc.Dropdown(
        options=opts,
        value="LAX",
        multi=True),
    html.Label("Radio Buttons"),
    dcc.RadioItems(
        options=opts,
        value="LAX"
        ),
    html.Label("Checkboxes"),
    dcc.Checklist(
        options=opts,
        values=["LAX"]
        ),
    html.Label("Text Input"),
    dcc.Input(
        value="LAX",
        type="text"
        ),
    html.Label("Slider"),
    dcc.Slider(
        min=0,
        max=9,
        marks={i : f"Label {i}" for i in range(1,6) },
        value= 5
        )

    ],
    style={"columnCount":2})


if __name__ == "__main__":
    app.run_server(debug=True)