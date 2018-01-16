## Python memcache client   
1. python-memcached  
- The first choice was a pure  Python solution to access memcached, that is python-memcached. It is a simple to install, understand and use solution.  
- It do not offer many customization setting, at least on its README 🙂  
- Very less or non-existent, useful documentation   
- Fails consistently for a high frequency request to memcached server. Failures are for simultaneous read on a file xxx.  I could not find an easy fix for this problem.  
- I do not suggest using it for a highly scalable application.  

2. Pylibmc  
- Bare minimum Python wrapper to C/C++ API to memcached  
- Installation was simple similar to Python-memcached  
- Offers many useful options during connection setup (such as non-blocking requests, TCP no-delay disable)  
- Shows no problem in demanding and highly scalable application  
- Shows better performance than Python-memcached  

3. memcache vs pylibmc case  
- when use memcache lib error happend as below:  
```
  File "/usr/xxx/xxx/memcachewrap.py", line 19, in MemSet
    self.mc.set(k, v, t)
  File "/usr/lib/python2.7/site-packages/memcache.py", line 700, in set
    return self._set("set", key, val, time, min_compress_len, noreply)
  File "/usr/lib/python2.7/site-packages/memcache.py", line 1020, in _set
    return _unsafe_set()
  File "/usr/lib/python2.7/site-packages/memcache.py", line 1008, in _unsafe_set
    server.send_cmd(fullcmd)
  File "/usr/lib/python2.7/site-packages/memcache.py", line 1395, in send_cmd
    self.socket.sendall(cmd + b'\r\n')
  File "/usr/lib64/python2.7/site-packages/gevent/socket.py", line 464, in sendall
    data_sent += self.send(_get_memory(data, data_sent), flags, timeout=timeleft)
  File "/usr/lib64/python2.7/site-packages/gevent/socket.py", line 441, in send 
    self._wait(self._write_event)
  File "/usr/lib64/python2.7/site-packages/gevent/socket.py", line 292, in _wait              
    assert watcher.callback is None, 'This socket is already used by another greenlet: %r' % (watcher.callback, )
AssertionError: This socket is already used by another greenlet: <bound method Waiter.switch of <gevent.hub.Waiter object at 0x442c050>>

[2018-01-10 14:55:12 GMT][][][][]<6916:32217040>(ERROR)(xxx.py#135): Traceback (most recent call last):
  File "/usr/xxxxx/xxxx/xxx.py", line 133, in idCacheUpdate                
    self.memClient.MemSet(key, id)
  File "/usr/xxx/xxx/xxx/memcachewrap.py", line 19, in MemSet
    self.mc.set(k, v, t)
  File "/usr/lib/python2.7/site-packages/memcache.py", line 700, in set
    return self._set("set", key, val, time, min_compress_len, noreply)
  File "/usr/lib/python2.7/site-packages/memcache.py", line 1020, in _set
    return _unsafe_set()
  File "/usr/lib/python2.7/site-packages/memcache.py", line 1008, in _unsafe_set
    server.send_cmd(fullcmd)
  File "/usr/lib/python2.7/site-packages/memcache.py", line 1395, in send_cmd
    self.socket.sendall(cmd + b'\r\n')
  File "/usr/lib64/python2.7/site-packages/gevent/socket.py", line 464, in sendall
    data_sent += self.send(_get_memory(data, data_sent), flags, timeout=timeleft)
  File "/usr/lib64/python2.7/site-packages/gevent/socket.py", line 441, in send
    self._wait(self._write_event)
  File "/usr/lib64/python2.7/site-packages/gevent/socket.py", line 292, in _wait
    assert watcher.callback is None, 'This socket is already used by another greenlet: %r' % (watcher.callback, )
AssertionError: This socket is already used by another greenlet: <bound method Waiter.switch of <gevent.hub.Waiter object at 0x442c050>>
```
- after we replace memcache lib with pylibmc, this isssue solved.  


result: We should use pylibmc better than memcache.  

## A useful command to check memcache server data  
`memdump --servers="localhost" | xargs memcat --servers="localhost" --verbose {} > result`  

## Reference  
- [Best Python memcache client: Python-memcached v/s Pylibmc](https://freethreads.wordpress.com/2013/10/01/best-python-memcache-client-python-memcached-vs-pylibmc/)  

