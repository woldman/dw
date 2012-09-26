#!/usr/bin/env python

import sqlite3 
import sys

con = sqlite3.connect('dw_esc.db')

CREATE_STATEMENT = '''
CREATE TABLE escapes
(
    dtmin REAL,
    dtmax REAL,
    threshold REAL,
    noise REAL,
    escapetime REAL
)
'''

with con:
    cur = con.cursor()
    cur.execute(CREATE_STATEMENT)
