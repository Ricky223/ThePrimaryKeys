# Team: The Primary Keys
# Members: Josh McKone, Ruiqi Zhao, Varun Apte
# file: load_hall.py
# Loads data from halloffame.csv files into database

import numpy as np
import pymysql
import pandas
import csi3335sp2022 as cfg

params = []

con = pymysql.connect(host=cfg.mysql['location'],user=cfg.mysql['user'],password=cfg.mysql['password'],db=cfg.mysql['database'])

try:
    cur = con.cursor()

    # Hall of Fame Table Insert
    # playerID,yearID,votedBy,ballots,needed,votes,inducted,category,note
    sql = "INSERT INTO halloffame(playerID,yearID,votedBy,ballots,needed,votes,inducted,category,note) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('HallOfFame.csv')
    df = dataframe[['playerID','yearID','votedBy','ballots','needed','votes','inducted','category','needed_note']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    print(df1.shape)

    # Makes sure table is clear before inserting
    clearSql = "DELETE FROM halloffame;"
    cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))

    dataframe = pandas.read_csv('HallOfFameExtra.csv')
    df = dataframe[['playerID','yearID','votedBy','ballots','needed','votes','inducted','category','needed_note']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    print(df1.shape)

    # Playerid mismatch
    #for i,row in df1.iterrows():
        #cur.execute(sql, tuple(row))

except Exception:
    con.rollback()
    print("Database exception.")
    raise
else:
    con.commit()
finally:
    con.close()