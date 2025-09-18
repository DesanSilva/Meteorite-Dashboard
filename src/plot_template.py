from bokeh.layouts import column, row
from bokeh.models import Button, CustomJS, Div, Select, RangeSlider
from src.utils import load_js_code, load_html_code

def create_controls(df, period_label):
    # Statistics display
    stats_div = Div(text="", width=260, height=200, sizing_mode="fixed")
    
    # Year Slider
    year_slider = RangeSlider(
        title="Year",
        start=df['year'].min(),
        end=df['year'].max(),
        value=(df['year'].min(), df['year'].max()),
        step=1,
        width=260
    )
    
    # Mass Slider
    mass_slider = RangeSlider(
        title="Mass (kg)",
        start=0, end=1000, value=(0, 1000), step=10,
        width=260
    )
    
    # Toggle Button
    outlier_button = Button(label="Show Only Outliers (>1000kg)", button_type="primary", width=260)
    
    # Dropdown controls
    fall_options = ["All"] + list(df['fall'].unique())
    fall_select = Select(title="Fall/Find Type", value="All", options=fall_options, width=260)
    
    recclass_options = ["All"] + sorted(df['recclass'].unique().tolist())
    recclass_select = Select(title="Meteorite Class", value="All", options=recclass_options, width=260)
    
    return {
        'stats_div': stats_div,
        'year_slider': year_slider,
        'mass_slider': mass_slider,
        'outlier_button': outlier_button,
        'fall_select': fall_select,
        'recclass_select': recclass_select
    }

def create_callbacks(controls, source, period_label):
    callback = CustomJS(
        args=dict(
            source=source,
            original_data=source.data,
            **controls
        ),
        # Create JavaScript callbacks using external JS files
        code=load_js_code('filter_callback.js').replace('Statistics:', f'{period_label} Statistics:')
    )
    
    # Toggle button callback
    outlier_callback = CustomJS(
        args=dict(outlier_button=controls['outlier_button'], cb=callback),
        code=load_js_code('toggle_callback.js')
    )
    
    return callback, outlier_callback

def setup_interactions(controls, callbacks):
    callback, outlier_callback = callbacks
    
    controls['year_slider'].js_on_change('value', callback)
    controls['mass_slider'].js_on_change('value', callback)
    controls['fall_select'].js_on_change('value', callback)
    controls['recclass_select'].js_on_change('value', callback)
    controls['outlier_button'].js_on_click(outlier_callback)

def initialize_stats(controls, df, period_label):
    """Initialize statistics display using external HTML template."""
    stats = {
        'total_count': len(df),
        'avg_mass': df['mass'].mean(),
        'total_mass': df['mass'].sum(),
        'min_mass': df['mass'].min(),
        'max_mass': df['mass'].max(),
        'min_year': int(df['year'].min()),
        'max_year': int(df['year'].max()),
        'most_common_class': df['recclass'].mode().iloc[0] if not df['recclass'].mode().empty else 'N/A',
        'period_label': period_label
    }
    
    # Load HTML template and format with stats data
    stats_template = load_html_code('stats_template.html')
    controls['stats_div'].text = stats_template.format(**stats)

def create_layout(controls, plot):
    # Left side: controls and statistics column
    controls_layout = column(
        controls['year_slider'],
        controls['mass_slider'],
        controls['fall_select'],
        controls['recclass_select'],
        controls['outlier_button'],
        controls['stats_div'],
        sizing_mode="fixed",
        width=280,
        margin=(10, 10, 10, 10)
    )
    
    # Right side: main plot
    return row(
        controls_layout, 
        plot, 
        sizing_mode="stretch_width",
        margin=(20, 20, 20, 20)
    )
