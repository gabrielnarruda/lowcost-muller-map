import dash

from html_structures.global_map_html import global_map_layout

if __name__ == '__main__':
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = global_map_layout

    app.run_server(debug=True)
