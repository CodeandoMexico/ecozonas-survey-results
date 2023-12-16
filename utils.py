def normalize(value, from_min, from_max, to_min, to_max):
    return ((value - from_min) / (from_max - from_min)) * (to_max - to_min) + to_min
