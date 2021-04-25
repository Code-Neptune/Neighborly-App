import azure.functions as func
import pymongo


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://projectmicroservice-cosmodb:fTrUYxcdmbmbqWRWlog9XbI89WT7UTr5eTj9Hu6rsEG8BOHNFS1jQB8Fi8n1O6XHXyhzX6GhrySkTkuPHzMt5A==@projectmicroservice-cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@projectmicroservice-cosmodb@"
            client = pymongo.MongoClient(url)
            database = client['Neighborly']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
