from scipy.spatial import KDTree

def calculate_distances(bin_data, littering_data):
    # # Converts bin coordinates and illegal littering coordinates to numpy arrays
    bin_coords = bin_data[['latitude', 'longitude']].to_numpy()
    littering_coords = littering_data[['latitude', 'longitude']].to_numpy()

    # Creats KDTree
    tree = KDTree(bin_coords)

    # # Calculates the distance from each illegal littering coordinate to the nearest bin
    distances, _ = tree.query(littering_coords)
    distances_in_meters = distances * 111100  # 1 degree ≈ 111.1 km -> meters

    return distances_in_meters
