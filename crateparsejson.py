import json

class parse_crates(object):
	"""tools to convert Patchy's json data into dictionaries usable by cratesim library"""
	def __init__(self, fp):
		file = open(fp)
		self.data = json.load(file)  #parse json
		self.crates = list()   #create list of crate names
		for crate in self.data:
			self.crates.append(crate['n'])

	def get_crate(self,crate_name):   #given a crate name, return all corresponding data
		for crate in self.data:
			if(crate['n'] == crate_name):
				return crate
		raise KeyError

	def get_items(self,crate):   #given crate data, return dictionary of items with associated probabilities
		items = dict()
		item_dict = crate['i']
		for item in item_dict:
			items[item["n"]] = float(item['o'])
		return items

	def seperate_epics(self,items):  #given items, split into epic items and other items for use with cratesim library 
		epic_dict = dict()
		other_dict = dict()
		for key in items.keys():
			if("**" in key):
				epic_dict[key] = items[key]
			else:
				other_dict[key] = items[key]
		return epic_dict,other_dict

	def get_price(self,crate_name): #get the price of a crate, given its name
		dat = self.get_crate(crate_name)
		return dat['p']

