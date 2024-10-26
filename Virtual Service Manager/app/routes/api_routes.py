from flask import Blueprint, request, jsonify
from pymongo.errors import DuplicateKeyError
from app.db.mongo_connection import collection

# Create a Blueprint for API routes
api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/save-api-request', methods=['POST'])
def save_api_request():
    try:
        # Retrieve data from the request body
        data = request.get_json()

        # Extract fields from the request
        url = data.get('url')
        method = data.get('method')
        headers = data.get('headers', {})
        body = data.get('body', {})
        uri_params = data.get('uri_params', {})
        query_params = data.get('query_params', {})

        # Validate required fields
        if not url or not method:
            return jsonify({'error': 'URL and method are required'}), 400

        # Construct document for MongoDB
        api_request = {
            'url': url,
            'method': method,
            'headers': headers,
            'body': body,
            'uri_params': uri_params,
            'query_params': query_params
        }

        # Insert document into MongoDB
        collection.insert_one(api_request)

        return jsonify({'message': 'API request saved successfully'}), 201

    except DuplicateKeyError:
        return jsonify({'error': 'API request with the same URL and method already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/get-api-request', methods=['GET'])
def get_api_request():
    try:
        # Retrieve query parameters
        url = request.args.get('url')
        method = request.args.get('method')

        # Validate required parameters
        if not url or not method:
            return jsonify({'error': 'URL and method are required'}), 400

        # Query MongoDB for the document
        api_request = collection.find_one({'url': url, 'method': method}, {'_id': 0})

        # Check if document exists
        if api_request is None:
            return jsonify({'error': 'API request not found'}), 404

        return jsonify(api_request), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/get-all-api-requests', methods=['GET'])
def get_all_api_requests():
    try:
        # Retrieve all documents in the collection
        all_requests = list(collection.find({}, {'_id': 0}))

        # Check if there are any documents
        if not all_requests:
            return jsonify({'message': 'No API requests found'}), 404

        return jsonify(all_requests), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
