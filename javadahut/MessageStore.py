      #constructor
class Animal(object):

	def __init__(self, weight, age, name):
		self.weight = weight
		self.age = age
		self.name = name
		self.children = {}

	def addChild(self, child):
		self.children[child.name] = child

	def addChildren(self, children):
		for child in children:
			self.addChild(child)

	def hasChild(self, name):
		return name in self.children

	def feedChildren(self, isFriedCheese=False):
		for child in self.children.values():
			if isFriedCheese:
				child.weight = child.weight + 1
			else:
				child.weight = child.weight + .5

	def numDescendents(self):
		descendents = len(self.children)
		for child in self.children.values():
			descendents = descendents + child.numDescendents()
		return descendents




class AquaticAnimal(Animal):

	def __init__(self, weight, age, name, floatiness):
		#The constructor of the AquaticAnimal
		super(AquaticAnimal, self).__init__(weight, age, name)
		self.floatiness = floatiness

	def speed(self):
		speed = 100
		return speed -self.age - (self.weight/10)


class LandAnimal(Animal):
	def __init__(self, weight, age, name):
		#the constructor of the LandAnimal
		super(LandAnimal, self).__init__(weight, age, name)

	def speed(self):
		speed = 100
		return speed * 2 - self.age



dolphin1 = AquaticAnimal(100, 20, 'bob the dolphin', 0.4)
dolphin2 = AquaticAnimal(120, 40, 'susy the dolphin', 0.45)
shark = AquaticAnimal(200, 10, 'frank the shark', 0.5)
zebra = LandAnimal(150, 5, 'zack the zebra')
cheetah = LandAnimal(80, 4, 'charlie the cheetah')
cheetah2 = LandAnimal(40, 1, 'chase the baby cheetah')
gpanda = LandAnimal(130, 10, 'patty the panda')

zoo = [dolphin1, dolphin2, shark, zebra, cheetah, gpanda]

pandak1 = LandAnimal(120, 6, 'peter the panda')
pandak2 = LandAnimal(140, 5, 'piper the panda')
pandab1 = LandAnimal(80, 2, 'percy the panda')
pandab2 = LandAnimal(60, 1, 'penny the panda')
pandab3 = LandAnimal(60, 2, 'perry the panda')
pandab4 = LandAnimal(50, 1, 'pancho the panda')

dolphin1.addChild(AquaticAnimal(50, 1, 'bobby the child of bob', 0.45))
dolphin1.children['bobby the child of bob'].name

cheetah.addChild(cheetah2)

gpanda.addChildren([pandak1, pandak2])
pandak1.addChildren([pandab1, pandab2])
pandak2.addChildren([pandab3, pandab4])

for child in gpanda.children.values():
	print(child.name, child.age, child.weight)

# these are all the same
gpanda.feedChildren()
gpanda.feedChildren(False)
gpanda.feedChildren(isFriedCheese=False)

# these are all the same
gpanda.feedChildren(True)
gpanda.feedChildren(isFriedCheese=True)

for child in gpanda.children.values():
	print(child.name, child.age, child.weight)


print(gpanda.numDescendents())
pandab4.addChild(LandAnimal(10, .5, 'poseidon the panda'))
print(gpanda.numDescendents())

animals = 0
for animal in zoo:
	animals = animals + 1 + animal.numDescendents()
print(animals)

