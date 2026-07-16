from src.data.grid import create_lat_lon_grid
import xarray as xr
import numpy as np
import ee

def load_landcover(area: list[float]) -> tuple[xr.DataArray, np.ndarray]:

    # Convert [lat_min, lon_min, lat_max, lon_max] to EE [lon_min, lat_min, lon_max, lat_max]
    ee_area = [area[1], area[0], area[3], area[2]]

    region = ee.Geometry.Rectangle(ee_area)
    landcover = ee.ImageCollection("ESA/WorldCover/v200").first().clip(region)

    sample = landcover.reproject(crs="EPSG:4326", scale=500).sampleRectangle(region=region, defaultValue=0)
    lc_array = sample.get("Map").getInfo()
    lc_np = np.array(lc_array)

    lats, lons = create_lat_lon_grid(area, lc_np.shape)

    print(lc_np.shape)
    print(np.unique(lc_np))

    lc_da = xr.DataArray(lc_np, dims=["lat", "lon"], coords={"lat": lats, "lon": lons}, name="landcover")

    return lc_da, lc_np
