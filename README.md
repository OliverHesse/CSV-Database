# CSV-Database: a csv database that also includes a very primitive sql parser. managed to sneak a binary tree in here :)
currently supports SELECT, INSERT, UPDATE<br>
also supports WHERE statements with AND,OR using these operators:<br>
==,<=,>=,<,>,!=<br>
here is an example select command<br>
db.execute("SELECT id FROM UserData WHERE Username == Oliver AND Password == NOTAREALPASSWORD") <br>
its not the best axample but it works<br><br>
whilst not able to parse these it does have min max and total methods. each of these allow you to conditionaly use them<br>
example:<br>
db.MIN("Transactions","TransactionTotal","WHERE id == 0002")
i know amazing.<br>
it will support DELETE, but I am currently busy so cant rn<br>

Best thing about this database is that it is staticly typed. WHOA i know shocking<br>
the way i manage this is using the header of the csv file.<br>
here you will store Table information like this:<br>
Id:int,Username:str,valid:bool,account_total:float<br><br>

as you can see we define our column followed by a : and its type the database currently supports int, str, bool and float with not plans to add more because that is more work than i care for<br><br>

you can initialise all tables at once using a schema file.<br>
by using setup_from_csv("filename") you can create all the nescesary tables at once. if one of the tables exists it will not overwrite it and i will not add a DROP TABLE IF EXIST<br>
the schema file will be setup similar to a regular csv table file. the only 2 differences are that each row is a new table, and the first item must be the table name<br>
UserData,id:int,Username:str,HashedPassword:str,salt:str,accountType:str<br>
as we cab see here we define all the clomuns but start with the table name.<br><br>
Amazing isnt it
<br><br>
Do note that in the where method there is some bloat due to testing i was doing at the time. not sure when i will fix it but eventualy i will
