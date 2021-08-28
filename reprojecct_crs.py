#!/usr/bin/python3


"""reproject_crs.py
	Reprojects a current raster file's CRS to a new user 
	defined CRS.

	https://epsg.io/
	https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
	https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84

	This function only converts the CRS from the current value to
	a new user value, does nothing else.  The returned new dataset
	is of type xarray.core.dataarray.DataArray.

	User required to install the libraries to avoid errors.

	Libraries:
		rasterio
		rioxarray

	API Calls:
		open_rasterio()
		from_string()
		reproject()

        External Dependency:
		None
"""


import rasterio
from rasterio.crs import CRS
import rioxarray as rxr

def reproject_crs(rf: rxr, new_crs: str) -> rxr:
  """
  Reproject the raster from a current CRS to a user specified CRS.

  :rf:        (r)aster (f)ile sent for reprojection
  :new_crs:   user defined new CRS projection

  :Example:
  new_raster_object = reproject_crs(current_raster, 'EPSG:4326')

  """

  # open the raster with rioxarray
  file_crs = rxr.open_rasterio(rf, masked=True).squeeze()

  # display current CRS
  print(f'Raster file current CRS: {file_crs.rio.crs}')

  # obtain new CRS
  crs_wgs84 = CRS.from_string(new_crs)

  # Reproject the dataset with the new crs
  new_wgs84 = file_crs.rio.reproject(crs_wgs84)

  # display new CRS
  print(f'New reprojected raster file CRS: {new_wgs84.rio.crs}')

  return new_wgs84
# end of reproject_crs