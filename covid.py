import COVID19Py
import requests
covid19 = COVID19Py.COVID19()
covid19 = COVID19Py.COVID19(data_source="csbs")
latest = covid19.getLatest()


locations = covid19.getLocations(rank_by='confirmed')
print(locations)