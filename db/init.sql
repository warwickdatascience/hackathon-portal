CREATE DATABASE hackathon_portal;

USE hackathon_portal;
CREATE TABLE admin(admin_id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(30), password BLOB, salt BLOB);
CREATE TABLE team(team_id INT PRIMARY KEY AUTO_INCREMENT, teamname VARCHAR(30))
CREATE TABLE user(userteam_id INT PRIMARY KEY AUTO_INCREMENT, user_id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(30), password BLOB, salt BLOB)
CREATE TABLE userteam(team_id INT, user_id INT, FOREIGN KEY(team_id) REFERENCES team(team_id), FOREIGN KEY(user_id) REFERENCES user(user_id))
CREATE TABLE submission(submission_id INT PRIMARY KEY AUTO_INCREMENT, team_id INT, user_id INT, score INT, tag VARCHAR(100), FOREIGN KEY(team_id) REFERENCES team(team_id), FOREIGN KEY(user_id) REFERENCES user(user_id))

