from skyfield.api import load, wgs84
ts = load.timescale()

iss_url = "http://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE"
satellite_list = load.tle_file(iss_url)
Iss = satellite_list[0];

t = ts.now()
geocentric = Iss.at(t)

lat, lon = wgs84.latlon_of(geocentric)
print("Latitude:", lat)
print("Longitude:", lon)