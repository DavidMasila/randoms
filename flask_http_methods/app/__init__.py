from flask import Flask, make_response, jsonify, request, render_template

app = Flask(__name__)

stock = {
    "fruit":{
        "Apple":30,
        "Banana":45,
        "cherry":1000
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-text")
def get_text():
    return "Some text"

@app.route("/stock")
def stocks():
    res = make_response(jsonify(stock), 200)
    return res

@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res
    
    res = make_response(jsonify({"error":"Item not found"}), 400)

    return res

@app.route("/stock/<collection>", methods = ["PUT"])
def put_collection(collection):
    req = request.get_json()
    stock[collection] = req
    res = make_response(jsonify({"message":"Collection replaced"}), 200)
    return res


@app.route("/stock/<collection>", methods = ["PATCH"])
def patch_collection(collection):
    "checks is the items are in stock first if not create"
    req = request.get_json()
    if collection in stock:
        for k,v in req.items():
            stock[collection][k] = v

        res  = make_response(jsonify({"message":"collection updated"}), 200)
        return res

    stock[collection] = req
    res = make_response(jsonify({"message":"Collection created Successfully"}), 200)
    return res


@app.route("/stock/<collection>/<member>", methods = ["PATCH"])
def patch_member(collection, member):
    "checks is the items are in stock first if not create"
    req = request.get_json()
    if collection in stock:
        for k,v in req.items():
            if member in stock[collection]:
                stock[collection][member] = v

                res  = make_response(jsonify({"message":"collection member updated"}), 200)
                return res
            
            stock[collection][member] = v
            res = make_response(jsonify({"message":"Collection member Successfully created"}), 200)
            return res
    
    res = make_response(jsonify({"error":"collection not found"}))
    return res

#delete
@app.route("/stock/<collection>", methods = ["DELETE"])
def delete_collection(collection):
    "checks is the items are in stock first if not create"
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({}), 204)
        return res

    res = make_response(jsonify({"error":"collection not found"}), 400)
    return res

@app.route("/stock/<collection>/<member>", methods = ["DELETE"])
def delete_member(collection, member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({}), 204)
            return res 
        
        res = make_response(jsonify({"Error":"member not found"}), 400)
        return res
    
    res = make_response(jsonify({"error":"collection not found in stock"}), 400)
    return res