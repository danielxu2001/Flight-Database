"""Defines all the functions related to the database"""
from app import db

def searchFlight(depAirport, arvAirport, depDate, ArvDate) -> dict:
    """Reads all tasks listed in the todo table
    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    # depAirport = "%" + depAirport + "%"
    # arvAirport = "%" + arvAirport + "%"
    # print(arvAirport)
    if (ArvDate == "//" and depDate == "//"):
        query = '''SELECT * FROM Flight where (DepAirCode LIKE '{}' or DepartureCity LIKE '{}') and (ArivAirCode LIKE '{}' or ArrivalCity 
        LIKE '{}')'''.format(depAirport, depAirport, arvAirport, arvAirport)
    
    elif (ArvDate == "//"):
        query = '''SELECT * FROM Flight where (DepAirCode LIKE '{}' or DepartureCity LIKE '{}') and (ArivAirCode LIKE '{}' or ArrivalCity LIKE '{}') and DepartureDate = '{}'
        '''.format(depAirport, depAirport, arvAirport,arvAirport, depDate)
    elif (depDate == "//"):
        query = '''SELECT * FROM Flight where (DepAirCode LIKE '{}' or DepartureCity LIKE '{}') and (ArivAirCode LIKE '{}' or ArrivalCity LIKE '{}') and ArrivalDate = '{}'
        '''.format(depAirport, depAirport, arvAirport, arvAirport, ArvDate)
    else:
        query = '''SELECT * FROM Flight where (DepAirCode LIKE '{}' or DepartureCity LIKE '{}') and (ArivAirCode LIKE '{}' or ArrivalCity LIKE '{}')
        and DepartureDate = '{}' and ArrivalDate = '{}' '''.format(depAirport, depAirport, arvAirport, arvAirport, depDate, ArvDate)
    # if (ArvDate == "//" and depDate == "//"):
    #     query = "SELECT * FROM Flight where (DepAirCode = '{}' or DepartureCity = '{}') and (ArivAirCode = '{}' or ArrivalCity = '{}')".format(depAirport, depAirport, arvAirport, arvAirport)
    # elif (ArvDate == "//"):
    #     query = "SELECT * FROM Flight where (DepAirCode = '{}' or DepartureCity = '{}') and (ArivAirCode = '{}' or ArrivalCity = '{}') and DepartureDate = '{}'".format(depAirport, arvAirport, depDate)
    # elif (depDate == "//"):
    #     query = "SELECT * FROM Flight where (DepAirCode = '{}' or DepartureCity = '{}') and (ArivAirCode = '{}' or ArrivalCity = '{}') and ArrivalDate = '{}'".format(depAirport, arvAirport, ArvDate)
    # else:
    #     query = "SELECT * FROM Flight where (DepAirCode = '{}' or DepartureCity = '{}') and (ArivAirCode = '{}' or ArrivalCity = '{}') and DepartureDate = '{}' and ArrivalDate = '{}'".format(depAirport, depAirport, arvAirport, arvAirport, depDate, ArvDate)
    
    query_results = conn.execute(query).fetchall()
    conn.close()
    flight_info= []
    for result in query_results:
        item = {
            "FlightNumber": result[0],
            "Price": result[1],
            "Class": result[2],
            "ArrivalCity": result[3],
            "DepartureCity": result[4],
            "DepartureDate": result[5],
            "ArrivalDate": result[6],
            "DepAirCode": result[7],
            "ArivAirCode": result[8],
            "AirlineName": result[9]
        }
        flight_info.append(item)

    return flight_info

def insert_new_flight(FlightNumber):
    """Insert new task to todo table.
    Args:
        text (str): Task description
    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query = "INSERT INTO Users(FlightNumber, Price, Class, ArrivalCity, DepartureCity, DepartureDate, ArrivalDate, DepAirCode, ArivAirCode, AirlineName) SELECT * FROM Flight WHERE FlightNumber = '{}'".format(FlightNumber)
    conn.execute(query)

def get_insert_flight()->dict:
    conn = db.connect()
    query_results = conn.execute("Select * FROM Users").fetchall()
    conn.close()
    flight_info= []
    for result in query_results:
        item = {
            "FlightNumber": result[0],
            "Price": result[1],
            "Class": result[2],
            "ArrivalCity": result[3],
            "DepartureCity": result[4],
            "DepartureDate": result[5],
            "ArrivalDate": result[6],
            "DepAirCode": result[7],
            "ArivAirCode": result[8],
            "AirlineName": result[9],
            "Description": result[10]
        }
        flight_info.append(item)
    return flight_info


def update_flight_status(FlightNumber: str, Description: str) -> dict:
    conn = db.connect()
    query = "UPDATE Users SET Description = '{}' WHERE FlightNumber = '{}'".format(Description, FlightNumber)
    conn.execute(query)
    query_results = conn.execute("Select * FROM Users WHERE FlightNumber = '{}'".format(FlightNumber)).fetchall()
    conn.close()
    user_info= []
    for result in query_results:
        item = {
            "FlightNumber": result[0],
            "Price": result[1],
            "Class": result[2],
            "ArrivalCity": result[3],
            "DepartureCity": result[4],
            "DepartureDate": result[5],
            "ArrivalDate": result[6],
            "DepAirCode": result[7],
            "ArivAirCode": result[8],
            "AirlineName": result[9],
            "Description": result[10]
        }
        user_info.append(item)
    return user_info

def delete_flight(FlightNumber: str):
    conn = db.connect()
    query = "DELETE FROM Users WHERE FlightNumber = '{}'".format(FlightNumber)
    conn.execute(query)
    conn.close()
#advanced query 1
def get_flight_status() -> dict:
    conn = db.connect()
    query = '''SELECT COUNT(f.FlightNumber), f.DepAirCode, s.CurrentStatus FROM Flight f NATURAL JOIN FlightStatus s
    WHERE s.CurrentStatus = 'Delayed' GROUP BY f.DepAirCode ORDER BY f.DepAirCode, COUNT(f.FlightNumber)'''
    queryResult = conn.execute(query).fetchall()
    flightStatus = []
    for result in queryResult:
        item = {
            "CurrentStatus": result[2],
            "Count": result[0],
            "Airport": result[1]
        }
        flightStatus.append(item)
    return flightStatus
#advance query 2
def maxSeat()-> dict:
    conn = db.connect()
    query = 'SELECT COUNT(MaxSeats), AirportName, AirplaneType FROM Airport LEFT JOIN Airplanes USING (AirportCode) WHERE MaxSeats > 0 GROUP BY AirplaneType, AirportName ORDER BY COUNT(MaxSeats)'
    queryResult = conn.execute(query).fetchall()
    seats = []
    for result in queryResult:
        item = {
            "Seats": result[0],
            "AirportName": result[1],
            "AirplaneType": result[2]
        }
        seats.append(item)
    return seats
# store procedure
def avgPrice(minPrice, maxPrice, departure_city, maxseats)->dict:
    conn = db.connect()
    query = "call myProcedure({}, {}, '{}',{})".format(minPrice,maxPrice, departure_city, maxseats)
#     query = ''' PROCEDURE myProcedure()
# BEGIN
#     DECLARE fn VARCHAR(20);
#     DECLARE p double;
#     DECLARE cap double;
#     DECLARE com double;
#     DECLARE c VARCHAR(255);
#     DECLARE ac VARCHAR(255);
#     DECLARE dc VARCHAR(255);
#     DECLARE dd VARCHAR(255);
#     DECLARE ad VARCHAR(255);
#     DECLARE dac VARCHAR(10);
#     DECLARE aac VARCHAR(10);
#     DECLARE an VARCHAR(20);
    
#     DECLARE cur CURSOR FOR
#     (SELECT distinct FlightNumber, Price, ClassAvgPrice, Class, ArrivalCity, DepartureCity, DepartureDate, 
#     ArrivalDate, DepAirCode, ArivAirCode, AirlineName
#     FROM Flight NATURAL JOIN FlightStatus NATURAL JOIN (SELECT class, ROUND(avg(price)) as ClassAvgPrice
#               FROM Flight f NATURAL JOIN Airplanes a
#               WHERE f.DepartureCity = '{}' AND (f.price >= {} AND f.price <= {}) AND a.MaxSeats > {}
#               GROUP BY f.Class) AS t1
#     WHERE DepartureCity = '{}' AND (price >= {} AND price <= {}));
#     DROP TABLE IF EXISTS FinalTable;
    
#     CREATE TABLE FinalTable(
#     FlightNumber VARCHAR(20) PRIMARY KEY,
#     Price float,
#     ClassAvgPrice float,
#     Comments float,
#     Class VARCHAR(255),
#     ArrivalCity VARCHAR(255),
#     DepartureCity VARCHAR(255),
#     DepartureDate VARCHAR(255),
#     ArrivalDate VARCHAR(255),
#     DepAirCode VARCHAR(10),
#     ArivAirCode VARCHAR(10),
#     AirlineName VARCHAR(20)
#     );

#     OPEN cur;
#     BEGIN 
#     DECLARE exit_flag BOOLEAN DEFAULT FALSE;
#         DECLARE CONTINUE HANDLER FOR NOT FOUND SET exit_flag = TRUE;
#         cloop: LOOP
#     FETCH cur INTO fn, p, cap, c, ac, dc, dd, ad, dac, aac, an;
#             IF fn is NULL THEN
#     LEAVE cloop;
#             ELSEIF exit_flag THEN
#                 LEAVE cloop; 
#     END IF;
#             IF (p != cap) THEN
#     SET com =  (p-cap)/cap * 100 ;
#     END IF;
#             INSERT INTO FinalTable VALUES (fn, p, cap, com, c, ac, dc, dd, ad, dac, aac, an);
#         END LOOP cloop;
#     END;
#     CLOSE cur;
#     SELECT ft.FlightNumber, ft.Price, ft.ClassAvgPrice, ft.Comments, ft.Class, ft.ArrivalCity, ft.DepartureCity, 
#     ft.DepartureDate, 
#     ft.ArrivalDate, ft.DepAirCode, ft.ArivAirCode, ft.AirlineName
#     FROM FinalTable ft
#     ORDER BY Class, AirlineName;
# END'''.format(departure_city, minPrice, maxPrice, maxseats,departure_city,minPrice,maxPrice)
    queryResult = conn.execute(query).fetchall()
    seats = []
    for result in queryResult:
        if (result[3] > 0):
            re = '+' + str(result[3])
        else:
            re = str(result[3])
        item = {
            "FlightNumber": result[0],
            "Price": result[1],
            "ClassAvgPrice": result[2],
            "Comments": re + "%",
            "ArrivalCity": result[4],
            "DepartureCity": result[5],
            "DepartureDate": result[6],
            "ArrivalDate": result[7],
            "DeptAirCode": result[8],
            "ArivAirCode": result[9],
            "AirlineName": result[10],
        }
        seats.append(item)
    return seats
    



