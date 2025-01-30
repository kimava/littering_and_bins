# Visualising the Distance Between Rubbish Bins and Littering

## 1. About this Project
### 1.1 📌 Overview
This project focuses on **data visualisation** while incorporating key data processing techniques. It explores the **spatial relationship between rubbish bins and littering locations** through mapping and statistical summaries. The primary goal is to enhance **data wrangling, database management, and visualisation skills** using real-world geographical data.

### 1.2 🎯 Objective
  - **Data Collection & Processing:** Collected raw location data (addresses) from the Open Data Portal, then used Geopy to convert these addresses into latitude and longitude. The processed data was stored in MySQL, allowing for efficient querying and management.
  - **Data Cleaning & Wrangling:** Filtered out errors and inconsistencies in the data using Python (Pandas) for accurate analysis. The dataset was further cleaned to focus on Yongsan and Gangnam districts for a more targeted study.
  - **Data Analysis & Visualisation:** Employed SQL queries to extract relevant data, and used Python scripts (Matplotlib, Folium) to generate summary statistics and interactive visualisations.

### 1.3 🛠️ Tech Stack
- **Databases & Programming:** MySQL (Database creation & management), Python (Pandas for data wrangling, Matplotlib for analysis, Folium for visualisation)
- **Geo-coding Tools:** Geopy (for adding latitude and longitude to addresses), Naver Search API


### 1.4 🔍 Key Notes
  - This is a personal project for visualisation practice.
  - The dataset is limited to two districts (Yongsan and Gangnam) due to limited data availability.
  - The project does not aim to provide statistical insights or causal analysis.

### 1.5 📊 Results
You can view them [here!](https://inky-trunk-6f7.notion.site/Do-Garbage-Bins-Reduce-Illegal-Littering-15304b8816d980c68cd6fbcd2688c53a?pvs=74)**

<br/>

## 2. Data
### 2.1 Sources
- **Garbage Bin Locations**: [Open Data Portal of South Korea](https://www.data.go.kr/en/index.do)
- **Illegal Littering Locations**: [Open Data Portal of South Korea](https://www.data.go.kr/en/index.do) <br/>
  (The original data only includes addresses, without latitude or longitude.)

### 2.2 Database Structure
The dataset is structured into four tables:

| Table Name              | Description                                               |
|-------------------------|-----------------------------------------------------------|
| `bin_locations_raw`     | Original dataset with garbage bin locations in Seoul (without coordinates). |
| `bin_locations`         | Processed dataset with latitude and longitude added.     |
| `bin_locations_focus`   | Filtered dataset for Yongsan and Gangnam.                |
| `illegal_littering`     | Recorded littering locations in Yongsan and Gangnam.     |

<br/>

## 3. Installation & Usage Instructions
1. Clone the repository
   ```
   git clone https://github.com/kimava/littering_and_bins.git
   ```
2. Create a virtual environment
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the project
   ```
   python3 -m analysis.scripts.run_analysis
   ```

<br/>

## 4. Summary
This project showcases various data processing and visualisation techniques, including:
- **Data Processing:** Collected raw data and used Geopy to convert addresses into geospatial coordinates, then stored them in a MySQL database for efficient management.
- **Data Wrangling:** Cleaned and filtered data using Python (Pandas), removing inconsistencies and anomalies to ensure accuracy.
- **Data Analysis & Visualisation:**
  - 📊 **Summary Statistics**: Calculated the minimum, maximum, mean, and median distances to the nearest garbage bins.
  - 📈 **Histogram**: Analysed the distribution of distances between littering locations and the nearest bins.
  - 📉 **Box Plot**: Identified outliers and examined data spread.
  - 🗺️ **Interactive Map**: Used Folium to create a map for visual exploration of bin locations and littering hotspots.

✨ **[Live Map Link](https://transcendent-chimera-2544be.netlify.app/)**
![image](https://github.com/user-attachments/assets/00b7c7e7-7ab5-4a51-ac54-7018acb309bc)


