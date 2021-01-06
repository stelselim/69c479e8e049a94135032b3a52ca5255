from flask import Flask, request, jsonify
from src.api import compare, compareWithDate

app = Flask(__name__)

# Page Not Found Handler
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route('/')
def compareRates():
    try:
        return compare()
    except:
        return {"error": "error occured in the service"}


@app.route('/date')
def compareRatesWithDate():
    try:
        year = request.args.get('year')
        month = request.args.get('month')
        day = request.args.get('day')
        return compareWithDate(int(year), int(month), int(day))
    except:
        return {"error": "please check your date"}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
