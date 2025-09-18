from bokeh.plotting import figure
from bokeh.models import HoverTool, ColorBar
import xyzservices.providers as xyz

def create_figure(title):
    p = figure(
        title=title,
        x_axis_type="mercator",
        y_axis_type="mercator",
        tools="pan,wheel_zoom,reset,save",
        active_scroll="wheel_zoom",
        width=1000,
        height=625,  # 16:10 aspect ratio
        sizing_mode="scale_width",
        output_backend="webgl",
        background_fill_color="#161b22",
        border_fill_color="#0d1117"
    )
    
    # dark themed CartoDB tile by xyzservices library
    p.add_tile(xyz.CartoDB.DarkMatter, retina=True)
    
    # Set bounds and default view
    p.x_range.bounds = (-20037508, 20037508)
    p.y_range.bounds = (-20037508, 20037508)
    p.x_range.start = -20000000
    p.x_range.end = 20000000
    p.y_range.start = -10000000
    p.y_range.end = 15000000
    
    return p

def add_hover_tool(figure, circles):
    hover = HoverTool(
        tooltips=[
            ("Name", "@name"),
            ("Class", "@recclass"),
            ("Mass (g)", "@mass{0,0.0000}"),
            ("Log Mass", "@log_mass{0.00}"),
            ("Year", "@year"),
            ("Fall/Find", "@fall"),
            ("Location", "(@reclat{0.000}, @reclong{0.000})")
        ],
        renderers=[circles]
    )
    figure.add_tools(hover)

def add_color_bar(figure, color_mapper):
    # color bar legend information
    color_bar = ColorBar(
        color_mapper=color_mapper,
        width=8,
        height=200,
        location=(0, 0),
        title="Log Mass (g)",
        title_text_font_size="12pt",
        label_standoff=12,
        border_line_color=None,
        background_fill_alpha=0
    )
    figure.add_layout(color_bar, 'right')
