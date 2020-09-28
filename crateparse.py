class parse_crate(object):
	"""docstring for parse_crate"""
	def __init__(self, raw_data):
		self.raw_data = str(raw_data.split("{",1)[1])
		self.info,self.items = self.raw_data.split("items: ")
		self.name = self.info.split("\n")[1].split(":")[1][2:-2]
		self.price = int(self.info.split("\n")[2].split(":")[1][1:-1])
		self.date = self.info.split("\n")[3].split("Date")[1][:-1]
		if("true" in self.info.split("\n")[4]):
			self.is_duplicate_protected = True
		else:
			self.is_duplicate_protected = False
		self.season = int(self.info.split("\n")[5].split(":")[1][1:-1])
		self.info = self.info.replace("{","").replace("}","").replace("[","").replace("]","")
		self.items = self.items.replace("{","").replace("}","").replace("[","").replace("]","").replace(";","")[0:-4].split("\n")
		for i in self.items:
			if(len(i) < 5):
				self.items.pop(self.items.index(i))
		item_dict = dict()
		for item in self.items:
			item_dict[item.split(",")[0].split(":")[1][2:][:-1]] = float(item.split(",")[1].split(":")[1][1:])
		self.item_dict = item_dict

	def seperate_epics(self,items):
		epic_dict = dict()
		other_dict = dict()
		for key in items.keys():
			if("**" in key):
				epic_dict[key] = items[key]
			else:
				other_dict[key] = items[key]
		return epic_dict,other_dict
