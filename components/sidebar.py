from dash.dependencies import Input, Output, State
from app import app

from dash_bootstrap_templates import load_figure_template

load_figure_template(["darkly"])

# =========  Callbacks  =========== #
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal2", "is_open"),
    [Input("open2", "n_clicks"), Input("close2", "n_clicks")],
    [State("modal2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal5", "is_open"),
    [Input("open5", "n_clicks"), Input("close5", "n_clicks")],
    [State("modal5", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
