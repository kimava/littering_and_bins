# Do Garbage Bins Reduce Illegal Littering?

## 1. Project Overview
### 1.1 Overview
- **Objective** : Investigate whether the availability of garbage bins influences the occurrence of illegal littering.
- **📊 Analysis report** : You can **find it [here!](https://inky-trunk-6f7.notion.site/Do-Garbage-Bins-Reduce-Illegal-Littering-15304b8816d980c68cd6fbcd2688c53a?pvs=74)**
- **Disclaimer**
  - This project is a personal side project.
  - It is focused only on two districts (Yongsan and Gangnam) due to limited data availability.
  - The findings may not be fully representative of Seoul as a whole.
  - The analysis does not account for other factors that might influence littering, such as population density, street infrastructure, or behavioral patterns.

### 1.2 Tech Stack
- **Databases & Programming:** MySQL, Python (Pandas, Matplotlib, Folium)
- **Geo-coding Tools:** Geopy, Naver(Korean Platform) Search API

## 2. Data
### 2.1 Sources
- **Garbage Bin Locations**: [Open Data Portal of South Korea](https://www.data.go.kr/en/index.do)
- **Illegal Littering Locations**: [Open Data Portal of South Korea](https://www.data.go.kr/en/index.do) <br/>
- **The raw data contains only address information without latitude or longitude.*

### 2.2 Data Descriptions
The DB has the following tables:
- `bin_locations_raw` : original bin locations in Seoul without latitude or longitude. <br/>
  
  | Field            | Type         | Null |
  | ---------------- | ------------ | ---- |
  | id               | int          | NO   |
  | district         | varchar(255) | YES  |
  | address          | varchar(255) | YES  |
  | detailed_address | varchar(255) | YES  |
  | location_type    | varchar(255) | YES  |
  | bin_type         | varchar(255) | YES  |
  | created_at       | timestamp    | YES  |
  | updated_at       | timestamp    | YES  |
  
- `bin_locations` : simplified data containing only district and address.

  | Field      | Type         | Null |
  | ---------- | ------------ | ---- |
  | id         | int          | NO   |
  | district   | varchar(255) | YES  |
  | address    | varchar(255) | YES  |
  | latitude   | double       | YES  |
  | longitude  | double       | YES  |
  | created_at | timestamp    | YES  |
  | updated_at | timestamp    | YES  |

- `bin_locations_focus` : filtered data for Yongsan and Gangnam districts, focusing on illegal littering analysis.

  | Field      | Type         | Null |
  | ---------- | ------------ | ---- |
  | id         | int          | NO   |
  | district   | varchar(255) | YES  |
  | address    | varchar(255) | YES  |
  | latitude   | double       | YES  |
  | longitude  | double       | YES  |
  | created_at | timestamp    | YES  |
  | updated_at | timestamp    | YES  |

- `illegal_littering` : locations of illegal littering in Yongsan and Gangnam districts.

  | Field       | Type         | Null |
  | ----------- | ------------ | ---- |
  | id          | int          | NO   |
  | district    | varchar(255) | YES  |
  | address     | varchar(255) | YES  |
  | create_time | timestamp    | YES  |
  | latitude    | double       | YES  |
  | longitude   | double       | YES  |

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
3. Install the dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the project
   ```
   python3 -m analysis.scripts.run_analysis
   ```

## 4. Analysis Overview
Run the project to explore visualisations:
- 📊 **Summary Statistics**: Minimum, maximum, mean, and median distances to garbage bins.
- 📈 **Histogram**: Analyse the distribution of distances between illegal littering locations and the nearest garbage bin.
- 📉 **Box Plot**: Examine data spread and identify outliers.
- 🗺️ **Interactive Map**: Explore bin locations and illegal littering spots visually.

✨ **[Live Map Link](https://transcendent-chimera-2544be.netlify.app/)**  

## 5. Future Improvements
- **Expand data collection:** Include additional districts and variables such as population density, road infrastructure, and repeated littering incidents.
- **Incorporate behavioural insights:** Study behavioural and environmental factors contributing to illegal littering to complement the geospatial analysis.
