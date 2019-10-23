''' controller and routes for users '''
import os
from flask import request, jsonify
from app import app, db
from app.schemas import validate_release
from bson.json_util import dumps
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/release/id', methods=['GET'])
def singlerelease():
    ''' get a single release'''
    if request.method == 'GET':
        query = request.args
        data = db.releases.find_one(query)
        return jsonify({'ok': True, 'data': data}), 200

@app.route('/release', methods=['GET', 'POST','DELETE', 'PATCH'])
def release():
    ''' get all single release'''
    if request.method == 'GET':
        data = []
        for d in db.releases.find():
            data.append(d)
        return jsonify({'ok': True, 'data': data}), 200

    if request.method == 'POST':
        ''' Create a new release'''
        data = validate_release(request.get_json())
        if data['ok']:
            data = data['data']
            db.releases.insert_one(data)
            return jsonify({'ok': True, 'message': 'Release created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400

    data = request.get_json()
    if request.method == 'DELETE':
        if data.get('release_id', None) is not None:
            db_response = db.releases.delete_one({'release_id': data['release_id']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH': 
        if data.get('release_id', None) is not None:
            data = validate_release(request.get_json())
            if data['ok']:
                query = request.args
                db.releases.update_one(query, {'$set': data.get('payload', {})})
                return jsonify({'ok': True, 'message': 'Release updated successfully!'}), 200
            else:
                return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400