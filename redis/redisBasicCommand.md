# Redis cli
- input command `redis-cli` to get in local redis server
- input command `redis-cli -h host -p port -a password` to get in remote redis server
- input `PING` if return `PONG`, it express redis server work
# Redis data type
- string, hash, list, set, zset(sorted set)
# Command operation
1. String
- set key "value"
- get key  
> Note: one key max storage 512MB
2. Hash
- hmset name:1 user1 user2 user3 20 //name:1 is the key
- hgetall name:1  
> Note: one hash max storage 2^32-1 key-value pair
3. List
- lpush L v1
- lpush L v2
- lpush L v3
- lrange L 0 2  
> Note: one list max storage 2^32-1 elements
4. Set(unsort set)
- format: `sadd key member`
- sadd s 1
- sadd s 2
- sadd s 3
- smembers s  
> Note: made by hash, time complexity is O(1)  
> max memmbers is 2^32-1
> return value  
   1: success
   0: exists
5. zset(sorted set)
- format: `zadd key score member`
- zadd zs 1 3
- zadd zs 0 5 
- zadd zs 2 2
- zrangebyscore zs 0 1000  
> Note: Sort member by score
