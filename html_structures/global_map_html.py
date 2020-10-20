import dash_html_components as html
import dash_core_components as dcc

from chart.global_map_chart import fig
from globals.styles import colors

global_map_layout = html.Div(children=[
    html.H1(children='ENVIRONMENTAL RADIATION EXPOSURE THOUGH THE USE OF GEIGER-MÜLLER DETECTOR', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
