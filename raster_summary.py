#!/usr/bin/python3

""" raster_summary.py
	Provides a summary of the raster metadata and plot the image.  
	User ensures the raster file path is known and pass into this function.
	Note the naming scheme, '.tif' is the common type when raster is originally created.

	https://rasterio.readthedocs.io/en/latest/topics/reading.html

	This function opens the file for reading then calls the close() method to end
	the process.  If this function gets called many times, this could slow down
	the process.  Remove the close() at the end or redesign the code to avoid
	process slowdown.

	Libraries:
		OS
		Pprint
		Rasterio

	API Calls:
		os.path.join()
		rasterio.open()
		pprint()
		show()

        External Dependency:
		None

"""

import os
from pprint import pprint
import rasterio
from rasterio.plot import show

def raster_summary(raster_dir: str, raster_file: str):
	"""Reads a raster file and outputs the metadata and image.

	Args:
		raster_dir:	dir path location of the raster file
		raster_file:	raster file name
	Returns:
		None
	"""

	# for single file operation, use line by line commands
	# open file for rasterio
	fp = os.path.join(raster_dir, raster_file)
  
	# Open the file:
	raster = rasterio.open(fp)

	# from rasterio doc: attributes
	print(f'Raster shape:\t\t {raster.shape}')
	print(f'Raster band count:\t {raster.count}')
	print(f'Raster data types:\t {raster.dtypes} ')
	print(f'Raster valid data mask:\t {raster.nodatavals}')
	print(f'Raster not valid mask:\t {raster.nodata}')

	print(f'Raster metadata:\n')
	pprint(raster.meta)

	# the plot dimensions show the longitude, x, and lattitude, y
	show(raster);

	raster.close()
	return
# end raster_summary