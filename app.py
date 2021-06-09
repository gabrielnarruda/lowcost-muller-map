import dash

from data.global_map_data import get_data_from_backend
from environment_variables import HOST, PORT
from html_structures.global_map_html import global_map_layout

if __name__ == '__main__':
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = global_map_layout

    app.run_server(host=HOST, port=PORT, debug=False)
