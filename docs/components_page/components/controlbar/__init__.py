from pathlib import Path

from dash import dcc
from dash import html

from ...api_doc import ApiDoc
from ...metadata import get_component_metadata

HERE = Path(__file__).parent

content = [
    html.H2("Controlbar", className="display-4"),
    html.P(
        dcc.Markdown(
            "Documentation and examples for how to use "
            "Controlbar with *dash-admin-components*."
        ),
        className="lead",
    ),
    ApiDoc(get_component_metadata("src/lib/components/Controlbar.react.js")),
]
