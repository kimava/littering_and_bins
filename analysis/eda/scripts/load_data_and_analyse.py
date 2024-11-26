import pandas as pd
import matplotlib.pyplot as plt
from src.db.db_connector import create_connection

db = create_connection()

query_bins = "SELECT * FROM bin_locations_focus"
query_littering = "SELECT * FROM illegal_littering"

data_bins = pd.read_sql_query(query_bins, db)
data_littering = pd.read_sql_query(query_littering, db)

# 1. Basic Info and Summary
with open("bin_locations_info.txt", "w") as f:
    data_bins.info(buf=f)

with open("illegal_littering_info.txt", "w") as f:
    data_littering.info(buf=f)

data_bins.describe().to_csv("bin_locations_summary.csv")
data_littering.describe().to_csv("illegal_littering_summary.csv")


# 2. Define Seoul's geographical range
min_lat, max_lat = 37.413294, 37.715133
min_lng, max_lng = 126.734086, 127.269311

# Filter out data outside Seoul's range
out_of_seoul_bins = data_bins[
    (data_bins['latitude'] < min_lat) | 
    (data_bins['latitude'] > max_lat) | 
    (data_bins['longitude'] < min_lng) | 
    (data_bins['longitude'] > max_lng)
]

out_of_seoul_littering = data_littering[
    (data_littering['latitude'] < min_lat) | 
    (data_littering['latitude'] > max_lat) | 
    (data_littering['longitude'] < min_lng) | 
    (data_littering['longitude'] > max_lng)
]

print(f"Number of bins outside Seoul: {len(out_of_seoul_bins)}")
print(f"Number of illegal littering outside Seoul: {len(out_of_seoul_littering)}")

# 3. Delete out-of-range data from the database
with db.cursor() as cursor:
    bins_to_delete = tuple(out_of_seoul_bins['id'].tolist())
    if bins_to_delete:
        cursor.execute(f"""
                    DELETE FROM bin_locations_focus
                    WHERE id IN {bins_to_delete}
                """)
        print(f"Deleted {len(bins_to_delete)} bins data from the database.")
    
    littering_ids_to_delete = tuple(out_of_seoul_littering['id'].tolist())
    if littering_ids_to_delete:
        cursor.execute(f"""
                    DELETE FROM illegal_littering
                    WHERE id IN {littering_ids_to_delete}
                """)
        print(f"Deleted {len(littering_ids_to_delete)} illegal littering data from the database.")

    db.commit()

# 4. Data Visualization
# Bin locations
plt.scatter(data_bins['longitude'], data_bins['latitude'], c='blue', label='Within Seoul')
plt.scatter(out_of_seoul_bins['longitude'], out_of_seoul_bins['latitude'], c='green', label='Outside Seoul')
plt.title('Distribution of Bin Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.xlim(126.734086, 127.269311)  # x-axis range (longitude)
plt.ylim(37.413294, 37.715133)    # y-axis range (latitude)

plt.xticks([x * 0.1 + 126.734086 for x in range(int((127.269311 - 126.734086) / 0.1) + 1)])
plt.yticks([y * 0.02 + 37.413294 for y in range(int((37.715133 - 37.413294) / 0.02) + 1)])

# Format the ticks to display 2 decimal digits
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))

plt.legend()
plt.savefig("distribution_of_bin_locations.png")
plt.show()

# Illegal littering
plt.scatter(data_littering['longitude'], data_littering['latitude'], c='red', label='Within Seoul')
plt.scatter(out_of_seoul_littering['longitude'], out_of_seoul_littering['latitude'], c='yellow', label='Outside Seoul')
plt.title('Distribution of Illegal Littering Records')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.xlim(126.734086, 127.269311)  # x-axis range (longitude)
plt.ylim(37.413294, 37.715133)    # y-axis range (latitude)

plt.xticks([x * 0.1 + 126.734086 for x in range(int((127.269311 - 126.734086) / 0.1) + 1)])
plt.yticks([y * 0.02 + 37.413294 for y in range(int((37.715133 - 37.413294) / 0.02) + 1)])

# Format the ticks to display 2 decimal digits
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))

plt.legend()
plt.savefig("distribution_of_illegal_littering_records.png")
plt.show()

# 5. Save filtered data locally
data_bins_in_seoul = data_bins.drop(out_of_seoul_bins.index)
data_littering_in_seoul = data_littering.drop(out_of_seoul_littering.index)

data_bins_in_seoul.to_csv("bin_locations_in_seoul.csv", index=False)
data_littering_in_seoul.to_csv("illegal_littering_in_seoul.csv", index=False)
