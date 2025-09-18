from src.utils import create_map
from src.plot_template import (
    create_controls, create_callbacks, setup_interactions, 
    initialize_stats, create_layout
)

def create_plot():
    # Create map
    plot, source, df = create_map('data/geo_data3.csv', 'Meteorite Landings (Year <= 1752)', 'cividis')
    
    # Create controls
    controls = create_controls(df, "Year <= 1752")
    
    # Setup callbacks and interactions
    callbacks = create_callbacks(controls, source, "Year <= 1752")
    setup_interactions(controls, callbacks)
    
    # Initialize statistics
    initialize_stats(controls, df, "Year <= 1752")
    
    # Create and return layout
    return create_layout(controls, plot)
