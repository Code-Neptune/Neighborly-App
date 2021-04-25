import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://projectmicroservice-cosmodb:fTrUYxcdmbmbqWRWlog9XbI89WT7UTr5eTj9Hu6rsEG8BOHNFS1jQB8Fi8n1O6XHXyhzX6GhrySkTkuPHzMt5A==@projectmicroservice-cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@projectmicroservice-cosmodb@"
            client = pymongo.MongoClient(url)
            database = client['Neighborly']
            collection = database['advertisements']

            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
