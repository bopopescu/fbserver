from flask import Flask, Response
from flask import request
from OpenSSL import SSL
from investfbfilter import *
from database import *
from data import *
import json
from filtercomputation import *
app = Flask(__name__)

# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('/etc/apache2/ssl4/myserver.key')
# context.use_certificate_file('/etc/apache2/ssl4/fbcredibility_com.crt')

@app.route("/", methods=['POST', 'GET'])
def hello():
	return "Hello"

@app.route('/fbfilterel', methods=['POST', 'GET'])
def fbfilterel():
	return_id = request.args.get('return_id')
	message = request.args.get('message')
	sholdbe = request.args.get('sholdbe')
	user_post = request.args.get('user_post')
	
	data = {}
	data['sholdbe'] = sholdbe
	data['message'] = message
	data['user_post'] = user_post
	db = Database()
	db.insert_filter_el_2(data)
	db.close()
	db.close_connection()
		
	map_result = {}
	map_result['status'] = 0
	map_result['description'] = 'Thanks'
	map_result['return_id'] = return_id
	return Response(json.dumps(map_result),  mimetype='application/json')
	
@app.route('/invfbfilter', methods=['POST', 'GET'])
def invdisplay():
	inv = InvFBFilter()
	q = request.args.get('q','')
	if q != '':
		return inv.getQueryData(q)
	else:
		return inv.getAllMessage()
	
@app.route('/tinvfbfilter')
def tinvdisplay():
	inv = InvFBFilter()
	return inv.getTData()

@app.route('/fbfiltersave')
def fbfiltersave():
	message = request.args.get('message', '')
	return_id = request.args.get('return_id')
	user_post = request.args.get('user_post','')
	agree_value = request.args.get('agree_value','')
	filter_status = request.args.get('filter_status')
	data = {}
	data['message'] = message
	data['user_post'] = user_post
	data['agree_value'] = agree_value
	data['filter_status'] = filter_status
	db = Database()
	db.insert_fb_filter_save(data)
	map_result = {}
	map_result['status'] = 0
	map_result['description'] = 'Thanks'
	map_result['return_id'] = return_id
	return Response(json.dumps(map_result),  mimetype='application/json')

@app.route('/fbfilter', methods=['POST', 'GET'])
def fbfilter():
	print "*************** start"
	message = request.args.get('message', '')
	return_id = request.args.get('return_id')
	map_result = {}
	if message != '':
		filtercomputation = FilterComputation()
		data = filtercomputation.isFilterMessage(message)
		if data == 'yes':
			map_result['status'] = 0
			map_result['description'] = 'Measurement credibility'
		else:
			map_result['status'] = 1
			map_result['description'] = 'Not measurement credibility'					
	else:
		data = 'No message'
		map_result['status'] = 2
		map_result['description'] = 'No message to compare'		
	map_result['return_id'] = return_id
	map_result['measurement'] = data
	return Response(json.dumps(map_result),  mimetype='application/json')

@app.route('/j1fbfilterel', methods=['POST', 'GET'])
def j1fbfilterel():
	return_id = request.args.get('return_id')
	fbPost = FBPost(likes=request.args.get('likes'), 
				shares=request.args.get('shares'),
				comments=request.args.get('comments'),
				url=request.args.get('url'),
				hashtags=request.args.get('hashtags'),
				images=request.args.get('images'),
				vdo=request.args.get('vdo'),
				is_public=request.args.get('is_public'))
	message = request.args.get('message')
	processData = ProcessData(message)
	fbPost.word_count, fbPost.character_length, fbPost.question_mark, fbPost.exclamation_mark = processData.process()
	print fbPost 
# 	db = Database()
# 	db.insert_training_data(fbPost)
	map_result = {}
	map_result['status'] = 0
	map_result['description'] = 'Thanks'
	map_result['return_id'] = return_id
	return Response(json.dumps(map_result),  mimetype='application/json')	
	
if __name__ == "__main__":
# 	app.run(host='0.0.0.0', port=8080, ssl_context=context)
	app.run(host='127.0.0.1', port=9090)