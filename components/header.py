import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://conecta.mx/images/partners-logos/logo-23.png', height='60', width='60')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Vista completa  ', href='/dash-vanguard-report/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Inversiones Vanguard 500')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Vision General   ', href='/dash-vanguard-report/overview', className="tab first"),

        dcc.Link('Rendimientos   ', href='/dash-vanguard-report/price-performance', className="tab"),

        dcc.Link('Portfolio   ', href='/dash-vanguard-report/portfolio-management', className="tab"),

        dcc.Link('Tarifas y minimos   ', href='/dash-vanguard-report/fees', className="tab"),

        dcc.Link('Distribuciones   ', href='/dash-vanguard-report/distributions', className="tab"),

        dcc.Link('Noticias   ', href='/dash-vanguard-report/news-and-reviews', className="tab")

    ], className="row ")
    return menu
