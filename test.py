import pgeocode
import folium
import geopandas as gpd

# pgeocodeを使用して日本の郵便番号情報を取得
nomi = pgeocode.Nominatim('JP')

# 例としていくつかの郵便番号をリストにする
postal_codes = ['100-0001', '150-0001', '060-0001', '900-0001']

# 郵便番号に基づいて位置情報を取得
locations = []
for code in postal_codes:
    location = nomi.query_postal_code(code)
    if not location.empty:
        lat, lon = location.latitude, location.longitude
        locations.append((lat, lon, code))

# folium地図オブジェクトを作成
map_japan = folium.Map(location=[36.2048, 138.2529], zoom_start=5)

# 郵便番号の位置を地図上にマーク
for lat, lon, code in locations:
    folium.Marker(location=[lat, lon], popup=f'Postal Code: {code}').add_to(map_japan)

# 地図を保存
map_japan.save("japan_map.html")

# Geopandasを使用して日本の地理データを読み込み、地図をプロットする例
# ここでは、シェープファイルのパスを指定する必要があります。例: 'path/to/japan_shapefile.shp'
# gdf = gpd.read_file('path/to/japan_shapefile.shp')

# 地図をプロット（これはオプションです）
# gdf.plot()
# plt.show()
