from flask import Flask,request
import utils
app = Flask(__name__)

@app.route('/summarize', methods=['GET'])
def summ():
	url = request.args.get('url')
	print(url)
	transcript = utils.transcript(url)
	summary = utils.summarize(transcript)
	return summary

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)