import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from dash_table import DataTable
import pandas as pd

df = pd.DataFrame(
    {
        
        "Action": [
            "<a href='https://www.google.com/' target='_blank'>Form Submission</a>",
            "<a href='https://www.google.com/' target='_blank'>Started Trial</a>",
            "<a href='https://www.google.com/' target='_blank'>Jobs Page Visited</a>",
            "<a href='https://www.google.com/' target='_blank'>Exited Website</a>",
            "<a href='https://www.google.com/' target='_blank'>Tried Connecting Cloud</a>",
            "<a href='https://www.google.com/' target='_blank'>Cloud Connection Failed</a>",
            "<a href='https://www.google.com/' target='_blank'>Connected Cloud</a>",
            "<a href='https://www.google.com/' target='_blank'>Did not visit any page after</a>",
            "<a href='https://www.google.com/' target='_blank'>Visited Other Pages Cloud</a>"
        ],
        "User Count" : [26,26,24,2,21,3,21,4,17]
    }
)
app = Dash(__name__)
app.layout = html.Div(children=[
    html.Div([  html.H4('Test'),
                dcc.Graph(id="graph"),
                html.P("Opacity"),
                dcc.Slider(id='slider', min=0, max=1, 
                value=0.5, step=0.1)]),
                DataTable(z
    id="table",
    data=df.to_dict("records"),
    columns=[
        {"id": "Action", "name": "Action", "presentation": "markdown"},
        {"id": "User Count", "name": "User Count", "presentation": "markdown"}
    ],
    style_cell={'textAlign': 'center'},
    style_cell_conditional=[
        {
            'if': {"column_id": c},
            'textAlign': 'left'
        }for c in ["Action","User Count"]
    ],
    markdown_options={"html": True},
)
    
])

@app.callback(
    Output("graph", "figure"), 
    Input("slider", "value"))
def display_sankey(opacity):
    fig = go.Figure(data=[go.Sankey(
        link = dict(
            source = [0,  1,  1, 2,  2, 4,  4, 6,  6 ], # indices correspond to labels, eg A1, A2, A1, B1, ...
            target = [1,  2,  3, 4,  3, 6,  7, 8,  9 ],
            value  = [26, 26, 0, 24, 2, 21, 3, 17, 4 ],
            color = [f'rgba(73, 148, 245,{opacity})', f'rgba(96, 221, 240,{opacity})', f'rgba(177,250,202,{opacity})',f'rgba(93, 245, 131,{opacity})',f'rgba(78, 245, 95,{opacity})',f'rgba(135, 247, 54,{opacity})', f'rgba(202, 247, 54,{opacity})', f'rgba(247, 231, 54,{opacity})', f'rgba(240, 161, 34,{opacity})',f'rgba(245, 169, 125,{opacity})']
            ),
        node = {
        'pad' : 3,
        'thickness' : 10,
        'line' : dict(color = "black", width = 0.1),
        "label" : ["landing", "started trial", "jobs visited", "exited website", "tried connecting cloud", "visited other page", "connected cloud", "cloud connection failed" ,"restore page", "export page", "settings page" "did not visit any page"],
        "color" : ['rgba(73, 148, 245,1)', 'rgba(96, 221, 240,1)', 'rgba(177,250,202,1)','rgba(93, 245, 131,1)','rgba(78, 245, 95,1)','rgba(135, 247, 54,1)', 'rgba(202, 247, 54,1)', 'rgba(247, 231, 54,1)', 'rgba(240, 161, 34,1)','rgba(240, 161, 34,1)','rgba(245, 169, 125,1)'],
        "x": [0.1, 0.2, 0.3, 0.35, 0.4, 0.53, 0.46, 0.8, 0.7, 0.8],
        "y": [0.3, 0.3, 0.3, 0.8 , 0.3, 0.3, -0.2, 0.3, 0.8, 0.3],
        
        }
        #color_for_links = ['rgba(73, 148, 245,1)', 'rgba(96, 221, 240,1)', 'rgba(177,250,202,1)','rgba(93, 245, 131,1)','rgba(78, 245, 95,1)','rgba(135, 247, 54,1)', 'rgba(202, 247, 54,1)', 'rgba(247, 231, 54,1)', 'rgba(240, 161, 34,1)','rgba(245, 169, 125,1)']
        )])

    
    fig.update_layout(hovermode='x', font_size=15, width=1200, height=400)
    return fig
if __name__ == "__main__":
    app.run_server(debug=True)




