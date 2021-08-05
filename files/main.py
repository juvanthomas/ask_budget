from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
import logging
import boto3
from botocore.exceptions import ClientError
from botocore.client import Config
import requests

# ~ data of the url of views
dashboard_urls = {
    'overview': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/f5950062-44c8-4990-87ba-aac5976cd2ca/pdf",
    'product': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/05173d09-3cf7-43b7-954f-ffeb0201084e/pdf",
    'customers': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/0d7cf321-8275-47fb-89ab-4801ff7441da/pdf",
    'shipping': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/7c2d395e-06b1-4865-a34a-e6224ac5d11c/pdf",
    'performance': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/5a867a38-f317-41f1-96e2-4951eff63be3/pdf",
    'commision_model': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/05c9936d-dc4b-458d-a201-debc5bc09a01/pdf",
    'order_details': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/98dc43c1-ff10-4735-8683-e36250a4ae74/pdf",
    'forecast': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/b6fad0af-8532-4e89-b672-c8d5242bec7b/pdf",
    'what_if_forecast': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/72fb1301-1112-4a4a-93ca-5b77aa1cdd90/pdf",
    'profit': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/b0397337-d0d1-48c7-b28b-d990de327c95/pdf",
    'sales': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/e35824f8-3e84-42dd-b7be-ebe5cf7ed6df/pdf",
    'employees': "http://61.2.141.81:8080//api/3.6/sites/3dccc5ce-a7e1-498f-a3d6-816927b960cd/views/29a349ae-d4c1-4955-8d90-02392f3d1f86/pdf"

}

maping = {"1": "overview",
          "2": "product",
          "3": "customers",
          "4": "shipping",
          "5": "performance",
          "6": "commision_model",
          "7": "order_details",
          "8": "forecast",
          "9": "what_if_forecast",
          "10": "profit",
          "11": "sales",
          "12": "employees"}

# ~ logic of the program starts here

app = Flask(__name__)


@app.route("/")
def hello():
    return "#########"


@app.route("/ask", methods=['POST'])
def sms_reply():
    msg = request.json["text"]  # postman
    query = str(msg)
    try:
        dashboard_name = maping[query]
        keyword = dashboard_urls[maping[query]]
        print(maping[query])

        print('keyword = ', keyword)
        response = keyword

    except:

        response = "nothing"

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
