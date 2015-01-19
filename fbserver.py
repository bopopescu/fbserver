from flask import Flask, Response, jsonify, request
from data import *
from initial import FBInit
from database import *
import json
from flask.templating import render_template

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def landingpage():
    return render_template('index.html')

@app.route('/PyAI', methods=['POST','GET'])
def pyAI():
    return render_template('pyai.html')


@app.route('/fbcred', methods=['POST','GET'])
def fbcredibility():
    print 'start fb cred'
    from fbcredibility import FBCredibility
    try:
        fbCredibility = FBCredibility(request)
        map_result = fbCredibility.get_credibility()
        print 'map result ', map_result
        return Response(json.dumps(map_result),  mimetype='application/json')
    except Exception as e:
        print e

@app.route('/fbcredfeedback', methods=['POST','GET'])
def fbcred_feedback():
    print 'start fb feed back'
    from fbcredibility import FBCredibility
    fbCred = FBCredibility(request)
    map_result = fbCred.get_feedback()
    return Response(json.dumps(map_result),  mimetype='application/json')

@app.route('/fbcredel', methods=['POST','GET'])
def fbcred_el():
    print 'start fb cred el'
    from fbcredibility import FBCredibilityEL
    fbCred = FBCredibilityEL(request)
    map_result = fbCred.evaluator_credibility()
    return Response(json.dumps(map_result),  mimetype='application/json')

@app.route('/j1fbfilterel', methods=['POST', 'GET'])
def j1fbfilterel():
    return_id = request.args.get('return_id')
    map_result = {}
    try:
        fbPost = FBPost(likes=request.args.get('likes'), 
                    shares=request.args.get('shares'),
                    comments=request.args.get('comments'),
                    url=request.args.get('url'),
                    hashtags=request.args.get('hashtag'),
                    images=request.args.get('images'),
                    vdo=request.args.get('vdo'),
                    share_public=request.args.get('is_public'))
        fbPost.cred_value = request.args.get('cred_value')
        fbPost.share_with_location = request.args.get('location')
        fbPost.share_with_non_location = request.args.get('non_location')
        fbPost.share_only_friend = request.args.get('share_only_friend')
        fbPost.tag_with = request.args.get('tag_with')
        fbPost.app_sender = request.args.get('app_sender')
        fbPost.feeling_status = request.args.get('feeling_status')
        fbPost.user_evaluator = request.args.get('user_evaluator')
        message = request.args.get('message','')
        fbPost.message = message
        processData = ProcessData(message)
        processData.process(fbPost)
        print fbPost
        db = Database()
        db.insert_training_data(fbPost.to_dict())        
    except Exception as e:
        print e
    map_result['status'] = 0
    map_result['description'] = 'Thanks'        
    map_result['return_id'] = return_id
    return Response(json.dumps(map_result),  mimetype='application/json')    

def server_init():
    print 'fb server init'
    FBInit()
    
if __name__ == "__main__":
    # server_init()
#    app.run(host='0.0.0.0', port=80)
    app.run(host='127.0.0.1', port=9090)
