{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Imports\n",
    "import pandas as pd\n",
    "import geopandas as gpd\n",
    "import requests\n",
    "import geojson\n",
    "\n",
    "import matplotlib\n",
    "%matplotlib inline\n",
    "from shapely.geometry import Polygon, LineString, Point\n",
    "import matplotlib.pyplot as plt\n",
    "import shapely.speedups\n",
    "import folium\n",
    "import contextily as ctx\n",
    "from pyproj import CRS\n",
    "\n",
    "import osmnx as ox\n",
    "import networkx as nx\n",
    "\n",
    "import contextily as ctx\n",
    "import mplleaflet\n",
    "\n",
    "from folium.features import FeatureGroup, GeoJson, TopoJson, Marker\n",
    "from folium.plugins import MarkerCluster, Search\n",
    "from folium.utilities import parse_options\n",
    "import cgi\n",
    "from geopandas.tools import geocode\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/vipy/anaconda3/lib/python3.7/site-packages/pyproj/crs.py:77: FutureWarning: '+init=<authority>:<code>' syntax is deprecated. '<authority>:<code>' is the preferred initialization method.\n",
      "  return _prepare_from_string(\" \".join(pjargs))\n",
      "/home/vipy/anaconda3/lib/python3.7/site-packages/pyproj/crs.py:77: FutureWarning: '+init=<authority>:<code>' syntax is deprecated. '<authority>:<code>' is the preferred initialization method.\n",
      "  return _prepare_from_string(\" \".join(pjargs))\n",
      "/home/vipy/anaconda3/lib/python3.7/site-packages/pyproj/crs.py:77: FutureWarning: '+init=<authority>:<code>' syntax is deprecated. '<authority>:<code>' is the preferred initialization method.\n",
      "  return _prepare_from_string(\" \".join(pjargs))\n",
      "/home/vipy/anaconda3/lib/python3.7/site-packages/pyproj/crs.py:77: FutureWarning: '+init=<authority>:<code>' syntax is deprecated. '<authority>:<code>' is the preferred initialization method.\n",
      "  return _prepare_from_string(\" \".join(pjargs))\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "single positional indexer is out-of-bounds",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-13-4beff630d2a5>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     56\u001b[0m \u001b[0mdest\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgeocode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdestAddress\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mprovider\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'nominatim'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muser_agent\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'autogis_xx'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 58\u001b[0;31m \u001b[0mMarker\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0morig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'geometry'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0morig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'geometry'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpopup\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'Lähtöpaikka'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd_to\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mm\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     59\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     60\u001b[0m \u001b[0mSearch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlayer\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnodesGeoJson\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msearch_zoom\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;36m18\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mposition\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"topleft\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd_to\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mm\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py\u001b[0m in \u001b[0;36m__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   1416\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mKeyError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1417\u001b[0m                     \u001b[0;32mpass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1418\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_getitem_tuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1419\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1420\u001b[0m             \u001b[0;31m# we by definition only have the 0th axis\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py\u001b[0m in \u001b[0;36m_getitem_tuple\u001b[0;34m(self, tup)\u001b[0m\n\u001b[1;32m   2090\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_getitem_tuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtup\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2091\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2092\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_has_valid_tuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtup\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2093\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2094\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_getitem_lowerdim\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtup\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py\u001b[0m in \u001b[0;36m_has_valid_tuple\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    233\u001b[0m                 \u001b[0;32mraise\u001b[0m \u001b[0mIndexingError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Too many indexers\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    234\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 235\u001b[0;31m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_validate_key\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mk\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    236\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    237\u001b[0m                 raise ValueError(\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py\u001b[0m in \u001b[0;36m_validate_key\u001b[0;34m(self, key, axis)\u001b[0m\n\u001b[1;32m   2012\u001b[0m             \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2013\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2014\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_validate_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2015\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2016\u001b[0m             \u001b[0;31m# a tuple should already have been caught by this point\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py\u001b[0m in \u001b[0;36m_validate_integer\u001b[0;34m(self, key, axis)\u001b[0m\n\u001b[1;32m   2086\u001b[0m         \u001b[0mlen_axis\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_axis\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2087\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mkey\u001b[0m \u001b[0;34m>=\u001b[0m \u001b[0mlen_axis\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mkey\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0mlen_axis\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2088\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"single positional indexer is out-of-bounds\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2089\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2090\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_getitem_tuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtup\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: single positional indexer is out-of-bounds"
     ]
    }
   ],
   "source": [
    "def search_for_path(origX, origY, destX, destY, graph, nodes, edges):\n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "etasonAlueet = gpd.read_file(\"Lahtotiedot/Erikoistason_alueet_shp-export/HKRPTY_esteettomyys_erikois_alue_areas.shp\")\n",
    "\n",
    "etasonReitit = gpd.read_file(\"Lahtotiedot/Erikoistason_reitti_toteutunut/HKRPTY_esteettomyys_TOT_erikois_reitti_lines.shp\")\n",
    "\n",
    "aaniopasteet = gpd.read_file(\"Lahtotiedot/HELSINKI1_OjalaKi_20191219_160434 (1)/HKRPTY_esteettomyys_TOT_aaniopas_suojat.tab\")\n",
    "\n",
    "etasonReititWGS84 = etasonReitit.to_crs(epsg=4326)\n",
    "aaniopasteetWGS84 = aaniopasteet.to_crs(epsg=4326)\n",
    "etasonAlueetWGS84 = etasonAlueet.to_crs(epsg=4326)\n",
    "\n",
    "polyBorder = Polygon([(24.917896, 60.183715), (24.965640, 60.186536),\n",
    "                     (24.965640, 60.160687), (24.917896, 60.160687)])\n",
    "graph = ox.graph_from_bbox(north=60.183715, south=60.160687, east=24.965640, \n",
    "                           west=24.917896, network_type='walk')\n",
    "\n",
    "\n",
    "nodes, edges = ox.graph_to_gdfs(graph, nodes=True, edges=True)\n",
    "convexHull = edges.unary_union.convex_hull\n",
    "\n",
    "etasonReititWGS84 = etasonReititWGS84.loc[(etasonReititWGS84['geometry'].within(convexHull))]\n",
    "etasonAlueetWGS84 = etasonAlueetWGS84.loc[(etasonAlueetWGS84['geometry'].within(convexHull))]\n",
    "aaniopasteetWGS84 = aaniopasteetWGS84.loc[(aaniopasteetWGS84['geometry'].within(convexHull))]\n",
    "\n",
    "center = convexHull.centroid\n",
    "center.x\n",
    "\n",
    "\n",
    "nodesGeoJson = GeoJson(nodes, name=\"places\")\n",
    "etasonReititGeoJson = GeoJson(etasonReititWGS84, name=\"etasonReitit\")\n",
    "etasonAlueetGeoJson = GeoJson(etasonAlueetWGS84, name=\"etasonAlueet\")\n",
    "aaniopasteetGeoJson = GeoJson(aaniopasteetWGS84, name=\"aaniopasteet\")\n",
    "\n",
    "aaniopasteetWGS84['centroid'] = aaniopasteetWGS84['geometry'].centroid\n",
    "\n",
    "\n",
    "m = folium.Map(location= [center.y, center.x], zoom_start=14, min_zoom = 13, \n",
    "               max_zoom= 20, control_scale=True, tiles=\"CartoDB Positron\")\n",
    "\n",
    "etasonReititGeoJson.add_to(m)\n",
    "etasonAlueetGeoJson.add_to(m)\n",
    "aaniopasteetGeoJson.add_to(m)\n",
    "for index, row in aaniopasteetWGS84.iterrows():\n",
    "    Marker(location=[row['centroid'].y, row['centroid'].x], popup='Ääniopaste').add_to(m)\n",
    "\n",
    "\n",
    "form = cgi.FieldStorage()\n",
    "\n",
    "origAddress = form.getvalue('Origin address')\n",
    "destAddress = form.getvalue('Destination address')\n",
    "\n",
    "\n",
    "# Geocode addresses using Nominatim. Remember to provide a custom \"application name\"\n",
    "# in the user_agent parameter!\n",
    "\n",
    "orig = geocode(origAddress, provider='nominatim', user_agent='autogis_xx', timeout=4)\n",
    "dest = geocode(destAddress, provider='nominatim', user_agent='autogis_xx', timeout=4)\n",
    "\n",
    "Marker([orig.iloc[0, 'geometry'].y, orig.iloc[0, 'geometry'].x], popup='Lähtöpaikka').add_to(m)\n",
    "\n",
    "Search(layer=nodesGeoJson, search_zoom= 18, position=\"topleft\").add_to(m)\n",
    "m.add_child(Search(nodesGeoJson))\n",
    "\n",
    "m.save(\"Esteetomyyskartta1.html\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<form name=\"search\" action=\"~/search_engine.py\" method=\"post\">\n",
    "        <input type=\"text\" name=\"Origin address\" placeholder=\"Search origin address\">\n",
    "        <input type=\"text\" name=\"Destination address\" placeholder=\"Search destination address\">\n",
    "        <input type=\"submit\" value=\"Search\">\n",
    "        </form> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "geopandas.geodataframe.GeoDataFrame"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(orig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
