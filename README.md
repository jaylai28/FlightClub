# FlightClub

This project is designed to help users find the best flight deals by subscribing to a daily email service. The email will contain the best deal available for a particular destination within the next six months.
![Screenshot 2023-04-02 at 20 38 10](https://user-images.githubusercontent.com/69461406/229348683-d3c0fdf7-7a91-4640-86c4-285889819515.png)


The project has six main files: app.py, flight_data.py, flight_search.py, data_manager.py, main.py and notification_manager.py.
App.py is responsible to run the Flask application
Data_manager.py is responsible to store the data into a google sheet using Google Sheet API.
Flight_data.py is responsible to retrieve flight data from the Tequila API.
Flight_search.py is use to search for the flights based on the user requirements using Tequila API.
Notification_manager.py is responsible to send the notification via Twilio.
Main.py is used to run the program and return the best flight deals.

You will need to get API access key from Tequila website to access the flight search API.
https://tequila.kiwi.com/portal/docs/tequila_api

You will need Google Sheet API to store the data into google sheet as a database.
https://console.cloud.google.com/apis/library/sheets.googleapis.com

You will need to use Twilio API to send the message to the recipient.
https://www.twilio.com/docs/api

Overall, this project provides a convenient and automated way for users to find the best flight deals and plan their travels accordingly.
