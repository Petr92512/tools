import requests as re
import json
import webbrowser

class Flickr():
	def __init__(self, tags):
		self.tags = tags
		self.flickr_key = 'YOUR_API_KEY'

	def get_photo(self):

		baseurl = 'https://api.flickr.com/services/rest/'
		
		#tags = input("Enter which tag photo u want : \t")
		params_dict = {} 
		params_dict["method"] = "flickr.photos.search" 	# methods in api docs
		params_dict["api_key"] = self.flickr_key 			#api_key for authentication 
		params_dict["tags"] = self.tags 						# must be a comma separated string to work correctly
		params_dict["tag_mode"] = "all"
		params_dict["per_page"] = 1 					# photos limit
		params_dict["media"] = "photos" 				# media type
		params_dict["format"] = "json" 					# o/p formate 
		params_dict["nojsoncallback"] = 1
		params_dict["geo_context"] = 2 					#1:indoor , 2:outdoor
		res = re.get(baseurl , params = params_dict)
		#print(res.json())
		photos = res.json()
		photo_urls = photos['photos']['photo']
		#print(photo_urls)
		urls = []
		for photo in photo_urls:
		    owner = photo['owner']
		    photo_id = photo['id']
		    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id) # make url
		    urls.append(url)

		return urls
    	#webbrowser.open(url) # will open url in the web browser

	def __repr__(self):
		return f"Images of {self.tag}"
		
#test = Flickr('mountains')
#test.get_photo()
