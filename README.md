# polygon_to_h3_converter
Project that used python script to convert a polygon into a collection of h3 hexes

This script will convert a geometry file to a collection of Uber H3 shapes. Needs either a shapefile
or geojson as an input and will output a geojson. Run in terminal/cmd window

Example run: python polygon_to_h3_collection.py input_file.json --resolution 9 --output_name output_file
