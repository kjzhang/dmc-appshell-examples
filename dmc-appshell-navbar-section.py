import dash
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify

dash._dash_renderer._set_react_version("18.2.0")

stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

header = dmc.AppShellHeader(
    dmc.Group(
        [
            dmc.Burger(id="burger-button", hiddenFrom="sm", size="sm"),
            DashIconify(icon="logos:mantine"),
        ],
        h="100%",
        px="md",
    ),
)

navbar = dmc.AppShellNavbar(
    [
        dmc.AppShellSection("Navbar header"),
        dmc.AppShellSection(
            [
                dmc.ScrollArea(
                    [
                        dmc.Text("60 links in a scrollable section"),
                        *[
                            dmc.Skeleton(h=28, mt="sm", animate=False)
                            for _ in range(60)
                        ],
                    ],
                    type="hover",
                    scrollbarSize=12,
                    h=0,
                    style={"flexGrow": 1},
                ),
            ],
            grow=True,
            my="md",
            style={"display": "flex", "flexDirection": "column"},
        ),
        dmc.AppShellSection("Navbar footer – always at the bottom"),
    ],
    p="md",
    id="navbar",
    style={"display": "flex", "flexDirection": "column"},
)

app_shell = dmc.AppShell(
    [
        header,
        navbar,
        dmc.AppShellMain("Main"),
    ],
    header={"height": 60},
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    padding="md",
    id="app-shell",
)

app.layout = dmc.MantineProvider([app_shell])


@app.callback(
    Output("app-shell", "navbar"),
    Input("burger-button", "opened"),
    State("app-shell", "navbar"),
)
def toggle_navbar(opened, navbar):
    navbar["collapsed"]["mobile"] = not opened
    return navbar


if __name__ == "__main__":
    app.run_server(debug=True)
