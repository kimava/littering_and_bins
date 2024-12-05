import requests
import folium
from folium.plugins import MarkerCluster
import numpy as np
import matplotlib.pyplot as plt

def create_folium_map(bin_data, littering_data, distances):

    # URL for the GeoJSON file containing Seoul administrative districts
    url = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
    response = requests.get(url)
    seoul_geo = response.json() # Loads data

    # Center coords of Seoul
    center_lat, center_lng = 37.5721, 126.9854
    
    # Creates Folium map
    folium_map = folium.Map(
        location = [center_lat, center_lng],
        zoom_start = 12,
        tiles = 'CartoDB positron'
    )
    
    # Adds district boundaries (using GeoJSON)
    folium.GeoJson(
        seoul_geo,
        name = "Seoul Boundary",
        style_function = lambda x: {
            'fillColor': 'none', 'color': 'blue', 'weight': 2
        }
    ).add_to(folium_map)
    
    # Adds marker cluster to address overlapping markers issue
    littering_cluster = MarkerCluster(name="Littering Locations").add_to(folium_map)
    bin_cluster = MarkerCluster(name="Bin Locations").add_to(folium_map)
    
    # Classifies distance data (sets color)
    color_map = {
        'close': 'green',    # Close distance (0 - 100m)
        'medium': 'orange',  # Medium distance (100 - 200m)
        'far': 'red'         # Far distance (greater than 200m)
    }

    # Sets color baesd on distance
    def get_color(distance):
        if distance <= 100:
            return color_map['close']
        elif distance <= 200:
            return color_map['medium']
        else:
            return color_map['far']
    
    # Adds littering location markers
    for index, row in littering_data.iterrows():
        lat, lng = row['latitude'], row['longitude']
        
        # Checks if distances[index] is valid
        if index < len(distances):
            distance = distances[index]
        else:
            distance = None
        
        color = get_color(distance) if distance is not None else 'gray'  # Adds a gray color if distance is None

        if isinstance(distance, (int, float)):
            popup_text = f"Distance to nearest bin: {distance:.2f} meters"
        else:
            popup_text = "Distance to nearest bin: N/A"
        folium.CircleMarker(
            location=[lat, lng],
            radius = 5,
            color = color,
            fill = True,
            fill_color = color,
            fill_opacity = 0.7,
            popup = popup_text
        ).add_to(littering_cluster)
    
    # Adds littering location markers
    for _, row in bin_data.iterrows():
        lat, lng = row['latitude'], row['longitude']
        folium.Marker(
            location = [lat, lng],
            icon = folium.Icon(color = 'blue', icon = 'trash'),
            popup="Bin Location"
        ).add_to(bin_cluster)
    
    # Adds legend
    legend = '''
        <div style="position:fixed;
                left: 50px;
                bottom: 50px;  
                width: 200px;
                height: 140px;
                padding: 10px;
                font-size: 14px;
                background-color: white; 
                z-index: 10000; 
                border: 1px solid black;">
            <b>Legend:</b><br>
            <i style="background: green; color: green;">&nbsp;&nbsp;&nbsp;</i> Close (0-100m)<br>
            <i style="background: orange; color: orange;">&nbsp;&nbsp;&nbsp;</i> Medium (100-200m)<br>
            <i style="background: red; color: red;">&nbsp;&nbsp;&nbsp;</i> Far (>200m)<br>
            <i style="background: blue; color: blue;">&nbsp;&nbsp;&nbsp;</i> Bin Locations<br>
        </div>
    '''
    folium_map.get_root().html.add_child(folium.Element(legend))
    
    return folium_map

def create_distance_distribution_plot(distances):
    # Divides the interval at 5 meter intervals
    bins = np.arange(0, np.max(distances) + 5, 5)

    # Visualises the distance data as a histogram
    fig, ax = plt.subplots(figsize = (10, 6))
    ax.hist(distances, bins = bins, color = 'salmon', edgecolor = 'black')
    ax.set_title("Distribution of Nearest Bin Distances From Illegal Littering Location")
    ax.set_xlabel("Distance (meters)")
    ax.set_ylabel("Frequency")
    ax.grid(True)
    
    return fig, ax
