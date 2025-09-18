// Filter callback for meteorite dashboard
// Updates the data source based on slider and dropdown values

const data = original_data;
const [year_min, year_max] = year_slider.value;
const [mass_min, mass_max] = mass_slider.value;
const fall_value = fall_select.value;
const recclass_value = recclass_select.value;
const show_only_outliers = outlier_button.button_type === 'success';

// Helper function to check if a data point should be included
function shouldInclude(i) {
    const is_outlier = data.is_outlier[i] === 1;
    const in_year = data.year[i] >= year_min && data.year[i] <= year_max;
    const in_mass = (data.mass[i] / 1000) >= mass_min && (data.mass[i] / 1000) <= mass_max;
    const in_fall = fall_value === "All" || data.fall[i] === fall_value;
    const in_recclass = recclass_value === "All" || data.recclass[i] === recclass_value;
    
    // Basic filters must pass
    if (!in_year || !in_fall || !in_recclass) return false;
    
    // Apply outlier/mass logic
    if (show_only_outliers) {
        return is_outlier;  // Only outliers
    } else {
        return is_outlier || in_mass;  // Outliers + normal data within mass range
    }
}

// Filter data using indices
const included_indices = [];
for (let i = 0; i < data.year.length; i++) {
    if (shouldInclude(i)) {
        included_indices.push(i);
    }
}

// Build new data object efficiently
const new_data = {};
Object.keys(data).forEach(key => {
    new_data[key] = included_indices.map(i => data[key][i]);
});

source.data = new_data;

// Update statistics
if (new_data.mass && new_data.mass.length > 0) {
    const total_count = new_data.mass.length;
    const avg_mass = new_data.mass.reduce((a, b) => a + b, 0) / total_count;
    const total_mass = new_data.mass.reduce((a, b) => a + b, 0);
    const min_mass = Math.min(...new_data.mass);
    const max_mass = Math.max(...new_data.mass);
    const min_year = Math.min(...new_data.year);
    const max_year = Math.max(...new_data.year);
    
    // Find most common class
    const class_counts = {};
    new_data.recclass.forEach(cls => {
        class_counts[cls] = (class_counts[cls] || 0) + 1;
    });
    const most_common_class = Object.keys(class_counts).reduce((a, b) => 
        class_counts[a] > class_counts[b] ? a : b, '');
    
    stats_div.text = `
        <b>Statistics:</b><br>
        Total Meteorites: ${total_count}<br>
        Average Mass: ${avg_mass.toFixed(1)} g<br>
        Total Mass: ${total_mass.toFixed(0)} g<br>
        Mass Range: ${min_mass.toFixed(0)}g - ${max_mass.toFixed(0)}g<br>
        Year Range: ${min_year} - ${max_year}<br>
        Most Common Class: ${most_common_class}
    `;
} else {
    stats_div.text = "<b>No meteorites match current filters</b>";
}

source.change.emit();
