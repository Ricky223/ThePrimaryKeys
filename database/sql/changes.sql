-- This is a specific list of the changes that we have made to the existing tables

-- Indexes
CREATE INDEX as_player_ndx ON allstarfull(playerid);
CREATE INDEX a_player_ndx ON appearances(playerid);
CREATE INDEX b_player_ndx ON batting(playerid);
CREATE INDEX bp_player_ndx ON battingpost(playerid);
CREATE INDEX f_player_ndx ON fielding(playerid);
CREATE INDEX fp_player_ndx ON fieldingpost(playerid);
CREATE INDEX h_team_ndx ON homegames(teamid);
CREATE INDEX m_team_ndx ON manager(teamid);
CREATE INDEX p_player_ndx ON pitching(playerid);
CREATE INDEX pp_player_ndx ON pitchingpost(playerid);
CREATE INDEX s_player_ndx ON salary(playerid);
CREATE INDEX t_team_ndx ON team(teamid);

-- Alter Appearances
ALTER TABLE appearances ADD COLUMN G_rf smallint(6) DEFAULT NULL;

-- Changes to Fielding Post
ALTER TABLE fieldingpost CHANGE COLUMN f_WP f_TP smallint(6) DEFAULT NULL;
ALTER TABLE fieldingpost DROP COLUMN f_ZR;

-- Changes to Series Post
ALTER TABLE seriespost CHANGE COLUM loses losses smallint(6) DEFAULT NULL;

-- Changing Column ID in each table
ALTER TABLE allstarfull CHANGE COLUMN ID as_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE appearances CHANGE COLUMN ID ap_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE awards CHANGE COLUMN ID aw_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE awardsshare CHANGE COLUMN ID aws_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE batting CHANGE COLUMN ID b_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE battingpost CHANGE COLUMN ID bp_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE fielding CHANGE COLUMN ID f_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE fieldingpost CHANGE COLUMN ID fp_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE halloffame CHANGE COLUMN ID hf_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE homegames CHANGE COLUMN ID hg_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE manager CHANGE COLUMN ID m_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE park CHANGE COLUMN ID pa_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE pitching CHANGE COLUMN ID p_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE pitchingpost CHANGE COLUMN ID pp_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE salary CHANGE COLUMN ID s_ID int(12) NOT NULL AUTO_INCREMENT;
ALTER TABLE seriespost CHANGE COLUMN ID sp_ID int(12) NOT NULL AUTO_INCREMENT;

ALTER TABLE team CHANGE COLUMN ID t_ID int(12) NOT NULL AUTO_INCREMENT;


-- Drop School
DROP TABLE IF EXISTS `school`;

-- Drop Salary
DROP TABLE IF EXISTS `salary`;

-- Drop Awards tables
DROP TABLE IF EXISTS `awards`;
DROP TABLE IF EXISTS `awardsshare`;