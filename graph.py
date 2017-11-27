import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='mcdito13', api_key='cMRrKsSawEP7ycufsfpq')

cLevel = ['10','20','50','100','200','500','700','1000','1200','1500','2000','2500','3000']

def readFileIntoArray(A, F):
	for i in F:
		i = i.rstrip('\n')
		A.append(i)

tMean = open("2-data/2-mean.txt", "r")
twoMean = []
readFileIntoArray(twoMean, tMean)

thMean = open("3-data/3-mean.txt", "r")
threeMean = []
readFileIntoArray(threeMean, thMean)

fMean = open("4-data/4-mean.txt", "r")
fourMean = []
readFileIntoArray(fourMean, fMean)

fvMean = open("5-data/5-mean.txt", "r")
fiveMean = []
readFileIntoArray(fiveMean, fvMean)

traceTwoMean = go.Scatter(
	x = cLevel,
	y = twoMean,
	name = '2-node Mean Response Time',
	line = dict(
		color = ('rgb(205, 12, 24)'),
		width = 4,
	)
)

traceThreeMean = go.Scatter(
	x = cLevel,
	y = threeMean,
	name = '3-node Mean Response Time',
	line = dict(
		color = ('rgb(34, 139, 34)'),
		width = 4,
	)
)

traceFourMean = go.Scatter(
	x = cLevel,
	y = fourMean,
	name = '4-node Mean Response Time',
	line = dict(
		color = ('rgb(127, 0, 255)'),
		width = 4,
	)
)

traceFiveMean = go.Scatter(
	x = cLevel,
	y = fiveMean,
	name = '5-node Mean Response Time',
	line = dict(
		color = ('rgb(255, 128, 0)'),
		width = 4,
	)
)

data = [traceTwoMean, traceThreeMean, traceFourMean, traceFiveMean]

# Edit the layout
layout = dict(title = 'Comparison of Performance for 2, 3, 4, and 5 REST Servers',
              xaxis = dict(title = 'Concurency Level'),
              yaxis = dict(title = 'Time (ms)', range=[0,1100]),
              )

fig = dict(data=data, layout=layout)

py.plot(fig, filename='CS385-L02-Comparison-Data')
