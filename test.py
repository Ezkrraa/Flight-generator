import random
import json
from datetime import datetime, timedelta


def generate_flight_data():
    flights = []
    rott = "Rotterdam"

    destinations = ['Tokyo', 'Warsaw', 'Bangkok', 'Osaka', 'Riyadh', 'Edinburgh', 'Hanoi', 'London', 'Tel Aviv', 'Dublin', 'Dallas/Fort Worth', 'Paris', 'Athens', 'Manila', 'Istanbul', 'Brisbane', 'Johannesburg', 'Toronto', 'Madrid', 'Dubai', 'Helsinki', 'Doha', 'Zurich', 'Vienna', 'Incheon', 'Frankfurt', 'São Paulo', 'Hong Kong', 'Stockholm', 'San Francisco', 'Melbourne', 'Milan', 'Singapore', 'Moscow', 'Cape Town', 'Seoul', 'Mumbai', 'Copenhagen', 'Budapest', 'Beijing', 'Brussels', 'Barcelona', 'New York', 'Los Angeles', 'Kuala Lumpur', 'Oslo', 'Prague', 'Lima', 'Sydney', 'Rome', 'Munich', 'Mexico City', 'Cairo', 'Lisbon', 'Shanghai']
    aircraft = "Boeing 737"
    gate = "A1"
    flight_token = ["AB", "CD", "EF", "GH", "IJ", "KL", "MN", "OP", "QR", "ST", "UV", "WX", "YZ"]
    
    start_date = datetime(2023, 7, 1)
    end_date = datetime(2023, 10, 31)
    
    for i in range(0, 100000):
        flight_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        flight_id = i
        flight_number = random.choice(flight_token) + str(random.randint(1000, 9999))
        dest = random.choice(destinations)
        price = random.randint(150, 400)
        
        if(random.choice([True, False])):
            origin = rott
        else:
            origin = dest
            dest = rott

        depart_time = datetime.strptime(random.choice(["09:00", "10:00", "11:00", "12:00", "13:00"]), "%H:%M")
        flight_time = round(random.uniform(1.5, 4.0), 2)
        arrival_time = (depart_time + timedelta(hours=flight_time)).strftime("%H:%M")

        flight_data = {
            "Flight-ID": flight_id,
            "Flight-number": flight_number,
            "Aircraft": aircraft,
            "Origin": origin,
            "Destination": dest,
            "Date": flight_date.strftime("%d-%m-%Y"),
            "FlightTime": flight_time,
            "DepartTime": depart_time.strftime("%H:%M"),
            "ArrivalTime": arrival_time,
            "Gate": gate,
            "SeatsTaken": [],
            "Price": price
        }
        
        flights.append(flight_data)
    
    return flights

flights_data = generate_flight_data()

# Save flight data to a JSON file
with open("flights.json", "w") as file:
    data = json.dump(flights_data, file, indent=4)

print("Flight data generated and saved to flights.json.")
