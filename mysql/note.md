##**MySQL Table Locking**
refer:`http://www.mysqltutorial.org/mysql-table-locking/`  
###LOCK and UNLOCK TABLES syntax  
The simple form of acquiring a lock for a table is as follows:  
```
LOCK TABLES table_name [READ | WRITE]
```
You put the name of the table after the LOCK TABLES keywords and followed by a lock type.   
MySQL provides two lock types: READ and WRITE.  
We will go into detail of each lock type in the next section.
To release a lock for a table, you use the following statement:  
```
UNLOCK TABLES;
```
###Table locking for READ  
A READ lock for a table has the following features:  
- A READ lock for a table can be acquired by multiple sessions at the same time. In addition, other sessions can read data from the table without acquiring the lock.  
- The session that holds the READ lock can only read data from the table, but not write. In addition, other sessions cannot write data into the table until the READ lock is released. The write operations from another session will be put into the waiting states until the READ lock is released.  
- If the session is terminated normally or abnormally, MySQL will release all the locks implicitly. This is also relevant for the WRITE lock.  
Let’s take a look at how the READ lock works in the following scenario.  
First, connect to the sampledb database. To find out the current connection id, you use the CONNECTION_ID() function as follows:  
`SELECT CONNECTION_ID();`  
![first-session-id](https://github.com/hatcherfang/Database/mysql/img/first-sessioon-id.jpg)
