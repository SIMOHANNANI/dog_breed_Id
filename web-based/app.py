import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select an image')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True,
        className='mt-5',
    ),
    dbc.Row(
        children=[
            dbc.Col(
                className='col img-fluid',
                children=[dbc.Container(id='output-image-upload')],
            ),

        ],
    ),
    dbc.Row(
        children=[
            dbc.Col(
                className='col',
                children=[html.Div(id='predicted-dog-breed')],
            ),
        ]
    )

])


def parse_contents(contents):
    return html.Div([
        html.Img(src=contents),
    ])


@app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents')],
              )
def update_output(list_of_contents):
    if list_of_contents is not None:
        children = [
            parse_contents(c) for c in
            list_of_contents]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)
