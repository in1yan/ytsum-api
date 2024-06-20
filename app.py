from flask import Flask,request, jsonify
import utils
app = Flask(__name__)

@app.route('/summarize', methods=['GET'])
def summ():
	url = request.args.get('url')
	print(url)
	script = utils.transcript(url)
	summary = utils.summarize(script['transcript'])
	print(script['transcript'])
	print('--------------------------')
	print(summary)
	data = {
	        "url":url,
	        "thumbnail":script['thumbnail'],
	        "title":script['title'],
	        "summary":summary
	        }
	return jsonify(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
