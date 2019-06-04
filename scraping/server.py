from . import brandname
from flask import Flask, request, jsonify
import json

server = Flask(__name__)
server.config['JSON_AS_ASCII'] = False

@server.route("/brandname", methods=['GET'])
def get_brand_name():
    params = request.args
    response = {}
    result = {}
    bn_list = []
    try:
        bn = brandname.BrandName("folio-sec.com", "https")
        if 'theme' in params:
            bn.set_brand_name("theme/" + params.get('theme'))
            bn_list = bn.get_brand_name()
            if len(bn_list) != 0:
                result["code"] = 1
                result["message"] = "success"
            else:
                raise Exception(params.get('theme') + " doesn't exit.")
        else:
            raise Exception("params is incorrect.")
    except Exception as e:
        result["code"] = 0
        result["message"] = str(e)

    response["result"] = result
    response["brandname"] = bn_list
    return jsonify(response)

def start_server():
    server.run(host="0.0.0.0", port=8000)
