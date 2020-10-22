# Emotions API

This API is for testing purposes. It receives an ad_id as parameter (as part of the URL, example: http://localhost/ad_stats/445534) and returns an emoji based on the ad performance (views and contacts).

## How to Run

In order to get this application up & running you have two options described below...

## Locally

To run this application you need python installed (versions 2 and 3 are well supported).

Once you have python installed just make sure to install the dependencies by running:

`pip install -r requirements.txt`

or 

`pip3 install -r requirements.txt` for python 3 

And you can run the app with the following command:

`sudo python app.py`

or

`sudo python3 app.py` for python 3

NOTE: Sudo privileges are required since the app open a port for http connections handler in the host machine.

## Docker 

If you want to run the application in docker just follow these steps :

###### Build

To build the docker image run:

`docker build -t emotions-api .`

NOTE: You must be in the same directory as the Dockerfile

###### Run

Once you succesfully built the image you can run it with:

`docker run -p 80:80/tcp -d emotions-api`

NOTE: In this case the application is being exposed in the 80 port (change it if needed). Ex. 8080:80/tcp if you want to reach the app in the 8080 port.

###### Test

Once the application is running you should be able to reach it using the following command:

`curl "http://localhost/ad_stats/445534"`

Or with your web browser going to http://localhost/ad_stats/445534 and you should see an output like:

`{"ad_id":"445534","emoji":"bad","num_contacts":46,"num_views":19,"version":"1.0"}`


