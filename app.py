import numpy as np
import sqlalchemy
import pandas as pd
from flask import Flask, render_template, jsonify
import psycopg2
from flask_cors import CORS



#################################################
# Flask Setup
#################################################
app = Flask(__name__)
cors = CORS(app)

# Function to create connection and cursor to connect to the PostgreSQL Database
def create_cursor():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host='localhost',
        database='project3',
        user='postgres',
        #Replace with YOUR user password for pgadmin 4
        password='Gwqcmn47sv'
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
    return render_template("index.html")
    #return("List all available routes")



@app.route("/api/v1.0/domestic_change/<country>/boxplot")
def boxplot(country):
    conn, cursor = create_cursor()
    
    cursor.execute(f"SELECT * FROM box_plot_data where country = '{country}'")
    
    box_plot_data = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(box_plot_data)

@app.route("/api/v1.0/domestic_change/<country>/lineplot")
def lineplot(country):
    conn, cursor = create_cursor()
    
    cursor.execute(f"SELECT * FROM line_graph_data where country = '{country}'")
    
    box_plot_data = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(box_plot_data)


@app.route("/api/v1.0/domestic_commodities/<country>")
def domestic_commodities(country):
    conn, cursor = create_cursor()
    
    cursor.execute(f"SELECT DISTINCT commodity FROM line_graph_data where country = '{country}'")

    commodities = cursor.fetchall()
    
    return jsonify(commodities)

@app.route("/api/v1.0/box_country_list")
def country_list():
    conn, cursor = create_cursor()
    
    query = f"SELECT DISTINCT country FROM box_plot_data order by country"
    cursor.execute(query)
    
    countries = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(countries)

@app.route("/api/v1.0/int_commodity_list")
def commodity_list():
    conn, cursor = create_cursor()
    
    query = f"SELECT DISTINCT commodity FROM int_annual_index"
    cursor.execute(query)
    
    commodities = cursor.fetchall()
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(commodities)

@app.route("/api/v1.0/int_commodity_data")
def int_commodity_data():
    conn, cursor = create_cursor()
    
    query = f"SELECT * FROM int_annual_index"
    cursor.execute(query)
    
    commodity_data = cursor.fetchall()
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(commodity_data)

@app.route("/api/v1.0/bar_2010")
def bar_2010_data():
    conn, cursor = create_cursor()
    
    query = f"SELECT * FROM bar_2010"
    cursor.execute(query)
    
    data_2010 = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(data_2010)

@app.route("/api/v1.0/bar_2020")
def bar_2020_data():
    conn, cursor = create_cursor()
    
    query = f"SELECT * FROM bar_wheat_2020"
    cursor.execute(query)
    
    data_2020 = cursor.fetchall()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()
    
    return jsonify(data_2020)


if __name__ == "__main__":
    app.run(debug=True)