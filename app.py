from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/analyze', methods =['GET'])

def analyze():
	with open('logfile.txt', a) as fp_log:
		fp_log.write('endpoint hit %s \n' % datetime.datetime.now().strfttime('%Y-%m-%d %H:%M:%S'))
	return 'Got it'

app.run(host='0.0.0.0')
