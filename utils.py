 
import sqlite3
from sqlite3 import Error
import os
import datetime
import json
import pandas as pd

def createConnection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def createTable(conn):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS WebsiteData (
                        datetimeInfo text NOT NULL,
                        ipAddress text NOT NULL,
                        userAgent text NOT NULL,
                        operation text NOT NULL,
                        PRIMARY KEY (datetimeInfo)
                    ); """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insertData(conn,values):
    sql = ''' INSERT OR IGNORE INTO WebsiteData(datetimeInfo,ipAddress,userAgent,operation)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    #cur.executemany(sql, values)  # multiple insert
    cur.execute(sql, values) # single insert
    
    conn.commit()

    #return cur.lastrowid

def updateWebsiteInfoData(conn,values):
    sql = ''' UPDATE OR IGNORE WebsiteData set country = ?, userInfo = ? where IpAddress = ?'''
    cur = conn.cursor()
    #cur.executemany(sql, values)  # multiple insert
    cur.execute(sql,values) # single insert
    conn.commit()
    #return cur.lastrowid

def getData(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM WebsiteData")

    rows = cur.fetchall()
    return rows

'''
sqlite info
-- add column to sqlite table
ALTER TABLE WebsiteData ADD COLUMN userInfo;
update WebsiteData set userInfo = Null;
ALTER TABLE WebsiteData ADD COLUMN country
'''

if __name__ == "__main__":   
    conn = createConnection("database.db")