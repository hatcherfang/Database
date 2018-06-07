import redis


class Redis(object):
    '''redis api test code'''
    def __init__(self, host="localhost", port=6379):
        self.host = host
        self.port = port
        self.conn = redis.Redis(host=host, port=port)

    def sdsTest(self):
        '''---string test---'''
        self.conn.set("s1", "sfang")
        print self.conn.get("s1")

    def linkListTest(self):
        '''---double end link list used for list---'''
        key = "link1"
        for i in xrange(10):
            self.conn.rpush(key, i)
        len1 = self.conn.llen(key)
        print self.conn.lrange(key, 0, len1)
        print self.conn.rpop(key)

    def dictTest(self):
        '''---dict test used for dict---'''
        key = "dict1"
        for k in xrange(10):
            self.conn.hset(key, k, k)
        len1 = self.conn.hlen(key)
        print len1
        print self.conn.hgetall(key)

    def skiplistTest(self):
        '''---skiplist test used for sorted set---'''
        key = 'fruit-price'
        self.conn.zadd(key, "banana", 2)
        self.conn.zadd(key, "apple", 5)
        self.conn.zadd(key, "pears", 1)
        print self.conn.zrange(key, 0, 3, desc=True, withscores=True)

    def intsetTest(self):
        '''---intset test used for integer type set---'''
        key = 'numbers'
        for i in xrange(40):
            self.conn.sadd(key, i)
        print self.conn.smembers(key)

    def ziplistTest(self):
        '''---ziplist used for list type---'''
        key = "zlst"
        self.conn.delete(key)
        self.conn.rpush(key, 1)
        self.conn.rpush(key, 3)
        self.conn.rpush(key, 5)
        self.conn.rpush(key, 10086)
        self.conn.rpush(key, "hello world")
        len1 = self.conn.llen(key)
        print self.conn.lrange(key, 0, len1)
        print self.conn.type(key)
        # help(self.conn.object)
        # print self.conn.object(key)

    def objectTest(self):
        '''---object type test---'''
        # string type object
        print '''\n---string type object---'''
        key1 = "typestring"
        # self.conn.delete(key1)
        self.conn.set(key1, "hello world")
        print "string value:%r" % self.conn.get(key1)
        print "type:%r" % self.conn.type(key1)
        print "encoding:%r" % self.conn.object("encoding", key1)
        print "STRLEN:%r" % self.conn.strlen(key1)
        print '''\n---int+str=>str---'''
        key2 = "number"
        self.conn.set(key2, 10086)
        print "key:number, value:%r" % self.conn.get(key2)
        print "encoding:%r" % self.conn.object("encoding", key2)
        self.conn.append(key2, " is a good number!")
        print "key:number, value:%r" % self.conn.get(key2)
        print "encoding:%r" % self.conn.object("encoding", key2)
        print '''\n---update embstr type will always convert it to raw---'''
        key3 = "msg"
        self.conn.set(key3, "hello world")
        print "key:%r, value:%r" % (key3, self.conn.get(key3))
        print "encoding:%r" % self.conn.object("encoding", key3)
        self.conn.append(key3, " again!")
        print "after append key:%r, value:%r" % (key3, self.conn.get(key3))
        print "encoding:%r" % self.conn.object("encoding", key3)
        print '\n---other API test---'
        key4 = "strAPI"
        self.conn.set(key4, 1)
        print "key:%r, value:%r" % (key4, self.conn.get(key4))
        self.conn.incr(key4)
        print "API: incr key:%r, value:%r" % (key4, self.conn.get(key4))


        # hash type object
        print '''\n---hash type object---'''
        key4 = "typehash"
        # self.conn.delete(key2)
        self.conn.hmset(key4, {"name": "tom"})
        self.conn.hmset(key4, {"age": 15})
        print "hash type all value:%r" % self.conn.hgetall(key4)
        print "hash type key: name, value:%r" % self.conn.hmget(key4, "name")
        print "encoding:%r" % self.conn.object("encoding", key4)
        print "type:%r" % self.conn.type(key4)


if __name__ == '__main__':
    redisObj = Redis(host="localhost", port=6379)
    # print redisObj.sdsTest.__doc__
    # redisObj.sdsTest()
    # print redisObj.linkListTest.__doc__
    # redisObj.linkListTest()
    # print redisObj.dictTest.__doc__
    # redisObj.dictTest()
    # print redisObj.skiplistTest.__doc__
    # redisObj.skiplistTest()
    # print redisObj.intsetTest.__doc__
    # redisObj.intsetTest()
    # print redisObj.ziplistTest.__doc__
    # redisObj.ziplistTest()
    print redisObj.objectTest.__doc__
    print redisObj.objectTest()
