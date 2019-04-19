## Event  
eg:  
每天定时清理 test表, create_time超过7天的数据   
```
create event e_delete_test on schedule every 1 DAY STARTS '2019-04-18 00:05:00' on completion preserve enable comment 'clear test table data that more than 7 days' DO delete from test where date(create_time) <=date_sub(CURDATE(), INTERVAL 7 DAY);
```
## Reference  
[Mysql 时间操作（当天，昨天，7天，30天，半年，全年，季度）](https://josh-persistence.iteye.com/blog/2128275)  
[mysql的event(事件)用法详解](https://blog.csdn.net/lixia755324/article/details/53923856)  
[mysql定时删除过期数据记录](https://blog.csdn.net/u011249920/article/details/78246647)  
