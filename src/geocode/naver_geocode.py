import requests
from src.geocode.naver_config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET

def get_coordinates_from_naver(address):
    url = f"https://openapi.naver.com/v1/search/local.json?query={{{address}}}"

    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if "items" in data and len(data["items"]) > 0:
                item = data["items"][0]
                mapx = item["mapx"]
                mapy = item["mapy"]

                latitude = float(str(mapy)[:-7] + "." + str(mapy)[-7:])
                longitude = float(str(mapx)[:-7] + "." + str(mapx)[-7:])
                
                return latitude, longitude
            else:
                return None, None
        else:
            return None, None
    except Exception as e:
        print(f"Error: Naver API request raised an exception - {str(e)}")
        return None, None
