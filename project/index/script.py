from gevent import monkey
from gevent.pywsgi import WSGIServer
import gevent

@app.route('/', methods=['POST', 'GET'])
def output():
	#scheduling = ['fcfs', 'rr', 'sjf', 'non_preemptive', 'srtf', 'preemptive', 'multilevel_queue']
	inp = request.system.args['input']
	out = ""
	#for algo in scheduling:
		out += executer.execute('main', inp)
	return out

@app.route('/')
def produce_output():
	return app.send_static_file('index.html')