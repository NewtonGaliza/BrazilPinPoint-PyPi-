import argparse
import folium

parser = argparse.ArgumentParser(description='Take lat and long to pin the map')
parser.add_argument('--lat', action='store', dest='lat', required='True', help='Latitude')
parser.add_argument('--long', action='store', dest='long', required='True', help='longitude')
parser.add_argument('--filename', action='store', dest='filename', required='True', help='File Name')

args = parser.parse_args()
lat = float(args.lat)
long = float(args.long)
filename = args.filename+'.html'

brazil = folium.Map(

  location = [-16.1237611, -59.9219642],
  zoom_start=4

)

folium.Marker(

  location = [lat, long],
  popup = 'Latitude {latitude} \n Longitude {longitude}'.format(latitude=str(lat), longitude=str(long))
  
).add_to(brazil)


brazil.save(filename)
