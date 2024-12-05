import requests
from shapely.geometry import shape, Point

def filter_data_within_bounds(bin_data, littering_data):
    # URL for the GeoJSON file containing Seoul administrative districts
    url = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
    response = requests.get(url)
    seoul_geo = response.json() # Loads data
    
    # Defines the boundaries of Yongsan-gu and Gangnam-gu (defined as polygons)
    target_districts = ['Yongsan-gu', 'Gangnam-gu']
    district_geometries = {}

    for feature in seoul_geo['features']:
        district_name = feature['properties']['name_eng']
        if district_name in target_districts:
            # Reads coordinates from 'geometry' and create polygon objects
            polygon = shape(feature['geometry'])
            district_geometries[district_name] = polygon

    # Checks if the given coordinates are within the polygon
    def is_within_bounds(lat, lng, district):
        point = Point(lng, lat)  # Converts coordinates to a point
        district_polygon = district_geometries[district]
        return district_polygon.contains(point)

    # Filters bin_data and littering_data
    filtered_bin_data = bin_data[bin_data.apply(lambda row: any(
        is_within_bounds(row['latitude'], row['longitude'], district) for district in target_districts), axis=1)]
    
    filtered_littering_data = littering_data[littering_data.apply(lambda row: any(
        is_within_bounds(row['latitude'], row['longitude'], district) for district in target_districts), axis=1)]

    return filtered_bin_data, filtered_littering_data
