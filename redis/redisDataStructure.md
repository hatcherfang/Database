# Redis内部数据结构  
## 简单动态字符串Sds(Simple Dynamic String)--> String    
1. Sds是Redis底层所使用的字符串表示, 它被用在几乎    
所有的Redis模块中。    
2. Sds在Redis中的主要作用有两个:  
>> 1. 实现字符串对象(StringObject);  
>> 2. 在Redis程序内部用作char*类型的替代品;  
3. 对比C字符串, sds有以下特性:    
>> - 可以高效地执行长度计算(strlen)--时间复杂度为O(1);  
>> - 可以高效地执行追加操作(append)--不会出现缓冲区溢出风险;  
>> - 二进制安全--可以保存文本或者二进制数据;  
sds会为追加操作进行优化: 加快追加操作的速度, 并降低内存分配的次数,代价是多占用了一些内存, 而且这些内存不会被主动释放。    

## 双向链表--> List      
Redis列表使用两种数据结构作为底层实现：双向链表和压缩列表, 从节省内存占用考虑优先选择压缩列表。    
Redis链表实现的特性总结：  
1. 双向链表可以通过prev和next指针获取某个节点的前置或后置节点时间复杂度为O(1)。  
2. 无环:表头节点的prev指针和表尾节点的next指针都指向NULL, 对链表的访问以NULL为终点。  
3. 带链表长度计数器, 程序获取链表长度时间复杂度为O(1)。  
4. 多态：链表节点值类型是void*, 所以链表可以保存各种不同类型的值。  

## 字典--> Hash    
字典的主要用途有以下两个:    
1. 实现数据库键空间(key space)--使用字典作为redis数据库的底层实现, 对数据库的增、删、改、查操作也是构建在对字典的操作之上;  
2. 用作Hash类型键的其中一种底层实现;  
3. Redis的字典使用哈希表作为底层实现, 一个哈希表里面可以有多个哈希表节点, 而每个哈希表节点就保存了字典中的一个键值对。  
键空间(key space): Redis是一个键值对数据库, 数据库中的键值对就由字典保存, 每个数据库都有一个与之对应的字典, 这个字典被称之为键空间。    
在众多可能的实现中,Redis选择了高效且实现简单的哈希表作为字典的底层实现。使用链地址法解决键碰撞。  

## 跳跃表--> zset       
- 跳跃表在Redis中的唯一作用就是作为有序集类型的底层数据结构之一, 另外一个构成有序集的结构是字典。   
- 跳跃表结构以有序的方式在层次化的链表中保存元素，它的效率可以和平衡树媲美--查找、删除、添加等操作都可以在对数期望时间下完成。  
  
# 参考资料  
1. 《Redis设计与实现》    