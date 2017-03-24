
##########################################
# r=map(f,[1,2,3,4,5])
# list(r)
# print r

##########################################
# l=[]
# for i in range(1,10):
# 	l.append(i)
# print l

##########################################
# def normalize(name):
# 	# if name.isupper():
# 	# 	print(name,'is true')
# 	# else:
# 	# 	name.capitalize()
# 	return name.capitalize()
# a=['lise','Waxyoung','liu']
# r=list(map(normalize,a))
# print(r)

##########################################
# def __odd__iter():
# 	n=1
# 	while True:
# 		n=n+2
# 		yield n

# def __not__divisible(n):
# 	return lambda x: x%n > 0

# def prime():

# 	it = __odd__iter()
# 	while True:
# 		n=next(it)
# 		yield n
# 		it = filter(__not__divisible(n),it)

# for n in prime():
# 	if n<1000:
# 		print n
# 	else:
		# break

##########################################
# def is_pailindrom(n):
# 	n=str(n)
# 	return n[::]==n[::-1] and len(n)>1
# output = filter(is_pailindrom,range(1,100))
# print(list(output))

##########################################
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

class Apple(object):

	"""docstring for Apple"""
	# def __init__(self, brand,price):
	# 	super(Apple, self).__init__()
	# 	self.brand = brand
	# 	self.price = price
	# def printapple(self):
	# 	print(self.brand,self.price)
	@property
	def get_price(self):
		return self._price

	@get_price.setter	
	def get_prise(self,value):	
		if not isinstance(value,int):
			raise ValueError('Error_001')
		if value < 0 or value >10000:
			raise ValueError('Error_002')
		self._price=value

# iphone=Apple()
# iphone.get_price(5000)
# print iphone.get_price()

iphone6=Apple()
iphone6.get_prise=123
print iphone6.get_price












