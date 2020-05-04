import unittest
import sqlite3
from unittest import TestCase
import datetime

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS history (action_type text, content text, date text)""") 
    
def show():
    c.execute('SELECT * FROM history')
    data = c.fetchall()
    return len(data)

def clear_history():
    conn = sqlite3.connect('clear.db')
    c = conn.cursor()
    c.execute("DELETE from history")
    c.execute('SELECT * FROM history')
    data = c.fetchall()
    return len(data)
        
def read_from_db_open():
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('open', 'word', '{}' )".format(currentDT[:16]))
    c.execute("SELECT * FROM history WHERE action_type = 'open'")
    data = c.fetchall()
    return len(data)


def read_from_db_search():
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('search', 'word', '{}' )".format(currentDT[:16]))
    c.execute("SELECT * FROM history WHERE action_type = 'search'")
    data = c.fetchall()
    return len(data)
       
def read_from_db_restart():
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('restart', 'word', '{}' )".format(currentDT[:16]))
    c.execute("SELECT * FROM history WHERE action_type = 'restart'")
    data = c.fetchall()
    return len(data)
           
def read_from_db_shutdown():
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('shutdown', 'word', '{}' )".format(currentDT[:16]))
    c.execute("SELECT * FROM history WHERE action_type = 'shutdown'")
    data = c.fetchall()
    return len(data)
   
def read_from_db_sleep():
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('sleep', 'word', '{}' )".format(currentDT[:16]))
    c.execute("SELECT * FROM history WHERE action_type = 'sleep'")
    data = c.fetchall()
    return len(data)

def read_from_db_lock():
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('lock', 'word', '{}' )".format(currentDT[:16]))
    c.execute("SELECT * FROM history WHERE action_type = 'lock'")
    data = c.fetchall()
    return len(data)

def read_from_db_tweet():
    currentDT = str(datetime.datetime.now()) 
    c.execute("INSERT INTO history VALUES ('tweet', 'word', '{}' )".format(currentDT[:16]))
    c.execute("SELECT * FROM history WHERE action_type = 'tweet'")
    data = c.fetchall()
    return len(data)

class test(unittest.TestCase):
    
    def test_show(self):
        self.assertNotEqual(show(),0)
    
    def test_clear(self):
        self.assertEqual(clear_history(),0)
    
    def test_read_open(self):
        self.assertNotEqual(read_from_db_open(),0)
        
    def test_read_search(self):
        self.assertNotEqual(read_from_db_search(),0)
        
    def test_read_restart(self):
        self.assertNotEqual(read_from_db_restart(),0)
        
    def test_read_shutdown(self):
        self.assertNotEqual(read_from_db_shutdown(),0)
        
    def test_read_sleep(self):
        self.assertNotEqual(read_from_db_sleep(),0)
        
    def test_read_lock(self):
        self.assertNotEqual(read_from_db_lock(),0)
        
    def test_read_tweet(self):
        self.assertNotEqual(read_from_db_tweet(),0)
        
    
    
if __name__ == '__main__':
    unittest.main()
