import sys
import argparse
import geopandas as gpd
import pandas as pd
import h3pandas

if __name__ == '__main__':

	description="""This script will convert a geometry file to a collection of Uber H3 shapes. Needs either a shapefile
				   or geojson as an input and will output a geojson.
				   Example run: python polygon_to_h3_collection.py input_file.json --resolution 9 --output_name output_file
				"""

	parser=argparse.ArgumentParser(description=description)
	parser.add_argument('filename', nargs='?', default = None, help="Filename of GeoJSON or ESRI Shapefile")
	parser.add_argument('--resolution',type=int ,help="Set resolution size, larger number equals smaller hexes. 7 minimum recommended")
	parser.add_argument('--output_name',type=str ,help="Set name of output file")
	args=parser.parse_args()

	if(args.filename.endswith('.shp')):
		geodf = gpd.read_file(args.filename,driver = 'ESRI Shapefile')
		geodf = geodf.to_crs('epsg:4326')
	elif(args.filename.endswith(('.json','.geojson')) ):
		geodf = gpd.read_file(args.filename,driver = 'GeoJSON')
	else:
		raise LookupError("Unrecognized file type")

	h3_size = args.resolution

	gdf_h3 = geodf.h3.polyfill_resample(h3_size).reset_index()

	gdf_h3.rename(columns = {'h3_polyfill':'h3_id'},inplace = True)
	gdf_h3['resolution_size'] = h3_size
	gdf_h3 = gdf_h3[['h3_id','resolution_size','geometry']]

	gdf_h3.to_file(args.output_name + '.json',driver = 'GeoJSON')