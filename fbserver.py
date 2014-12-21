from flask import Flask, Response
from flask import request
from data import *
import json

app = Flask(__name__)

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
                share_public=request.args.get('is_public'))
    fbPost.share_only_friend = request.args.get('share_only_friend')
    fbPost.app_sender = request.args.get('app_sender')
    fbPost.feeling_status = request.args.get('feeling_status')
    message = request.args.get('message','')
    processData = ProcessData(message)
    fbPost.word_count, fbPost.character_length, fbPost.question_mark, fbPost.exclamation_mark = processData.process()
    print fbPost
#     db = Database()
#     db.insert_training_data(fbPost)
    map_result = {}
    map_result['status'] = 0
    map_result['description'] = 'Thanks'
    map_result['return_id'] = return_id
    return Response(json.dumps(map_result),  mimetype='application/json')    
    
if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, ssl_context=context)
    app.run(host='127.0.0.1', port=9090)