import geopandas as gpd
from shapely.geometry import box

def load_blines(area: list[float]) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    blines = gpd.read_file("../data_cache/blines/blines_uk.gpkg")
    blines_4326 = blines.to_crs(epsg=4326)

    pilot_bbox = box(area[1], area[2], area[3],area[0])
    blines_clip = blines_4326.clip(pilot_bbox)

    blines_exploded = blines_4326.explode(index_parts=False).reset_index(drop=True)
    
    return (blines_exploded, blines_clip)