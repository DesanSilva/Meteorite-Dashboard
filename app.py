from bokeh.layouts import column
from bokeh.models import Div
from bokeh.plotting import curdoc
from bokeh.themes import Theme

from src.plot1 import create_plot as create_plot1
from src.plot2 import create_plot as create_plot2
from src.plot3 import create_plot as create_plot3
from src.utils import load_html_code

# custom dark theme optimized for meteorite dashboard
curdoc().theme = Theme(filename="theme.yml")

# title header using external HTML file
header_content = load_html_code('header.html')
header_div = Div(
    text=header_content, 
    sizing_mode="stretch_width",
    width_policy="max",
    height_policy="auto",
    margin=(0, 0, 0, 0)
)

# Create the three plots
plot1 = create_plot1()
plot2 = create_plot2()
plot3 = create_plot3()

# Arrange the layout with full width utilization
layout = column(
    header_div, 
    plot1, 
    plot2, 
    plot3, 
    sizing_mode="stretch_width",
    width_policy="max",
    spacing=20,
    margin=(0, 0, 0, 0)
)

# Add the layout to the document
curdoc().add_root(layout)
curdoc().title = "Meteorite Landings Dashboard"
