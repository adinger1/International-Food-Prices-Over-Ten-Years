import numpy as np
import sqlalchemy
import pandas as pd
from flask import Flask, jsonify
import psycopg2


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# Function to create connection and cursor to connect to the PostgreSQL Database
def create_cursor():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host='localhost',
        database='project3',
        user='postgres',
        password='*BlackSkies7'
    )

    # Create a cursor to interact with the database
    cursor = conn.cursor()
    return conn, cursor

#################################################
# Flask Routes
#################################################

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/percent_price_changes<br/>"
        f"/api/v1.0/domestic_change<br/>"
        f"/api/v1.0/international_food_price_data"
    )

@app.route("/api/v1.0/percent_price_changes")
def percent_price_changes():
    
    conn, cursor = create_cursor()
    cursor.execute('SELECT country,commodity,post_covid FROM percent_change_post_covid')
    #percentage_display_data = db.session.query(percent_change.country,percent_change.commodity,percent_change.post_covid).all()

    percentage_display_data = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(percentage_display_data)


    
@app.route("/api/v1.0/domestic_change")
def domestic_change():
    conn, cursor = create_cursor()
    
    cursor.execute('SELECT * FROM dom_cleaned_data')

    domestic_data = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(domestic_data)
 
@app.route("/api/v1.0/international_food_price_data")
def international_data():
    conn, cursor = create_cursor()
    
    cursor.execute('SELECT * FROM int_clean_data_cleaned')

    international_data = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(international_data)



if __name__ == "__main__":
    app.run(debug=True)