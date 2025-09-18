from src.utils import create_map
from src.plot_template import (
    create_controls, create_callbacks, setup_interactions, 
    initialize_stats, create_layout
)

def create_plot():
    # Create map
    plot, source, df = create_map('data/geo_data2.csv', 'Meteorite Landings (1753 <= Year <= 1973)', 'plasma')
    
    # Create controls
    controls = create_controls(df, "1753 <= Year <= 1973")
    
    # Setup callbacks and interactions
    callbacks = create_callbacks(controls, source, "1753 <= Year <= 1973")
    setup_interactions(controls, callbacks)
    
    # Initialize statistics
    initialize_stats(controls, df, "1753 <= Year <= 1973")
    
    # Create and return layout
    return create_layout(controls, plot)
