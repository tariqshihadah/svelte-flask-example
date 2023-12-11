import geopandas as gpd
from geodatasets import get_path

#
# DATA LOADING HELPERS
#

def _load_raw_geojson(content, crs=None):
    # Load data
    data = gpd.read_file(content, driver='GeoJSON')
    # Reproject if requested
    if not crs is None:
        data = data.to_crs(crs)
    # Return data
    return data

def _load_from_path(path, crs=None):
    # Load data
    data = gpd.read_file(path)
    # Reproject if requested
    if not crs is None:
        data = data.to_crs(crs)
    # Convert to JSON
    try:
        data.to_json()
    except:
        data = {
            'error': 100,
            'message': f'Unable to load input data path: {path}'
        }
    # Return data
    return data

def _load_sample_data(label, crs=None):
    # Retrieve sample data path
    path = get_path(label)
    # Load data
    return _load_from_path(path, crs=crs)