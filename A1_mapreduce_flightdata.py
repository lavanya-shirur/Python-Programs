#!/usr/bin/env python
import pydoop.mapreduce.api as api
import pydoop.mapreduce.pipes as pp
class Mapper(api.Mapper):
	def map(self, context):	
		delay=context.value.split(',')
		if delay[15]== "NA"  or delay[15] <= '0':
			newvar="10"
			context.emit(delay[16],newvar)
	
		else :
			newvar="11"
			context.emit(delay[16],newvar)
			
class Reducer(api.Reducer):
	def reduce(self, context):
        	array1=0
		array2=0
	        for num in map(str,context.values):
	                array1+= int(num[0])
        	        array2+= int(num[1])

	                percent= (float(array2)/array1)*100
        	context.emit(context.key,percent)

def __main__():
    pp.run_task(pp.Factory(Mapper, Reducer))
   
