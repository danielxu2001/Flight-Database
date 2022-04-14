from sys import displayhook
from flask import render_template, request, jsonify, redirect
from app import app
from app import database as db_helper
from app import __init__
@app.route("/delete/<string:FlightNumber>", methods=['POST'])
def delete(FlightNumber):
    """ recieved post requests for entry delete """
    
    try:
        db_helper.delete_flight(FlightNumber)
        result = {'success': True, 'response': 'Removed Flight'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    inserts = db_helper.get_insert_flight()
    return render_template("cart.html", inserts = inserts)
    


@app.route("/update", methods=['POST'])
def update():
    """ recieved post requests for entry updates """
    data = request.get_json()
    try:
        if "Description" in data:
            db_helper.update_flight_status(data["FlightNumber"], data["Description"])
            result = {'success': True, 'response': 'Description Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    inserts = db_helper.get_insert_flight()
    return render_template("cart.html", inserts = inserts)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    
    data = request.json
    db_helper.insert_new_flight(data["FlightNumber"])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/search", methods = ['GET'])
def search():
    DepCode = request.args.get("leavingFrom")
    AriCode = request.args.get("goingTo")
    DepDate = request.args.get("departureDate")
    AriDate = request.args.get("arrivalDate")
    if (len(DepCode) == 3 and len(AriCode) == 3):
        newDepCode = DepCode.upper()
        newAirCode = AriCode.upper()
    else:
        newDepCode = DepCode.lower()
        newDepCode = newDepCode.title()
        newAirCode = AriCode.lower()
        newAirCode = newAirCode.title()

    year = DepDate[:4]
    month = DepDate[5:7]
    day = DepDate[8:]
    newDepDate = year + "/" + month + "/" + day
    year2 = AriDate[:4]
    month2 = AriDate[5:7]
    day2 = AriDate[8:]
    newAriDate = year2 + "/" + month2 + "/" + day2
    results = db_helper.searchFlight(DepCode, AriCode, newDepDate, newAriDate)
    return render_template("index.html", results = results)

@app.route("/")
def homepage():
    results = []
    return render_template("index.html", results = results)
    
@app.route("/cart")
def cart():
    inserts = db_helper.get_insert_flight()
    return render_template("cart.html", inserts = inserts)
@app.route("/max-seats")
def maxseats():
    seats = db_helper.maxSeat()    
    return render_template("max-seats.html", seats = seats)
    
@app.route("/status")
def status():
    statuses = db_helper.get_flight_status()
    return render_template("status.html", statuses = statuses)

@app.route("/avg-price")
def avgPrice():
    results = []
    return render_template("average-price.html", results = results)

@app.route("/search-avg-price", methods = ['GET'])
def searchAvgPrice():
    # avgPrice = db_helper.avgPrice(300, 1000, "San Francisco", 100)
    # print(avgPrice)
    # return avgPrice[0]

    DepCode = request.args.get("leavingFrom")
    MinPrice = request.args.get("minPrice")
    MaxPrice = request.args.get("maxPrice")
    MaxSeat = request.args.get("maxSeat")
    if (len(DepCode) == 3):
        newDepCode = DepCode.upper()
    else:
        newDepCode = DepCode.lower()
        newDepCode = newDepCode.title()

    results = db_helper.avgPrice(MinPrice, MaxPrice, DepCode, MaxSeat)
    return render_template("average-price.html", results = results)