def remap(value, x_min, x_max, y_min, y_max):
    return ((value - x_min) / (x_max - x_min)) * (y_max - y_min) + y_min
