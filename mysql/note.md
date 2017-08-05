## **MySQL Table Locking**  
refer:`http://www.mysqltutorial.org/mysql-table-locking/`  
### LOCK and UNLOCK TABLES syntax  
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
### Table locking for READ  
A READ lock for a table has the following features:  
- A READ lock for a table can be acquired by multiple sessions at the same time. In addition, other sessions can read data from the table without acquiring the lock.  
- The session that holds the READ lock can only read data from the table, but not write. In addition, other sessions cannot write data into the table until the READ lock is released. The write operations from another session will be put into the waiting states until the READ lock is released.  
- If the session is terminated normally or abnormally, MySQL will release all the locks implicitly. This is also relevant for the WRITE lock.  
Let’s take a look at how the READ lock works in the following scenario.  
First, connect to the sampledb database. To find out the current connection id, you use the CONNECTION_ID() function as follows:  
```
SELECT CONNECTION_ID();
``` 
![first-session-id](https://github.com/hatcherfang/Database/blob/master/mysql/img/first-session-id.jpg)  
Then, insert a new row into the tbl table.  
```
INSERT INTO tbl(col) VALUES(10);
```
Next, retrieve all rows from the same table.  
```
SELECT * FROM tbl;
```
![tbl-data-first-session](https://github.com/hatcherfang/Database/blob/master/mysql/img/tbl-data-first-session.jpg)  

After that, to acquire a lock, you use the LOCK TABLE statement.  
```
LOCK TABLE tbl READ;
```
Finally, in the same session, if you try to insert a new row into the tbl table, you will get an error message.  
eg:  
```
INSERT INTO tbl(col) VALUES(11);
```
```
Error Code: 1099. Table \'tbl\' was locked with a READ lock and can\'t be updated.  
```
So the once READ lock is acquired, you cannot write data into the table within the same session. Let’s check the READ lock from a different session.  

First, connect to the sampledb and check the connection id:  
```
SELECT CONNECTION_ID();
```
![table-lock-second-session](https://github.com/hatcherfang/Database/blob/master/mysql/img/table-lock-second-session.jpg)  
Then, retrieve data from the tbl .   
```
SELECT * FROM tbl;
```
![tbl-data-first-session](https://github.com/hatcherfang/Database/blob/master/mysql/img/tbl-data-first-session.jpg)  
Next, insert a new row into the tbl table from the second session.  
```
INSERT INTO tbl(col) VALUES(20);
```
![table-lock-waiting-status](https://github.com/hatcherfang/Database/blob/master/mysql/img/table-lock-waiting-status.jpg)  
The insert operation from the second session is in the waiting state because a READ lock already acquired on the tbl table by the first session and it has not released yet.  

You can see the detailed information from the **SHOW PROCESSLIST** statement.  
```
SHOW PROCESSLIST;
```
![show-processlist-table-lock](https://github.com/hatcherfang/Database/blob/master/mysql/img/show-processlist-table-lock.jpg)  

After that, go back to the first session and release the lock by using the UNLOCK TABLES statement. After you release the READ lock from the first session, the INSERT operation in the second session executed.  

Finally, check it the data of the tbl table to see if the INSERT operation from the second session really executed.  
```
SELECT * FROM tbl;
```
![tbl-data-after-releasing-lock](https://github.com/hatcherfang/Database/blob/master/mysql/img/tbl-data-after-releasing-lock.jpg)  
### MySQL table locking for WRITE  
The table lock for WRITE has the following features:  

- Only session that holds the lock of a table can read and write data from the table.  
- Other sessions cannot read and write from the table until the WRITE lock is released.  
Let’s go into detail to see how the WRITE lock works.  

First, acquire a WRITE lock from the first session.  
```
LOCK TABLE tbl WRITE;
```
Then, insert a new row into the tbl table.  
```
INSERT INTO tbl(col) VALUES(11);
```
It works.  

Next, read data from the tbl table.  

```
SELECT * FROM tbl;
```
![table-lock-write](https://github.com/hatcherfang/Database/blob/master/mysql/img/table-lock-write.jpg)  
It is fine.  

After that, from the second session, try to write and read data:  

```
INSERT INTO tbl(col) VALUES(21);

SELECT * FROM tbl;
```

MySQL puts those operations into a waiting state. You can check it using the SHOW PROCESSLIST statement.  

```
SHOW PROCESSLIST
```
![show-processlist-table-lock1](https://github.com/hatcherfang/Database/blob/master/mysql/img/show-processlist-table-lock1.jpg)  
Finally, release the lock from the first session.  

```
UNLOCK TABLES;  
```
You will see all pending operations from the second session executed.  
![table-tbl-data-after-unlock](https://github.com/hatcherfang/Database/blob/master/mysql/img/table-tbl-data-after-unlock.jpg)  
In this tutorial, we have shown you how to lock and unlock tables for READ and WRITE to cooperate table access between sessions.  

### Related Tutorials  

[MySQL Transaction](http://www.mysqltutorial.org/mysql-transaction.aspx)  
