import ee
import numpy as np
import xarray as xr
import requests
import rioxarray
from src.data.grid import create_lat_lon_grid

def load_ndvi(start_date: str, end_date: str, area: list[float]) -> tuple[xr.DataArray, np.ndarray]:
    ee_area = [area[1], area[2], area[3], area[0]]  # [lon_min, lat_min, lon_max, lat_max]
    region = ee.Geometry.Rectangle(ee_area)

    ndvi_collection = (
        ee.ImageCollection("MODIS/061/MOD13Q1")
        .filterDate(start_date, end_date)
        .filterBounds(region)
        .select("NDVI")
    )

    ndvi_image = ndvi_collection.mean().clip(region)

    url = ndvi_image.getDownloadURL({
        "region": region,
        "scale": 1000,
        "crs": "EPSG:4326",
        "format": "GEO_TIFF",
    })

    response = requests.get(url)
    response.raise_for_status()

    tif_path = "../data_cache/tmp/ndvi_download.tif"
    with open(tif_path, "wb") as f:
        f.write(response.content)

    ndvi_da = rioxarray.open_rasterio(tif_path).squeeze() / 10000
    ndvi_da = ndvi_da.rename({"x": "lon", "y": "lat"})
    ndvi_da.name = "ndvi"
    ndvi_np = ndvi_da.values

    return ndvi_da, ndvi_np