## Database  
study database  
## 关系型(SQL)数据库与非关系型(NoSQL -> Not Only SQL)数据库的区别  
1. NoSQL数据库只能用来处理行为数据, 因为NoSQL强调所谓的分布式, 然后又有CAP的概念  
也就是说在保证数据吞吐量的基础上, 会在数据的一致性上大打一个折扣, 也就是说如果要处理  
用户的交易数据, 主要是跟钱有关的数据我们是不可能用NoSQL数据库去保存的, 只有这种行为数据  
才有可能被保存到NoSQL数据库里面。   
