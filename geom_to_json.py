#!/usr/bin/python3

""" geom_to_json.py
	Converts a geometry, whether a shapefile or something else, into a JSON 
	construct.  This format is required by Google Earth Engine (GEE) for further 
	operation such as extracting a raster from satellite images.
	https://developers.google.com/earth-engine/guides/table_upload

	This is a commen method of extracting datasets because it covers a certain 
	range of time rather than a single event. The geometry bounds this collection 
	to create a final raster that only contains attributes for the area of intereset 
	(AOI). Because it uses GEE, the type has to be converted to JSON.
	https://developers.google.com/earth-engine/tutorials/tutorial_api_04

	NOTE ABOUT Google Earth Engine:
	This code assumes the user has the authorization and authentication to use GEE.
	https://developers.google.com/earth-engine/guides/python_install

	The code below is an extension from this Q&A link (original code):
	https://gis.stackexchange.com/questions/333791/accessing-a-shapefile-with-googleearthengine-api-invalid-geojson-geometry/334400#334400

	And syntax explanation from geopandas:
	https://geopandas.org/gallery/polygon_plotting_with_folium.html?highlight=to_json

	Libraries:
		Pandas
		Geopandas
		Google Earth Engine

	API Calls:
		gpd.GeoSeries()
		[gpd].to_json()
		ee.FeatureCollection()
		ee.Feature()

        External Dependency:
		None

"""

import pandas as pd
import geopandas as gpd
import ee

def geom_to_json(df: pd.DataFrame, i: int) -> ee.geometry.Geometry, str:
	"""Converts shapefile or any geometry input into JSON format for GEE.

	Args:
		df:	panda dataframe containing shapefile contents
		i:	integer value indicating which row in the dataframe to process

	Returns:
		region:	the JSON string
		admin:	label for the section of the geometry, useful for file associations or names
	"""

	# extract the geometry for the given AOI
	g =  df.iloc[i,:]

	geom = gpd.GeoSeries(g['geometry'])           	# reflecting the new geopandas API for json conversion
                                            		# 'geometry' is the built in label commonly used in shapefiles, see dataframe
	jsonDict = eval(geom.to_json())
	geojsonDict = jsonDict['features'][0]		# [0]th location of the 'features' index in the JSON dictionary order

	# call to the GEE API
	region = ee.FeatureCollection(ee.Feature(geojsonDict)).geometry()

	# label the geometry for easy reference
	d = str(g['District Name']).lower().strip()
	admin = d.replace(' ', '_')     		# remove non alphanumeric character

	return region, admin
# end geom_to_json