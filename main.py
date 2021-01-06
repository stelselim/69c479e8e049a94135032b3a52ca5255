from flask import Flask, request,jsonify
import markdown

app = Flask(__name__)

# An Error Occured
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/',methods=['POST', 'GET'])
def welcomePage():
    if request.method == 'POST':
        return "POSTEd"
    else:
        return "GET"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)