from bokeh.models import LinearColorMapper
from bokeh.palettes import viridis, plasma, cividis

def get_palette(color_scheme):
    palettes = {
        'viridis': viridis(256),
        'plasma': plasma(256),
        'cividis': cividis(256)
    }
    return palettes.get(color_scheme, viridis(256))

def create_color_mapper(df, color_scheme):
    # Use non-outlier data for color range
    normal_data = df[df['is_outlier'] == 0]
    
    if len(normal_data) > 0:
        low_val = normal_data['log_mass'].min()
        high_val = normal_data['log_mass'].max()
    else:
        low_val = df['log_mass'].min()
        high_val = df['log_mass'].max()
    
    return LinearColorMapper(
        palette=get_palette(color_scheme),
        low=low_val,
        high=high_val,
        nan_color='lightgray'
    )
