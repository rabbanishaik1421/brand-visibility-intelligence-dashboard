import sqlite3

def get_connection():
    con = sqlite3.connect("brandvisibilitydashboard")
    return con
