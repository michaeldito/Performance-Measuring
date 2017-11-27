import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='mcdito13', api_key='cMRrKsSawEP7ycufsfpq')

cLevel = ['10','20','50','100','200','500','700','1000','1200','1500','2000','2500','3000']

def readFileIntoArray(A, F):
	for i in F:
		i = i.rstrip('\n')
		A.append(i)

#t98 = open("2-data/2-98.txt", "r")
tMean = open("2-data/2-mean.txt", "r")
#two98 = []
twoMean = []
#readFileIntoArray(two98, t98)
readFileIntoArray(twoMean, tMean)

#th98 = open("3-data/3-98.txt", "r")
thMean = open("3-data/3-mean.txt", "r")
#three98 = []
threeMean = []
#readFileIntoArray(three98, th98)
readFileIntoArray(threeMean, thMean)

#f98 = open("4-data/4-98.txt", "r")
fMean = open("4-data/4-mean.txt", "r")
#four98 = []
fourMean = []
#readFileIntoArray(four98, f98)
readFileIntoArray(fourMean, fMean)

#fv98 = open("5-data/5-98.txt", "r")
fvMean = open("5-data/5-mean.txt", "r")
#five98 = []
fiveMean = []
#readFileIntoArray(five98, fv98)
readFileIntoArray(fiveMean, fvMean)

# Create and style traces
'''
traceTwo98 = go.Scatter(
	x = cLevel,
    	y = two98,
   	name = '2-node 98%',
    	line = dict(
        	color = ('rgb(205, 12, 24)'),
        	width = 4)
)
'''
traceTwoMean = go.Scatter(
	x = cLevel,
	y = twoMean,
	name = '2-node Mean Response Time',
	line = dict(
		color = ('rgb(205, 12, 24)'),
		width = 4,
	)
)
'''
traceThree98 = go.Scatter(
    	x = cLevel,
   	y = three98,
    	name = '3-node 98%',
    	line = dict(
        	color = ('rgb(34, 139, 34)'),
        	width = 4)
)
'''
traceThreeMean = go.Scatter(
	x = cLevel,
	y = threeMean,
	name = '3-node Mean Response Time',
	line = dict(
		color = ('rgb(34, 139, 34)'),
		width = 4,
	)
)
'''
traceFour98 = go.Scatter(
    	x = cLevel,
   	y = four98,
    	name = '4-node 98%',
    	line = dict(
        	color = ('rgb(127, 0, 255)'),
       		width = 4)
)
'''
traceFourMean = go.Scatter(
	x = cLevel,
	y = fourMean,
	name = '4-node Mean Response Time',
	line = dict(
		color = ('rgb(127, 0, 255)'),
		width = 4,
	)
)
'''
traceFive98 = go.Scatter(
    	x = cLevel,
   	y = five98,
    	name = '5-node 98%',
    	line = dict(
        	color = ('rgb(255, 128, 0)'),
       		width = 4)
)
'''
traceFiveMean = go.Scatter(
	x = cLevel,
	y = fiveMean,
	name = '5-node Mean Response Time',
	line = dict(
		color = ('rgb(255, 128, 0)'),
		width = 4,
	)
)

#data = [traceTwo98, traceTwoMean, traceThree98, traceThreeMean, traceFour98, traceFourMean, traceFive98, traceFiveMean]
data = [traceTwoMean, traceThreeMean, traceFourMean, traceFiveMean]

# Edit the layout
layout = dict(title = 'Comparison of Performance for 2, 3, 4, and 5 REST Servers',
              xaxis = dict(title = 'Concurency Level'),
              yaxis = dict(title = 'Time (ms)', range=[0,1100]),
              )

fig = dict(data=data, layout=layout)

py.plot(fig, filename='CS385-L02-Comparison-Data')
