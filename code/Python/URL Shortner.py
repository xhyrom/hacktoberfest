from pyshorteners import Shortener

long_url = input("Enter The URL")

API_Key = 'AIzaSyBBS...jXKIGh1fNU'

url_shortener = Shortener('Google', api_key = API_Key)
print ("Short URL is {}".format(url_shortener.short(long_url)))
