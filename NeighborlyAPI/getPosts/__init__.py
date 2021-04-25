import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://projectmicroservice-cosmodb:fTrUYxcdmbmbqWRWlog9XbI89WT7UTr5eTj9Hu6rsEG8BOHNFS1jQB8Fi8n1O6XHXyhzX6GhrySkTkuPHzMt5A==@projectmicroservice-cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@projectmicroservice-cosmodb@"
        client = pymongo.MongoClient(url)
        database = client['Neighborly']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
