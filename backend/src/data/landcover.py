import ee
import numpy as np
import xarray as xr
import requests
import rioxarray

def load_landcover(area: list[float]) -> tuple[xr.DataArray, np.ndarray]:
    ee_area = [area[1], area[2], area[3], area[0]]  # [lon_min, lat_min, lon_max, lat_max]
    region = ee.Geometry.Rectangle(ee_area)

    landcover = ee.ImageCollection("ESA/WorldCover/v200").first().clip(region)

    url = landcover.getDownloadURL({
        "region": region,
        "scale": 1000,
        "crs": "EPSG:4326",
        "format": "GEO_TIFF",
    })

    response = requests.get(url)
    response.raise_for_status()

    tif_path = "../data_cache/tmp/landcover_download.tif"
    with open(tif_path, "wb") as f:
        f.write(response.content)

    lc_da = rioxarray.open_rasterio(tif_path).squeeze()
    lc_da = lc_da.rename({"x": "lon", "y": "lat"})
    lc_da.name = "landcover"
    lc_np = lc_da.values

    return lc_da, lc_np