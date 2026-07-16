import xarray as xr

def load_spei(date: str, area: list[float]) -> xr.Dataset:
    spei = xr.open_dataset("../data_cache/spei/spei03.nc")

    spei_uk_buffered = spei.sel(lat=slice(area[2], area[0]), lon=slice(area[1], area[3]))
    spei_uk_buffered = spei_uk_buffered.where(spei_uk_buffered["spei"] < 1e29)
    spei_uk_buffered = spei_uk_buffered.ffill(dim="lon").bfill(dim="lon").ffill(dim="lat").bfill(dim="lat")
    spei_pilot = spei_uk_buffered.sel(time=date, method="nearest")

    return spei_pilot