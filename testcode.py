import magic
import types
def perform():
	"""
	Provided a base class of a module, the functions that begin with
	'test' in the classes derived from the base class are invoked. In the code sample 'abc' is the base class.
	"""
	bases,target,allatrs,classes=[],[],[],[]
	atrb=dir(magic)
	for i in atrb:
		if type(getattr(magic,i))==types.ClassType:
			classes.append(i)
	for i in classes:
		bases=getattr(magic,i).__bases__
		if getattr(magic,'abc') in bases:
			target.append(i)
	for i in target:
		allatrs=dir(getattr(magic,i))
		for j in allatrs:
			if type(getattr(getattr(magic,i),j))==types.MethodType:
				if j[:4]=='test':
					instance=getattr(magic,i)()
					getattr(instance,j)()
	  
perform()

