from flask import Flask, request
from tracker import Tracker
import json

app = Flask(__name__)


@app.route('/<state>/produtos/<string:productname>/<int:pages>', methods = ["GET", "POST"])
def show_product_list(productname, state, pages = 1):
    tracker = Tracker(state)
    productsJson = tracker.GetProducts(productname, pages)
    if  request.method == 'GET':
        """[summary]
        """
        resultJson = {
            'data' : productsJson,
            'search' : productname,
            'state' : state,
            'pageCount' :  pages

        }
        outputJson = json.dumps(resultJson)
        return outputJson
    
    elif request.method == 'POST':
        request.get_data()

        body = request.data
        
        return body




app.run()