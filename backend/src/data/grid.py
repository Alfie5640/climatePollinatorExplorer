import numpy as np

def create_lat_lon_grid(area, shape):
    n_lat, n_lon = shape

    lats = np.linspace(area[0], area[2], n_lat)
    lons = np.linspace(area[1], area[3], n_lon)

    return lats, lons