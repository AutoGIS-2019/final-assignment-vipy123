
from branca.element import CssLink, Figure, JavascriptLink, MacroElement
from jinja2 import Template
from folium import Map
from folium.features import FeatureGroup, GeoJson, TopoJson
from folium.plugins import MarkerCluster
from folium.utilities import parse_options

class Search(MacroElement):
    
    """
    Adds a search tool to your map.
    Parameters
    ----------
    layer: GeoJson, TopoJson, FeatureGroup, MarkerCluster class object.
        The map layer to index in the Search view.
    search_label: str, optional
        'properties' key in layer to index Search, if layer is GeoJson/TopoJson.
    search_zoom: int, optional
        Zoom level to set the map to on match.
        By default zooms to Polygon/Line bounds and points
        on their natural extent.
    geom_type: str, default 'Point'
        Feature geometry type. "Point", "Line" or "Polygon"
    position: str, default 'topleft'
        Change the position of the search bar, can be:
        'topleft', 'topright', 'bottomright' or 'bottomleft',
    placeholder: str, default 'Search'
        Placeholder text inside the Search box if nothing is entered.
    collapsed: boolean, default False
        Whether the Search box should be collapsed or not.
    **kwargs.
        Assorted style options to change feature styling on match.
        Use the same way as vector layer arguments.
    See https://github.com/stefanocudini/leaflet-search for more information.
    """

    def __init__(self, layer, search_label=None, search_zoom=None, geom_type='Point',
                 position='topleft', placeholder='Search',
                 collapsed=False, **kwargs):
        super(Search, self).__init__()
        assert isinstance(layer, (GeoJson, MarkerCluster, FeatureGroup, TopoJson, Point)
                         ), 'Search can only index FeatureGroup, ' \
                            'MarkerCluster, GeoJson, and TopoJson layers at ' \
                            'this time.'
        self.layer = layer
        self.search_label = search_label
        self.search_zoom = search_zoom
        self.geom_type = geom_type
        self.position = position
        self.placeholder = placeholder
        self.collapsed = collapsed
        self.options = parse_options(**kwargs)
        
    def test_params(self, keys):
        if keys is not None and self.search_label is not None:
            assert self.search_label in keys, "The label '{}' was not " \
                                              "available in {}" \
                                              "".format(self.search_label, keys)
        assert isinstance(self._parent, Map), "Search can only be added to " \
                                              "folium Map objects."
    
    def render(self, **kwargs):
        if isinstance(self.layer, GeoJson):
            keys = tuple(self.layer.data['features'][0]['properties'].keys())
        elif isinstance(self.layer, TopoJson):
            obj_name = self.layer.object_path.split('.')[-1]
            keys = tuple(self.layer.data['objects'][obj_name]['geometries'][0]['properties'].keys())  # noqa
        else:
            keys = None
        self.test_params(keys=keys)
        super(Search, self).render()

        figure = self.get_root()
        assert isinstance(figure, Figure), ('You cannot render this Element '
                                            'if it is not in a Figure.')

        figure.header.add_child(
            JavascriptLink('https://cdn.jsdelivr.net/npm/leaflet-search@2.9.7/dist/leaflet-search.min.js'),  # noqa
            name='Leaflet.Search.js'
        )

        figure.header.add_child(
            CssLink('https://cdn.jsdelivr.net/npm/leaflet-search@2.9.7/dist/leaflet-search.min.css'),  # noqa
            name='Leaflet.Search.css'
        )