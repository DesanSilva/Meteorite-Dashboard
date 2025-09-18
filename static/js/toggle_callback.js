// Toggle button callback for outlier filtering
// Switches between showing all data and showing only outliers

if (outlier_button.button_type === 'primary') {
    outlier_button.button_type = 'success';
    outlier_button.label = "Show All Data";
} else {
    outlier_button.button_type = 'primary';
    outlier_button.label = "Show Only Outliers (>1000kg)";
}
cb.execute();
