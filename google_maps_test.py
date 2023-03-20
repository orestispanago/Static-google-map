import pandas as pd
import requests

GOOGLE_MAPS_API_KEY = ""

center = "Patras"
zoom = 12
size = "640x600"
color = "green"
label = 3


def create_map_markers():
    sensors = pd.read_csv("sensors.csv")
    markers = []
    for index, row in sensors.iterrows():
        sensor_lat = row["latitude"]
        sensor_lon = row["longitude"]
        markers.append(
            f"color:{color}%7Clabel:{label}%7C{sensor_lat},{sensor_lon}%7C"
        )
    return "".join(markers)


def plot_map(
    center="Patras",
    zoom=12,
    size="750x600",
    markers="",
    save_as="map.png",
    google_maps_api_key=GOOGLE_MAPS_API_KEY,
):
    url = (
        f"https://maps.googleapis.com/maps/api/staticmap?"
        f"center={center}&"
        f"zoom={zoom}&"
        f"size={size}&"
        f"markers={markers}&"
        f"key={google_maps_api_key}"
    )
    r = requests.get(url)
    print(r.status_code)
    with open(save_as, "wb") as f:
        f.write(r.content)


plot_map(markers=create_map_markers())
