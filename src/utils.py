from bokeh.models import ColumnDataSource
import pandas as pd
import os
from .color_utils import create_color_mapper
from .map_config import create_figure, add_hover_tool, add_color_bar

def create_map(data_path, title, color_scheme='viridis'):
    df = pd.read_csv(data_path)

    df['x'] = df['long_mercator']
    df['y'] = df['lat_mercator']
    
    source = ColumnDataSource(df)
    
    # Create color mapper using log_mass and is_outlier columns
    color_mapper = create_color_mapper(df, color_scheme)
    
    p = create_figure(title)
    
    # scatter plot using log_mass directly for coloring
    circles = p.scatter(
        x='x', y='y', source=source, size=8,
        color={'field': 'log_mass', 'transform': color_mapper},
        alpha=0.8, line_color='white', line_width=0.5
    )
    
    # interactive components
    add_hover_tool(p, circles)
    add_color_bar(p, color_mapper)
    
    return p, source, df


def load_html_code(filename):
    html_path = os.path.join('static', 'html', filename)
    try:
        with open(html_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"<!-- Error: Could not load {filename} -->"

def load_js_code(filename):
    js_path = os.path.join('static', 'js', filename)
    try:
        with open(js_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"// Error: Could not load {filename}"