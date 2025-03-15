class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self,price,origin,destination,departure_date,return_date):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.return_date = return_date

def find_affordable_flight(data):
        if data is None or not data['data']:
            print("No data available for the flight.")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

        first_flight = data['data'][0]
        lowest_price = float(first_flight['price']['grandTotal'])
        origin_city = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

        affordable_flight = FlightData(lowest_price,origin_city,destination,departure_date,return_date)

        for flight in data['data']:
            price = (flight["price"]["grandTotal"])
            if price == "N/A":
                continue
            price = float(price)
            if price < lowest_price:
                lowest_price = price
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                affordable_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
                print(f"Lowest price to {destination} is £{lowest_price}")

        return affordable_flight