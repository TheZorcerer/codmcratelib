from random import random


class crate(object):
	"""object to simulate a crate"""
	def __init__(self,epic_dict,other_dict):
		self.epics = dict(epic_dict) #initialize dictionary of epics/dupe protected items
		self.others = dict(other_dict) #everything else
		self.unpulled_epics = epic_dict #epics that have not been pulled, that is, all of them at the beginning
		self.guarenteed_crates = [10,30,60] #which crates have guarenteed epics
		self.chance_epic = sum(self.epics.values()) #chance to get an epic, this is constant and gets redistributed to remaining epics, since activision says that if a epic is pulled the chance of the other epics increases
		self.pulls = 0 #pulls done so far

		
	def pull(self,items):
		item_list = items
		rndm = random()*sum(item_list.values()) #random value between 0 and sum of total probability of items
		current = 0 #probability summed so far
		for item in item_list.keys():
			current = current + item_list[item] #take probability of current item, add it to to var current
			if(current >= rndm):   #if the sum of probabilities is smaller or equal to that random number
				return item  #return that item

	def play(self):
		if(random()*100 <= self.chance_epic):  # see if the item to be pulled is an epic or not
			if(len(self.unpulled_epics) == 0): #if so, check if all epics have already been pulled, then activision says that any random epic is pulled
				return self.pull(self.epics)
			else:
				epic_got = self.pull(self.unpulled_epics)  #if there are unpulled epics, pull one from them and remove from unpulled epics list
				self.unpulled_epics.pop(epic_got)
				return epic_got
		else:
			return self.pull(self.others)  #if its not a epic, draw from non-dupe protected items

	def reset_pulls(self):
		self.pulls = 0

	def pull_crate(self):
		self.pulls += 1  # nth pull, starting from 1
		if(self.pulls in self.guarenteed_crates):  #check if guarenteed epic
			if(len(self.unpulled_epics) == 0):
				return self.pull(self.epics)
			else:
				epic_got = self.pull(self.unpulled_epics)    #if so pull an unpulled epic, remove that from the pool
				self.unpulled_epics.pop(epic_got)
				return epic_got
		else:
			return self.play()   #otherwise just pull as usual. end of class.
