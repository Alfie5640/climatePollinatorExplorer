import ee
import numpy as np
import xarray as xr
from src.data.grid import create_lat_lon_grid

def load_ndvi(start_date: str, end_date: str, area: list[float]) -> tuple[xr.DataArray, np.ndarray]:
    region = ee.Geometry.Rectangle(area)

    ndvi_collection = (
        ee.ImageCollection("MODIS/061/MOD13Q1")
        .filterDate(start_date, end_date)
        .filterBounds(region)
        .select("NDVI")
    )

    ndvi_image = (
        ndvi_collection.mean()
        .clip(region)
        .reproject(crs="EPSG:4326", scale=500)
    )

    sample = ndvi_image.sampleRectangle(region=region, defaultValue=0)
    ndvi_array = sample.get("NDVI").getInfo()
    ndvi_np = np.array(ndvi_array) / 10000

    lats, lons = create_lat_lon_grid(area, ndvi_np.shape)

    ndvi_da = xr.DataArray(ndvi_np, dims=["lat", "lon"], coords={"lat": lats, "lon": lons}, name="ndvi")

    return ndvi_da, ndvi_np