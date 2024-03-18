# 1. Design a DB for keepting all the data for the movie theatres in Madurai.
# For each theatre you need to keep track of the name, phone number, web site address,
#  number of seats, location and owner details.
# Keep the owner details (such as name, address, phone number) in a separate table and connect with the theatre table.
# Write queries to print the following data. Add additional info in the table if needed.
# The number of theatres in Madurai that were built before 2010.
# The name and address of the theatre owners who have more than 3 theatres.
# 
# 2. For each theatre, keep track of the movies currently playing and when (the date that movie started playing 
# in that theatre)
# Write queries for the following
# The list of all the movies playing in Madurai (don't repeat the names)
# The movie thats been playing the longest time.
# The movie thats been playing in most theatres now
# 
# Design a DB for movie theatres in Madurai.
# For each theatre the name, phone number, web site address,number of seats, location and owner details.
# Keep the owner details (such as name, address, phone number) in a separate table and connect with the theatre table
# create table theatre_owner(oId varchar(5) not null,oName varchar(25) not null,oAddress varchar(250) not null,oPhoneNo bigint not null, primary key(oId));
# create table theatre(oId varchar(5) not null,tId varchar(5) not null,tName varchar(25) not null,tPhoneNo bigint not null,tWeb varchar(25) not null,tSeats int not null,tLocation varchar(150) not null,tSince int not null,primary key(tId));
# create table movie(tId varchar(5) not null,mName varchar(40) not null,mRDays int not null,mSDate date not null)
# 

# import mysql connector
import mysql.connector

# connect with local database
mysql = mysql.connector.connect(host='localhost',user='root',password='root',database='movie_theatre')
mycursor = mysql.cursor()

# build the function for get data from database for give query
def printResult(query):
    # execute a query
    mycursor.execute(query)
    # print the result
    for item in mycursor:
        print(item)
    print()


# The number of theatres in Madurai that were built before 2010.
print("The number of theatres in Madurai that were built before 2010")
printResult("select count(tName) from theatre where tSince < 2010")
# The name and address of the theatre owners who have more than 3 theatres.
print("The name and address of the theatre owners who have more than 3 theatres")
printResult("select theatre_owner.oName,theatre_owner.oAddress from theatre_owner join theatre on theatre_owner.oId=theatre.oId where (select count(*) from theatre as t1 where theatre.oId=t1.oId)>3 group by theatre.oId")
# The list of all the movies playing in Madurai (don't repeat the names)
print("The list of all the movies playing in Madurai")
printResult("select distinct mName from movie")
# The movie thats been playing the longest time.
print("The movie thats been playing the longest time")
printResult("select mName from movie where mRDays = (select max(mRDays) from movie)")
# The movie thats been playing in most theatres now
print("The movie thats been playing in most theatres")
printResult("select mName from movie group by mName limit 1")