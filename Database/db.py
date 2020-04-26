# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:08:17 2020

@author: eugen
"""
import sqlite3
import datetime

conn = sqlite3.connect('test1.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS history (action_type text, content text, date text)""")

def add_history(action_type,content):
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('{}', '{}', '{}' )".format(action_type,content,currentDT[:16]))
    conn.commit()
    conn.close
            
def show_history():
    c.execute('SELECT * FROM history')
    print(c.fetchall())
    

def clear_history():
    c.execute("DELETE from history")
    conn.commit()
    conn.close
    
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Table01(datestamp REAL, command TEXT, action TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS backupTable01(datestamp REAL, command TEXT, action TEXT)")
        
def read_from_db_open():
    c.execute("SELECT * FROM history WHERE action_type = 'open' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

def read_from_db_search():
    c.execute("SELECT * FROM history WHERE action_type = 'search' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
       
def read_from_db_restart():
    c.execute("SELECT * FROM history WHERE action_type = 'restart' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row) 
            
def read_from_db_shutdown():
    c.execute("SELECT * FROM history WHERE action_type = 'shutdown' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)                 
        
conn.commit()
conn.close
    
def add_history(action_type,content):
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('{}', '{}', '{}' )".format(action_type,content,currentDT[:16]))
    conn.commit()
    conn.close
            
def show_history():
    c.execute('SELECT * FROM history')
    print(c.fetchall())
    
def clear_history():
    c.execute("DELETE from history")
    conn.commit()
    conn.close
#####
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Table01(datestamp REAL, command TEXT, action TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS backupTable01(datestamp REAL, command TEXT, action TEXT)")

def read_from_db_open():
    c.execute("SELECT * FROM history WHERE action_type = 'open' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

def read_from_db_search():
    c.execute("SELECT * FROM history WHERE action_type = 'search' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
       
def read_from_db_restart():
    c.execute("SELECT * FROM history WHERE action_type = 'restart' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row) 
            
def read_from_db_shutdown():
    c.execute("SELECT * FROM history WHERE action_type = 'shutdown' ")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)                 
            