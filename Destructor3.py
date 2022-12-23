class Example:
	def __init__(self):
		print ("Object created");
	
	# destructor
	def __del__(self):
	    print ("Object destroyed");

# creating an object
myObj = Example();
# to delete the object explicitly
del myObj;