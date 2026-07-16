import earthkit.data as ekd
import xarray as xr

def load_era5(year: str, month: str, days: list[str], area: list[float]) -> xr.Dataset:
    temp_data = ekd.from_source(
        "cds",
        "reanalysis-era5-single-levels",
        variable="2m_temperature",
        product_type="reanalysis",
        year=str(year),
        month=str(month).zfill(2),
        day=days,
        time=["12:00"],
        area=area,
        format="netcdf",
    )

    ds = temp_data.to_xarray()
    ds["t2m_C"] = ds["t2m"] - 273.15

    return ds
