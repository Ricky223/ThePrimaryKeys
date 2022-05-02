# Team: The Primary Keys
# Members: Josh McKone, Ruiqi Zhao, Varun Apte
# file: load_data.py
# Loads data from .csv files into database

import numpy as np
import pymysql
import pandas
import csi3335sp2022 as cfg

params = []

con = pymysql.connect(host=cfg.mysql['location'],user=cfg.mysql['user'],password=cfg.mysql['password'],db=cfg.mysql['database'])

try:
    cur = con.cursor()

    
    # People Table Insert
    sql = "INSERT INTO people VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('People.csv')
    # playerID, birthYear, birthMonth, birthDay, birthCountry, birthState, birthCity, deathYear, deathMonth, deathDay, deathCountry, deathState, deathCity, nameFirst, nameLast, nameGiven, weight, height, bats, throws, debutDate, finalGameDate
    df = dataframe[["playerID", "birthYear", "birthMonth", "birthDay", "birthCountry", "birthState", "birthCity", "deathYear", "deathMonth", "deathDay", "deathCountry", "deathState", "deathCity", "nameFirst", "nameLast", "nameGiven", "weight", "height", "bats", "throws", "debut", "finalGame"]]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM people;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Team Table Insert
    # teamID,yearID,lgID,divID,franchID,name,Rank,G,Ghome,W,L,DivWin,WCWin,LgWin,WSWin,R,AB,H,2B,3B,HR,BB,SO,SB,CS,HBP,SF,RA,ER,ERA,CG,SHO,SV,IPouts,HA,HRA,BBA,SOA
    sql = "INSERT INTO team(teamID,yearID,lgID,divID,franchID,name,teamRank,team_G,team_G_home,team_W,team_L,DivWin,WCWin,LgWin,WSWin,team_R,team_AB,team_H,team_2B,team_3B,team_HR,team_BB,team_SO,team_SB,team_CS,team_HBP,team_SF,team_RA,team_ER,team_ERA,team_CG,team_SHO,team_SV,team_IPouts,team_HA,team_HRA,team_BBA,team_SOA) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('Teams.csv')
    df = dataframe[['teamID','yearID','lgID','divID','franchID','name','Rank','G','Ghome','W','L','DivWin','WCWin','LgWin','WSWin','R','AB','H','2B','3B','HR','BB','SO','SB','CS','HBP','SF','RA','ER','ERA','CG','SHO','SV','IPouts','HA','HRA','BBA','SOA']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM team;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Series Post Table Insert
    # teamIDwinner,teamIDloser,yearID,round,wins,losses,ties
    sql = "INSERT INTO seriespost(teamIDwinner,teamIDloser,yearID,round,wins,losses,ties) VALUES(%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('SeriesPost.csv')
    df = dataframe[['teamIDwinner','teamIDloser','yearID','round','wins','losses','ties']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM seriespost;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Park Table Insert
    # parkID,park_alias,park_name,city,state,country
    sql = "INSERT INTO park(parkID,park_alias,park_name,city,state,country) VALUES(%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('Parks.csv')
    df = dataframe[['park.key','park.alias','park.name','city','state','country']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM park;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Manager Table Insert
    # playerID,yearID,teamID,inseason,manager_G,manager_W,manager_L,teamRank,plyrMgr
    sql = "INSERT INTO manager(playerID,yearID,teamID,inseason,manager_G,manager_W,manager_L,teamRank,plyrMgr) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('Managers.csv')
    df = dataframe[['playerID','yearID','teamID','inseason','G','W','L','rank','plyrMgr']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM manager;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Homegames Table Insert
    # teamID,parkID,yearID,firstGame,lastGame,games,openings,attendence
    sql = "INSERT INTO homegames(teamID,parkID,yearID,firstGame,lastGame,games,openings,attendence) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('HomeGames.csv')
    df = dataframe[['team.key','park.key','year.key','span.first','span.last','games','openings','attendance']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM homegames;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Franchises Table Insert
    # franchID,franchName,active,NAassoc
    sql = "INSERT INTO franchises(franchID,franchName,active,NAassoc) VALUES(%s,%s,%s,%s);"
    dataframe = pandas.read_csv('TeamsFranchises.csv')
    df = dataframe[['franchID','franchName','active','NAassoc']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM franchises;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Allstarfull Table Insert
    # playerID,lgID,teamID,yearID,gameNum,gameID,GP,startingPos
    sql = "INSERT INTO allstarfull(playerID,lgID,teamID,yearID,gameNum,gameID,GP,startingPos) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('AllstarFull.csv')
    df = dataframe[['playerID','lgID','teamID','yearID','gameNum','gameID','GP','startingPos']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM allstarfull;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------
    
    # Appearances Table Insert
    # playerID,yearID,teamID,G_all,GS,G_batting,G_defense,G_p,G_c,G_1b,G_2b,G_3b,G_ss,G_lf,G_cf,G_rf,G_of,G_dh,G_ph,G_pr
    sql = "INSERT INTO appearances(playerID,yearID,teamID,G_all,GS,G_batting,G_defense,G_p,G_c,G_1b,G_2b,G_3b,G_ss,G_lf,G_cf,G_rf,G_of,G_dh,G_ph,G_pr) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('Appearances.csv')
    df = dataframe[['playerID','yearID','teamID','G_all','GS','G_batting','G_defense','G_p','G_c','G_1b','G_2b','G_3b','G_ss','G_lf','G_cf','G_rf','G_of','G_dh','G_ph','G_pr']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    # Makes sure table is clear before inserting
    #clearSql = "DELETE FROM appearances;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------
    
    # Batting table insert
    # playerID,yearID,teamID,stint,G,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,IBB,HBP,SH,SF,GIDP
    sql = "INSERT INTO batting(playerID,yearId,teamID,stint,b_G,b_AB,b_R,b_H,b_2B,b_3B,b_HR,b_RBI,b_SB,b_CS,b_BB,b_SO,b_IBB,b_HBP,b_SH,b_SF,b_GIDP) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('Batting.csv')
    df = dataframe[['playerID','yearID','teamID','stint','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    #clearSql = "DELETE FROM batting;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Batting post table insert
    # playerID,yearID,teamID,stint,G,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,IBB,HBP,SH,SF,GIDP
    sql = "INSERT INTO battingpost(playerID,yearId,teamID,round,b_G,b_AB,b_R,b_H,b_2B,b_3B,b_HR,b_RBI,b_SB,b_CS,b_BB,b_SO,b_IBB,b_HBP,b_SH,b_SF,b_GIDP) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('BattingPost.csv')
    df = dataframe[['playerID','yearID','teamID','round','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    #clearSql = "DELETE FROM battingpost;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Pitching Table insert
    # playerID,yearID,teamID,stint,W,L,G,GS,CG,SHO,SV,IPouts,H,ER,HR,BB,SO,BAOpp,ERA,IBB,WP,HBP,BK,BFP,GF,R,SH,SF,GIDP
    sql = "INSERT INTO pitching(playerID,yearID,teamID,stint,p_W,p_L,p_G,p_GS,p_CG,p_SHO,p_SV,p_IPouts,p_H,p_ER,p_HR,p_BB,p_SO,p_BAOpp,p_ERA,p_IBB,p_WP,p_HBP,p_BK,p_BFP,p_GF,p_R,p_SH,p_SF,p_GIDP) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('Pitching.csv')
    df = dataframe[['playerID','yearID','teamID','stint','W','L','G','GS','CG','SHO','SV','IPouts','H','ER','HR','BB','SO','BAOpp','ERA','IBB','WP','HBP','BK','BFP','GF','R','SH','SF','GIDP']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    #clearSql = "DELETE FROM pitching;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # PitchingPost Table insert
    # playerID,yearID,teamID,round,W,L,G,GS,CG,SHO,SV,IPouts,H,ER,HR,BB,SO,BAOpp,ERA,IBB,WP,HBP,BK,BFP,GF,R,SH,SF,GIDP
    sql = "INSERT INTO pitchingpost(playerID,yearID,teamID,round,p_W,p_L,p_G,p_GS,p_CG,p_SHO,p_SV,p_IPouts,p_H,p_ER,p_HR,p_BB,p_SO,p_BAOpp,p_ERA,p_IBB,p_WP,p_HBP,p_BK,p_BFP,p_GF,p_R,p_SH,p_SF,p_GIDP) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('PitchingPost.csv')
    df = dataframe[['playerID','yearID','teamID','round','W','L','G','GS','CG','SHO','SV','IPouts','H','ER','HR','BB','SO','BAOpp','ERA','IBB','WP','HBP','BK','BFP','GF','R','SH','SF','GIDP']]
    df = df.replace([np.inf, -np.inf], None)
    df1 = df.astype(object).where(pandas.notnull(df), None)

    #clearSql = "DELETE FROM pitchingpost;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # Fielding Table insert
    # playerID,yearID,teamID,stint,POS,G,GS,InnOuts,PO,A,E,DP,PB,WP,SB,CS,ZR
    sql = "INSERT INTO fielding(playerID,yearID,teamID,stint,position,f_G,f_GS,f_InnOuts,f_PO,f_A,f_E,f_DP,f_PB,f_WP,f_SB,f_CS,f_ZR) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('Fielding.csv')
    df = dataframe[['playerID','yearID','teamID','stint','POS','G','GS','InnOuts','PO','A','E','DP','PB','WP','SB','CS','ZR']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    #clearSql = "DELETE FROM fielding;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    dataframe = pandas.read_csv('FieldingOFsplit.csv')
    df = dataframe[['playerID','yearID','teamID','stint','POS','G','GS','InnOuts','PO','A','E','DP','PB','WP','SB','CS','ZR']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    
    #--------------------

    # FieldingPost Table insert
    # playerID,yearID,teamID,round,POS,G,GS,InnOuts,PO,A,E,DP,PB,TP,SB,CS
    sql = "INSERT INTO fieldingpost(playerID,yearID,teamID,round,position,f_G,f_GS,f_InnOuts,f_PO,f_A,f_E,f_DP,f_PB,f_TP,f_SB,f_CS) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dataframe = pandas.read_csv('FieldingPost.csv')
    df = dataframe[['playerID','yearID','teamID','round','POS','G','GS','InnOuts','PO','A','E','DP','PB','TP','SB','CS']]
    df1 = df.astype(object).where(pandas.notnull(df), None)

    #clearSql = "DELETE FROM fieldingpost;"
    #cur.execute(clearSql)

    for i,row in df1.iterrows():
        cur.execute(sql, tuple(row))
    

except Exception:
    con.rollback()
    print("Database exception.")
    raise
else:
    con.commit()
finally:
    con.close()