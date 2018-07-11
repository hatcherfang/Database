## mysql type convert  
- MySQL 的CAST()和CONVERT()函数可用来获取一个类型的值，并产生另一个类型的值。两者具体的语法如下：  
sql:  
```
CAST(value as type);  
CONVERT(value, type); 
```
 可转换的类型是以下值中的一个：  
```
    二进制，同带binary前缀的效果 : BINARY    
    字符型，可带参数 : CHAR()     
    日期 : DATE     
    时间: TIME     
    日期时间型 : DATETIME     
    浮点数 : DECIMAL      
    整数 : SIGNED     
    无符号整数 : UNSIGNED 
```
eg1:  
```
mysql> SELECT CONVERT('23',SIGNED);  
+----------------------+  
| CONVERT('23',SIGNED) |  
+----------------------+  
|                   23 |  
+----------------------+  
1 row in set  
```
eg2:  
```
mysql> SELECT CAST('125e342.83' AS signed);  
+------------------------------+  
| CAST('125e342.83' AS signed) |  
+------------------------------+  
|                          125 |  
+------------------------------+  
1 row in set  
```
eg3:  
```
mysql> SELECT CAST('3.35' AS signed);  
+------------------------+  
| CAST('3.35' AS signed) |  
+------------------------+  
|                      3 |  
+------------------------+  
1 row in set  
```
## Reference  
[字符串转int/double CAST与CONVERT函数的用法](http://hongmin118.iteye.com/blog/2029728)  
