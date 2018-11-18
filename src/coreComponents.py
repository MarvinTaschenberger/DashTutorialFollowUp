import dash
import dash_core_components as dcc
import dash_html_components as html

from datetime import datetime
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
    html.Label("Force to choose Drop Down "),
    dcc.Dropdown(
        options=opts,
        value="LAX",
        clearable=False
        ),
    html.Label("DropDown with Placeholder"),
    dcc.Dropdown(
        options=opts,
        placeholder="Select a City"
        ),
    html.Label("Disabled DropDown"),
    dcc.Dropdown(
        options=opts,
        value="LAX",
        disabled=True
        ),
    html.Label("Multi-Select-Dropdown"),
    dcc.Dropdown(
        options=opts,
        value="LAX",
        multi=True),
    html.Label("Radio Buttons Underneath each other"),
    dcc.RadioItems(
        options=opts,
        value="LAX"
        ),

    html.Label("Radio Buttons next to each other"),
    dcc.RadioItems(
        options=opts,
        value="LAX",
        labelStyle= {"display": "inline-block"}
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
    html.Label("Text Area"),
    dcc.Textarea(
        placeholder=" Enter your  wishes here",
        value="This is a text area component and it accepts your dreams",
        style={"width":"100%"}
        ),
    html.Label("Slider"),
    dcc.Slider(
        min=0,
        max=9,
        marks={i : f"Label {i}" for i in range(1,6) },
        value= 5
        ),
    html.Label("Non Linear Slider"),
    dcc.Slider(
        min=0,
        max=4,
        step=0.1,
        marks={i: f"{10**i}" for i in range(4)},
        value=2
        ),
    html.Label("Range Slider"),
    dcc.RangeSlider(
        count=1,
        min= -5,
        max = 10,
        step=0.5,
        value=[5,10]
        ),
    html.Label("Single Date Picker"),
    dcc.DatePickerSingle(
        date=datetime(1993,11,23)
        ),
    html.Label("Date Picker Range "),
    dcc.DatePickerRange(
        start_date=datetime(1993,11,23),
        end_date=datetime.today()
        ),
    html.Label("Date Picker with differen Format"),
    dcc.DatePickerRange(
        start_date=datetime(1993,11,23),
        end_date=datetime.today(),
        display_format="Do MMM YY"
        )

    ],
    style={"columnCount":2})


if __name__ == "__main__":
    app.run_server(debug=True)