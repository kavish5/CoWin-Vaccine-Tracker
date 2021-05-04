import requests
import datetime
import json
import sys

pin_code = str(sys.argv[1])
age = int(sys.argv[2])
days = int(sys.argv[3])

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(days)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

for input_date in date_str:
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
        pin_code, input_date)
    response = requests.get(url)
    if response.ok:
        result = response.json()
        flag = False
        if result["centers"]:
            print("Available on: {}".format(input_date))
            for center in result["centers"]:
                for session in center["sessions"]:
                    if session["min_age_limit"] <= age:
                        print("Place: ", center["name"])
                        print("Address: ", center["address"])
                        print("Zone Name: ", center["block_name"])
                        print("Free/Paid: ", center["fee_type"])
                        print("Available Capacity: ",
                              session["available_capacity"])
                        if(session["vaccine"] != ''):
                            print("Vaccine: ", session["vaccine"])
                        print("\n")
        else:
            print("No available slots on {}".format(input_date))
