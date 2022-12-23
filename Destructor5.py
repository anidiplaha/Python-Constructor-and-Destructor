class Example():
	def __init__(self, x):
	    # for x = 0, raise exception
		if x == 0:
			raise Exception();
		self.x = x;
		
	def __del__(self):
		print (self.x)

# creating an object
myObj = Example();
# to delete the object explicitly
del myObj