-- MariaDB dump 10.19  Distrib 10.6.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: the_primary_keys
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `allstarfull`
--

DROP TABLE IF EXISTS `allstarfull`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `allstarfull` (
  `as_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `lgID` char(2) NOT NULL,
  `teamID` char(3) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `gameNum` smallint(6) DEFAULT NULL,
  `gameID` varchar(12) DEFAULT NULL,
  `GP` smallint(6) DEFAULT NULL,
  `startingPos` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`as_ID`),
  KEY `fk_allstar_peo` (`playerID`),
  KEY `as_player_ndx` (`playerID`),
  CONSTRAINT `fk_allstar_peo` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `appearances`
--

DROP TABLE IF EXISTS `appearances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appearances` (
  `ap_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamId` char(3) NOT NULL,
  `G_all` smallint(6) DEFAULT NULL,
  `GS` smallint(6) DEFAULT NULL,
  `G_batting` smallint(6) DEFAULT NULL,
  `G_defense` smallint(6) DEFAULT NULL,
  `G_p` smallint(6) DEFAULT NULL,
  `G_c` smallint(6) DEFAULT NULL,
  `G_1b` smallint(6) DEFAULT NULL,
  `G_2b` smallint(6) DEFAULT NULL,
  `G_3b` smallint(6) DEFAULT NULL,
  `G_ss` smallint(6) DEFAULT NULL,
  `G_lf` smallint(6) DEFAULT NULL,
  `G_cf` smallint(6) DEFAULT NULL,
  `G_rf` smallint(6) DEFAULT NULL,
  `G_of` smallint(6) DEFAULT NULL,
  `G_dh` smallint(6) DEFAULT NULL,
  `G_ph` smallint(6) DEFAULT NULL,
  `G_pr` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`ap_ID`),
  KEY `k_app_team` (`teamId`),
  KEY `a_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `awards`
--

DROP TABLE IF EXISTS `awards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
/*
CREATE TABLE `awards` (
  `aw_ID` int(12) NOT NULL AUTO_INCREMENT,
  `awardID` varchar(255) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `playerID` varchar(9) NOT NULL,
  `lgID` char(2) NOT NULL,
  `tie` varchar(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`aw_ID`),
  KEY `fk_awd_peo` (`playerID`),
  CONSTRAINT `fk_awd_peo` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `awardsshare`
--

DROP TABLE IF EXISTS `awardsshare`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
/*
CREATE TABLE `awardsshare` (
  `aws_ID` int(12) NOT NULL AUTO_INCREMENT,
  `awardID` varchar(255) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `playerID` varchar(9) NOT NULL,
  `lgID` char(2) NOT NULL,
  `divID` char(2) NOT NULL,
  `pointsWon` double DEFAULT NULL,
  `pointsMax` smallint(6) DEFAULT NULL,
  `votesFirst` double DEFAULT NULL,
  PRIMARY KEY (`aws_ID`),
  KEY `fk_awdshr_peo` (`playerID`),
  CONSTRAINT `fk_awdshr_peo` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `batting`
--

DROP TABLE IF EXISTS `batting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `batting` (
  `b_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearId` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `stint` smallint(4) NOT NULL,
  `b_G` smallint(6) DEFAULT NULL,
  `b_AB` smallint(6) DEFAULT NULL,
  `b_R` smallint(6) DEFAULT NULL,
  `b_H` smallint(6) DEFAULT NULL,
  `b_2B` smallint(6) DEFAULT NULL,
  `b_3B` smallint(6) DEFAULT NULL,
  `b_HR` smallint(6) DEFAULT NULL,
  `b_RBI` smallint(6) DEFAULT NULL,
  `b_SB` smallint(6) DEFAULT NULL,
  `b_CS` smallint(6) DEFAULT NULL,
  `b_BB` smallint(6) DEFAULT NULL,
  `b_SO` smallint(6) DEFAULT NULL,
  `b_IBB` smallint(6) DEFAULT NULL,
  `b_HBP` smallint(6) DEFAULT NULL,
  `b_SH` smallint(6) DEFAULT NULL,
  `b_SF` smallint(6) DEFAULT NULL,
  `b_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`b_ID`),
  KEY `k_bat_team` (`teamID`),
  KEY `b_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `battingpost`
--

DROP TABLE IF EXISTS `battingpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `battingpost` (
  `bp_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearId` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `round` varchar(10) NOT NULL,
  `b_G` smallint(6) DEFAULT NULL,
  `b_AB` smallint(6) DEFAULT NULL,
  `b_R` smallint(6) DEFAULT NULL,
  `b_H` smallint(6) DEFAULT NULL,
  `b_2B` smallint(6) DEFAULT NULL,
  `b_3B` smallint(6) DEFAULT NULL,
  `b_HR` smallint(6) DEFAULT NULL,
  `b_RBI` smallint(6) DEFAULT NULL,
  `b_SB` smallint(6) DEFAULT NULL,
  `b_CS` smallint(6) DEFAULT NULL,
  `b_BB` smallint(6) DEFAULT NULL,
  `b_SO` smallint(6) DEFAULT NULL,
  `b_IBB` smallint(6) DEFAULT NULL,
  `b_HBP` smallint(6) DEFAULT NULL,
  `b_SH` smallint(6) DEFAULT NULL,
  `b_SF` smallint(6) DEFAULT NULL,
  `b_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`bp_ID`),
  KEY `k_bp_team` (`teamID`),
  KEY `bp_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fielding`
--

DROP TABLE IF EXISTS `fielding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fielding` (
  `f_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `stint` smallint(4) NOT NULL,
  `position` varchar(2) DEFAULT NULL,
  `f_G` smallint(6) DEFAULT NULL,
  `f_GS` smallint(6) DEFAULT NULL,
  `f_InnOuts` smallint(6) DEFAULT NULL,
  `f_PO` smallint(6) DEFAULT NULL,
  `f_A` smallint(6) DEFAULT NULL,
  `f_E` smallint(6) DEFAULT NULL,
  `f_DP` smallint(6) DEFAULT NULL,
  `f_PB` smallint(6) DEFAULT NULL,
  `f_WP` smallint(6) DEFAULT NULL,
  `f_SB` smallint(6) DEFAULT NULL,
  `f_CS` smallint(6) DEFAULT NULL,
  `f_ZR` double DEFAULT NULL,
  PRIMARY KEY (`f_ID`),
  KEY `k_fie_team` (`teamID`),
  KEY `f_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fieldingpost`
--

DROP TABLE IF EXISTS `fieldingpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fieldingpost` (
  `fp_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `round` varchar(10) NOT NULL,
  `position` varchar(2) DEFAULT NULL,
  `f_G` smallint(6) DEFAULT NULL,
  `f_GS` smallint(6) DEFAULT NULL,
  `f_InnOuts` smallint(6) DEFAULT NULL,
  `f_PO` smallint(6) DEFAULT NULL,
  `f_A` smallint(6) DEFAULT NULL,
  `f_E` smallint(6) DEFAULT NULL,
  `f_DP` smallint(6) DEFAULT NULL,
  `f_PB` smallint(6) DEFAULT NULL,
  `f_TP` smallint(6) DEFAULT NULL,
  `f_SB` smallint(6) DEFAULT NULL,
  `f_CS` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`fp_ID`),
  KEY `k_fp_team` (`teamID`),
  KEY `fp_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `franchises`
--

DROP TABLE IF EXISTS `franchises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `franchises` (
  `franchID` varchar(3) NOT NULL,
  `franchName` varchar(50) DEFAULT NULL,
  `active` char(1) DEFAULT NULL,
  `NAassoc` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`franchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `halloffame`
--

DROP TABLE IF EXISTS `halloffame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `halloffame` (
  `hf_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `votedBy` varchar(64) NOT NULL,
  `ballots` smallint(6) DEFAULT NULL,
  `needed` smallint(6) DEFAULT NULL,
  `votes` smallint(6) DEFAULT NULL,
  `inducted` varchar(1) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `note` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`hf_ID`),
  KEY `fk_people` (`playerID`),
  CONSTRAINT `fk_people` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `homegames`
--

DROP TABLE IF EXISTS `homegames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homegames` (
  `hg_ID` int(12) NOT NULL AUTO_INCREMENT,
  `teamID` char(3) NOT NULL,
  `parkID` varchar(255) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `firstGame` date DEFAULT NULL,
  `lastGame` date DEFAULT NULL,
  `games` int(11) DEFAULT NULL,
  `openings` int(11) DEFAULT NULL,
  `attendence` int(11) DEFAULT NULL,
  PRIMARY KEY (`hg_ID`),
  KEY `k_hg_park` (`parkID`),
  KEY `h_team_ndx` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manager` (
  `m_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `inSeason` smallint(6) NOT NULL,
  `manager_G` smallint(6) DEFAULT NULL,
  `manager_W` smallint(6) DEFAULT NULL,
  `manager_L` smallint(6) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  `plyrMgr` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`m_ID`),
  KEY `fk_man_person` (`playerID`),
  KEY `m_team_ndx` (`teamID`),
  CONSTRAINT `fk_man_person` FOREIGN KEY (`playerID`) REFERENCES `people` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `park`
--

DROP TABLE IF EXISTS `park`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `park` (
  `pa_ID` int(12) NOT NULL AUTO_INCREMENT,
  `parkID` varchar(255) NOT NULL,
  `park_alias` varchar(255) DEFAULT NULL,
  `park_name` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pa_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `playerID` varchar(9) NOT NULL,
  `birthYear` int(12) DEFAULT NULL,
  `birthMonth` int(12) DEFAULT NULL,
  `birthDay` int(12) DEFAULT NULL,
  `birthCountry` varchar(255) DEFAULT NULL,
  `birthState` varchar(255) DEFAULT NULL,
  `birthCity` varchar(255) DEFAULT NULL,
  `deathYear` int(12) DEFAULT NULL,
  `deathMonth` int(12) DEFAULT NULL,
  `deathDay` int(12) DEFAULT NULL,
  `deathCountry` varchar(255) DEFAULT NULL,
  `deathState` varchar(255) DEFAULT NULL,
  `deathCity` varchar(255) DEFAULT NULL,
  `nameFirst` varchar(255) DEFAULT NULL,
  `nameLast` varchar(255) DEFAULT NULL,
  `nameGiven` varchar(255) DEFAULT NULL,
  `weight` int(10) DEFAULT NULL,
  `height` int(10) DEFAULT NULL,
  `bats` varchar(255) DEFAULT NULL,
  `throws` varchar(255) DEFAULT NULL,
  `debutDate` date DEFAULT NULL,
  `finalGameDate` date DEFAULT NULL,
  PRIMARY KEY (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pitching`
--

DROP TABLE IF EXISTS `pitching`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pitching` (
  `p_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `stint` smallint(4) NOT NULL,
  `p_W` smallint(6) DEFAULT NULL,
  `p_L` smallint(6) DEFAULT NULL,
  `p_G` smallint(6) DEFAULT NULL,
  `p_GS` smallint(6) DEFAULT NULL,
  `p_CG` smallint(6) DEFAULT NULL,
  `p_SHO` smallint(6) DEFAULT NULL,
  `p_SV` smallint(6) DEFAULT NULL,
  `p_IPOuts` int(11) DEFAULT NULL,
  `p_H` smallint(6) DEFAULT NULL,
  `p_ER` smallint(6) DEFAULT NULL,
  `p_HR` smallint(6) DEFAULT NULL,
  `p_BB` smallint(6) DEFAULT NULL,
  `p_SO` smallint(6) DEFAULT NULL,
  `p_BAOpp` double DEFAULT NULL,
  `p_ERA` double DEFAULT NULL,
  `p_IBB` smallint(6) DEFAULT NULL,
  `p_WP` smallint(6) DEFAULT NULL,
  `p_HBP` smallint(6) DEFAULT NULL,
  `p_BK` smallint(6) DEFAULT NULL,
  `p_BFP` smallint(6) DEFAULT NULL,
  `p_GF` smallint(6) DEFAULT NULL,
  `p_R` smallint(6) DEFAULT NULL,
  `p_SH` smallint(6) DEFAULT NULL,
  `p_SF` smallint(6) DEFAULT NULL,
  `p_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`p_ID`),
  KEY `k_pit_team` (`teamID`),
  KEY `p_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pitchingpost`
--

DROP TABLE IF EXISTS `pitchingpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pitchingpost` (
  `pp_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `teamID` char(3) NOT NULL,
  `round` varchar(10) NOT NULL,
  `p_W` smallint(6) DEFAULT NULL,
  `p_L` smallint(6) DEFAULT NULL,
  `p_G` smallint(6) DEFAULT NULL,
  `p_GS` smallint(6) DEFAULT NULL,
  `p_CG` smallint(6) DEFAULT NULL,
  `p_SHO` smallint(6) DEFAULT NULL,
  `p_SV` smallint(6) DEFAULT NULL,
  `p_IPOuts` int(11) DEFAULT NULL,
  `p_H` smallint(6) DEFAULT NULL,
  `p_ER` smallint(6) DEFAULT NULL,
  `p_HR` smallint(6) DEFAULT NULL,
  `p_BB` smallint(6) DEFAULT NULL,
  `p_SO` smallint(6) DEFAULT NULL,
  `p_BAOpp` double DEFAULT NULL,
  `p_ERA` double DEFAULT NULL,
  `p_IBB` smallint(6) DEFAULT NULL,
  `p_WP` smallint(6) DEFAULT NULL,
  `p_HBP` smallint(6) DEFAULT NULL,
  `p_BK` smallint(6) DEFAULT NULL,
  `p_BFP` smallint(6) DEFAULT NULL,
  `p_GF` smallint(6) DEFAULT NULL,
  `p_R` smallint(6) DEFAULT NULL,
  `p_SH` smallint(6) DEFAULT NULL,
  `p_SF` smallint(6) DEFAULT NULL,
  `p_GIDP` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`pp_ID`),
  KEY `k_pp_team` (`teamID`),
  KEY `pp_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
/*
CREATE TABLE `salary` (
  `s_ID` int(12) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(9) NOT NULL,
  `teamID` char(3) NOT NULL,
  `lgId` char(2) NOT NULL,
  `divId` char(2) NOT NULL,
  `yearId` smallint(6) NOT NULL,
  `salary` double DEFAULT NULL,
  PRIMARY KEY (`s_ID`),
  KEY `key_team` (`teamID`),
  KEY `s_player_ndx` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
/*
CREATE TABLE `school` (
  `schoolId` varchar(15) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `city` varchar(55) DEFAULT NULL,
  `state` varchar(55) DEFAULT NULL,
  `country` varchar(55) DEFAULT NULL,
  PRIMARY KEY (`schoolId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seriespost`
--

DROP TABLE IF EXISTS `seriespost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seriespost` (
  `sp_ID` int(12) NOT NULL AUTO_INCREMENT,
  `teamIDwinner` char(3) NOT NULL,
  `teamIDloser` char(3) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `round` varchar(5) NOT NULL,
  `wins` smallint(6) DEFAULT NULL,
  `losses` smallint(6) DEFAULT NULL,
  `ties` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`sp_ID`),
  KEY `k_sp_tw` (`teamIDwinner`),
  KEY `k_sp_tl` (`teamIDloser`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team` (
  `t_ID` int(12) NOT NULL AUTO_INCREMENT,
  `teamID` char(3) NOT NULL,
  `yearID` smallint(6) NOT NULL,
  `lgID` char(2) DEFAULT NULL,
  `divID` char(1) DEFAULT NULL,
  `franchID` varchar(3) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `teamRank` smallint(6) DEFAULT NULL,
  `team_G` smallint(6) DEFAULT NULL,
  `team_G_home` smallint(6) DEFAULT NULL,
  `team_W` smallint(6) DEFAULT NULL,
  `team_L` smallint(6) DEFAULT NULL,
  `DivWin` varchar(1) DEFAULT NULL,
  `WCWin` varchar(1) DEFAULT NULL,
  `LgWin` varchar(1) DEFAULT NULL,
  `WSWin` varchar(1) DEFAULT NULL,
  `team_R` smallint(6) DEFAULT NULL,
  `team_AB` smallint(6) DEFAULT NULL,
  `team_H` smallint(6) DEFAULT NULL,
  `team_2B` smallint(6) DEFAULT NULL,
  `team_3B` smallint(6) DEFAULT NULL,
  `team_HR` smallint(6) DEFAULT NULL,
  `team_BB` smallint(6) DEFAULT NULL,
  `team_SO` smallint(6) DEFAULT NULL,
  `team_SB` smallint(6) DEFAULT NULL,
  `team_CS` smallint(6) DEFAULT NULL,
  `team_HBP` smallint(6) DEFAULT NULL,
  `team_SF` smallint(6) DEFAULT NULL,
  `team_RA` smallint(6) DEFAULT NULL,
  `team_ER` smallint(6) DEFAULT NULL,
  `team_ERA` double DEFAULT NULL,
  `team_CG` smallint(6) DEFAULT NULL,
  `team_SHO` smallint(6) DEFAULT NULL,
  `team_SV` smallint(6) DEFAULT NULL,
  `team_IPouts` int(11) DEFAULT NULL,
  `team_HA` smallint(6) DEFAULT NULL,
  `team_HRA` smallint(6) DEFAULT NULL,
  `team_BBA` smallint(6) DEFAULT NULL,
  `team_SOA` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`t_ID`),
  KEY `t_team_ndx` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-30 20:29:36
