# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/home")),
                dbc.NavItem(dbc.NavLink("API Documentation", href="/page2")),
                dbc.NavItem(dbc.NavLink("Send Feedback", href="/page2")),
                dbc.NavItem(dbc.NavLink("Contact", href="/page2")),
            ] ,
            brand="WHAM",
            brand_href="/home",
            color="#0071c5",
            dark=True,
        ), 
    ])

    return layout
