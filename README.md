# rate_limiting_service

# AB testing Results

bijnis@Bijniss-MacBook-Pro rate-limiting-service % **ab -n 20 -c 10 -H 'Accept: application/json; indent=4' -H 'Authorization: Basic YWRtaW46YWRtaW4='  'http://127.0.0.1:8000/users/' **
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /users/
Document Length:        286 bytes

Concurrency Level:      10
Time taken for tests:   0.373 seconds
Complete requests:      20
Failed requests:        10
   (Connect: 0, Receive: 0, Length: 10, Exceptions: 0)
Non-2xx responses:      10
Total transferred:      9790 bytes
HTML transferred:       3380 bytes
Requests per second:    53.61 [#/sec] (mean)
Time per request:       186.543 [ms] (mean)
Time per request:       18.654 [ms] (mean, across all concurrent requests)
Transfer rate:          25.63 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   2.0      0       8
Processing:     2  116 109.2    125     248
Waiting:        2  116 109.1    124     248
Total:          2  117 108.7    125     249

Percentage of the requests served within a certain time (ms)
  50%    125
  66%    223
  75%    233
  80%    233
  90%    241
  95%    249
  98%    249
  99%    249
 100%    249 (longest request)

