# Meteorite Landings Dashboard

An interactive visualization platform for exploring global meteorite landing data from NASA's Open Data Portal. This application provides comprehensive analysis tools for investigating meteorite discoveries across different time periods, geographic locations, and physical characteristics.

## Dataset Overview

The dashboard analyzes a dataset of 45,716 meteorite landings sourced from https://catalog.data.gov/dataset/meteorite-landings. The data encompasses meteorites discovered from 860 CE to 2025 CE, providing insights into both historical finds and modern systematic search efforts.

### Data Characteristics

- **Total Records**: 45,716 confirmed meteorite landings
- **Geographic Coverage**: Global coordinates with latitude and longitude precision
- **Temporal Range**: 860 CE - 2025 CE (over 1,100 years of data)
- **Mass Distribution**: Ranges from 0.01 grams to 60,000 kilograms
- **Classification System**: Over 450 distinct meteorite types and subtypes

### Key Variables

The dataset includes several critical variables for analysis:

- **Name and ID**: Unique identifiers for each meteorite
- **Classification (recclass)**: Meteorite type based on mineralogical composition
- **Mass**: Weight in grams, spanning seven orders of magnitude
- **Fall vs Find**: Discovery method classification
- **Year**: Year of discovery or observed fall
- **Geographic Coordinates**: Precise landing locations
- **Validation Status**: Data quality indicators

## Application Features

### Three-Period Analysis

The dashboard divides the data into three distinct historical periods to highlight different eras of meteorite discovery:

1. **Period 1 (≤1752)**: Historical discoveries from early civilizations
2. **Period 2 (1753-1973)**: Scientific revolution and systematic cataloging
3. **Period 3 (≥1974)**: Modern era with advanced detection technologies

### Interactive Controls

Each visualization includes filtering and exploration tools:

- **Temporal Filtering**: Year range sliders for temporal analysis
- **Mass Filtering**: Weight-based filtering with outlier toggle functionality
- **Classification Filtering**: Meteorite type selection from 450+ categories
- **Discovery Type Filtering**: Fall vs Find classification
- **Real-time Statistics**: Dynamic summary statistics that update with filters

### Outlier Analysis

The application includes specialized functionality for analyzing extreme statistical outliers (meteorites exceeding 1000 kg), which represent less than 1% of all discoveries but account for a significant portion of total recovered mass.

## Data Insights

### Geographic Patterns

- **Antarctica**: Largest concentration of discoveries due to systematic search programs
- **Desert Regions**: High preservation rates in arid climates
- **Population Centers**: Historical bias toward inhabited areas in early periods

### Temporal Trends

- **Exponential Growth**: Dramatic increase in discoveries since 1970s
- **Technology Impact**: Advanced detection methods revolutionized discovery rates
- **Search Programs**: Coordinated efforts in Antarctica and desert regions

### Classification Distribution

- **Ordinary Chondrites**: Constitute majority of all meteorites
- **Rare Types**: Include achondrites, irons, and specialized classifications
- **Composition Diversity**: Reflects variety of parent body origins

## Technical Implementation

Built using Python and Bokeh for interactive web-based visualization, the application features:

- **Modular Architecture**: Separate components for different time periods
- **Real-time Filtering**: Client-side JavaScript for responsive interactions
- **Statistical Analysis**: Dynamic computation of summary statistics
- **Responsive Design**: Optimized for various screen sizes and devices

## Data Source

https://catalog.data.gov/dataset/meteorite-landings

Origin: NASA's Jet Propulsion Laboratory and is maintained as part of NASA's Open Data initiative.

## Usage

To run the application:

```bash
python -m bokeh serve app.py --show
```