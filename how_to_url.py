# from pywikihow import HowTo
# from flask import Flask, request
# import json 
# import sys

# # Setup flask server
# app = Flask(__name__) 


# @app.route('/test', methods = ['GET']) 
# def getdata():

# 	data1 = request.get_json() 
# 	sea = data1['search']
# 	search=str(sea)
# 	print(search)
# 	how_to = HowTo("https://www.wikihow.com/"+search)

# 	data = how_to.as_dict()

# 	# print("# URL")
# 	# print(how_to.url)
# 	# print("\n# TITLE")
# 	# print(how_to.title)
# 	# print("\n# INTRO")
# 	# print(how_to.intro)
# 	# print("\n# NUMBER OF STEPS")
# 	# print(how_to.n_steps)
# 	# print("\n# SUMMARY")
# 	# print(how_to.summary)


# 	print("\n\n# FIRST STEP")
# 	first_step = how_to.steps[0]
# 	#first_step.print()
# 	dataset=[]
# 	dictt={"title":str(how_to.title),"intro":str(how_to.intro)}
# 	dataset.append(dictt)
# 	list = how_to.steps
# 	i=0
# 	for f in list:
# 		st = how_to.steps[i]
# 		d=st.as_dict()
# 		dataset.append(d)
# 		# print(d)
# 		i=i+1
# 	# a dict, useful for saving/sending
# 	data = first_step.as_dict()
# 	# print(dataset)
# 	return json.dumps({"result":dataset})
# 	json_object = json.dumps(dataset, indent = 4) 
# 	return json_object
# 	# print(json_object)
# 	# # print(data)
# 	# sys.stdout.flush()
# 	# print("\n\n# FULL HOW TO")
# 	# how_to.print(extended=True)
# if __name__ == "__main__": 
#     app.run(port=6000)



# # 
##function

from pywikihow import HowTo,WikiHow
from flask import Flask, request
import json 
import sys

# Setup flask server
app = Flask(__name__) 


# @app.route('/test', methods = ['GET']) 
# def getdata():

# 	data1 = request.get_json() 
# 	sea = data1['search']
# 	search=str(sea)
# 	print(search)
# 	datatitle=[]
# 	dataset=[]
# 	for how_tos in WikiHow.search(search):
# 		print(how_tos.title)
# 		how_to = HowTo("https://www.wikihow.com/"+how_tos.title)
# 		dictt={"title":str(how_to.title),"intro":str(how_to.intro)}
# 		datatitle.append(dictt)
# 		list = how_to.steps
# 		i=0
# 		for f in list:
# 			st = how_to.steps[i]
# 			d=st.as_dict()
# 			dataset.append(d)
			
# 			i=i+1

# 	return json.dumps({"title":datatitle,"data":dataset})	


# @app.route('/test1', methods = ['GET']) 
# def getdata2():

# 	data1 = request.get_json() 
# 	sea = data1['search']
# 	search=str(sea)
# 	print(search)
# 	datatitle=[]
# 	dataset=[]
# 	for how_tos in WikiHow.search(search):
# 		print(how_tos.title)
# 		how_to = HowTo("https://www.wikihow.com/"+how_tos.title)

# 		dictt={"title":str(how_to.title),"intro":str(how_to.intro)}
# 		datatitle.append(dictt)
# 		list = how_to.steps
# 		i=0
# 		for f in list:
# 			st = how_to.steps[i]
# 			d=st.as_dict()
# 			dataset.append(d)
			
# 			i=i+1

# 	return json.dumps({"title":datatitle,"data":dataset})	

@app.route('/search', methods = ['GET']) 
def getarticles():
	data1 = request.get_json() 
	sea = data1['search']
	search=str(sea)
	print(search)
	dataset=[]
	for how_tos in WikiHow.search(search):
		print(how_tos.title)
		how_to = HowTo("https://www.wikihow.com/"+how_tos.title)
		first_step = how_to.summary
		
		dictt={"title":str(how_to.title),"intro":str(how_to.intro)
		# ,"steps":first_step
		}
		dataset.append(dictt)
	
	return json.dumps({"result":dataset})	



@app.route('/getArticle', methods = ['GET']) 
def getartcileData():
	data1 = request.get_json() 
	sea = data1['search']
	search=str(sea)
	print(search)
	dataset=[]
	how_to = HowTo("https://www.wikihow.com/"+search)	
	# first_step = how_to.steps[0]
	#first_step.print()
	dataset=[]
	datatitle=[]
	dictt={"title":str(how_to.title),"intro":str(how_to.intro)}
	datatitle.append(dictt)
	list = how_to.steps
	i=0
	for f in list:
		st = how_to.steps[i]
		d=st.as_dict()
		dataset.append(d)
		# print(d)  
		i=i+1

	# data = first_step.as_dict()
	return json.dumps({"title":datatitle,"result":dataset})			

if __name__ == "__main__": 
    app.run(port=6000)