#Imports
import pandas as pd
import geopandas as gpd
from geopandas.tools import geocode
import requests
import geojson

#import matplotlib
#%matplotlib inline
from shapely.geometry import Polygon, LineString, Point
import matplotlib.pyplot as plt
import shapely.speedups
import folium
import contextily as ctx
from pyproj import CRS

import osmnx as ox
import networkx as nx

from folium.features import FeatureGroup, GeoJson, TopoJson, Marker
from shapely.geometry import mapping
from folium.plugins import MarkerCluster, Search, PolyLineTextPath
from folium.utilities import parse_options
from folium import plugins
import cgi
from fiona._drivers import GDALEnv
import momepy
env = GDALEnv()

def search_for_path(oA, dA):
	# Here we get the asked addresses.
	origAddress = oA
	destAddress = dA

	# Geocode addresses using Nominatim. 
	orig = geocode(origAddress, provider='nominatim', user_agent='autogis_xx', timeout=4)
	dest = geocode(destAddress, provider='nominatim', user_agent='autogis_xx', timeout=4)

	# Extract the lon,lat from orgin and destination.
	orig_yx = (orig['geometry'].at[0].y, orig['geometry'].at[0].x)
	dest_yx = (dest['geometry'].at[0].y, dest['geometry'].at[0].x)

	# Find nearest nodes
	oNearest = ox.get_nearest_node(graph, orig_yx, method='euclidean')
	dNearest = ox.get_nearest_node(graph, dest_yx, method='euclidean')

	
	origin = nodes.loc[oNearest]
	destination = nodes.loc[dNearest]

	odNodes = gpd.GeoDataFrame([origin, destination], geometry='geometry', 
                           crs=nodes.crs)
	

	# Import the files you want to use on the map.
	# The nodes and edges of the graph:
	nodes = gpd.read_file("Lahtotiedot/HelsinkiCenterNodes.shp")
	edges = gpd.read_file("Lahtotiedot/HelsinkiCenterEdges.shp")

	# The unobstructed routes to show on the map
	etasonReitit = gpd.read_file("Lahtotiedot/etasonreititkartalle.geojson", driver="GeoJson")
	etasonReititGeoJson = GeoJson(etasonReitit, name="etasonReitit")

	#The unobstructed squares to show on the map
	etatasonAlueet = gpd.read_file("Lahtotiedot/etasonalueetkartalle.geojson", driver="GeoJson")
	etasonAlueetGeoJson = GeoJson(etasonAlueet, name="etasonAlueet")

	#And the voice signages to show on the map
	aaniopasteet = gpd.read_file("Lahtotiedot/aaniopasteetkartalle.geojson", driver="GeoJson")
	aaniopasteetGeoJson = GeoJson(aaniopasteet, name="aaniopasteet")
	
	# Finally get the unobstructed buffer areas
	esteetonaluebuffer = gpd.read_file("Lahtotiedot/esteetonalue.shp")
	esteetonAluekartalle = esteetonaluebuffer.unary_union

	
	#Here we create the graph
	graph = momepy.gdf_to_nx(edges, approach='primal')

	#...And finally the shortest path
	route = nx.shortest_path(G=graph, source=oNearest, target=dNearest, 
                         weight='length')

	# For folium, we need to rearrage the points
	for i in range(len(route)-1):
    		point = nodes.loc[route[i]].geometry
    		path.append([point.y, point.x])

	# Now we can create a folium map
	m = folium.Map(location= [path[0][0], path[0][1]], zoom_start=17, min_zoom = 13, 
               max_zoom= 20, control_scale=True, tiles="CartoDB Positron")

	etasonReititGeoJson.add_to(m)
	etasonAlueetGeoJson.add_to(m)
	aaniopasteetGeoJson.add_to(m)

	startMarker = folium.Marker(location= [path[0][0], path[0][1]], popup='Lähtöosoite: ' + origAddress).add_to(m)

	# This list is going to be the path that we show on the map.
	for i in range(len(route)-1):
    		pathP = []

    		point1 = Point(nodes.loc[route[i]].geometry.x, nodes.loc[route[i]].geometry.y)
    
    		point2 = Point(nodes.loc[route[i+1]].geometry.x, nodes.loc[route[i+1]].geometry.y)
    
    		pathP.append([nodes.loc[route[i]].geometry.y, nodes.loc[route[i]].geometry.x])
    		pathP.append([nodes.loc[route[i+1]].geometry.y, nodes.loc[route[i+1]].geometry.x])
    		#print(pathP)
    		lineString = LineString([point1, point2])
    		if point1.within(esteetonAluekartalle) and point2.within(esteetonAluekartalle):
        		attr = {'fill': 'black', 'font-weight': 'bold', 'font-size': '16'}
        		pline = folium.PolyLine(pathP, weight=8, color='green', opacity=0.6).add_to(m)
        
    		else:
        		attr = {'fill': 'black', 'font-weight': 'bold', 'font-size': '16'}
        		pline = folium.PolyLine(pathP, weight=8, color='red', opacity=0.6).add_to(m)
        
	endMarker = folium.Marker(location= [path[len(path)-1][0], path[len(path)-1][1]], popup='Määränpää: ' + destAddress).add_to(m)
