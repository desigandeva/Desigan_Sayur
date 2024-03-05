# designing a database for a local cricket club about players, matches, and team statistics.
#
# 1. **Players:**
#    - Each player has a  name, age, role (batsman, bowler, all-rounder), and nationality.
#    - Some players have additional details such as batting average, bowling average, and total runs scored.
#
# 2. **Matches:**
#    - Store match details like  date, venue, opponent team, and result.
# 
# 3. **Player_Matches:**
#    - Include information about the players participating in each match, their roles, and
#     any specific statistics (runs scored, wickets taken, etc.) for that match.
#
# 4. **Teams:**
#    - Details of the teams affiliated with the club, including  name, coach, and captain.
#


import mysql.connector

# connect the local database
mysql = mysql.connector.connect(host="localhost",user="root",password="root",database="cricket_club")
mycursor = mysql.cursor()

# 1. Retrieve all players' details.
query1 = "select * from player"
# 2. Get the details of matches played in a specific venue.
query2 = "select * from matches where m_Venue = 'Chennai'"
# 3. List all matches where a particular player participated.
query3 = "select m_Id,p_Name from playerMatches where p_Name='Ram'"
# 4. Find players with a batting average above a certain value.
query4 = "select p_Name,p_Bat_Avg from player where p_Bat_Avg > 60"
# 5. Display the team details along with the list of players in each team.
query5 = "select team.t_Name,count(p_Name) as Total_Player from player join team on player.t_Name = team.t_Name group by player.t_Name"
# 6. Find the top-performing players based on their batting or bowling statistics across all matches.
query6 = "select * from player where p_Bat_Avg=(select max(p_Bat_Avg) from player)"
query6 = "select * from player where p_Bow_Avg=(select max(p_Bow_Avg) from player)"
# 7. List the total number of players in each team
query7 = "select team.t_Name,count(p_Name) as Total_Player from player join team on player.t_Name = team.t_Name group by player.t_Name"
# 8. List the teams that has more than 20 team members.
query8 = "select t_Name from player where (select count(*) from player as p where p.t_Name=player.t_Name)>20 group by t_Name" 

# execute the query
mycursor.execute(query1)
# mycursor.execute(query2)
# mycursor.execute(query3)
# mycursor.execute(query4)
# mycursor.execute(query5)
# mycursor.execute(query6)
# mycursor.execute(query7)
# mycursor.execute(query8)

# print the value
for item in mycursor:
    print(item)