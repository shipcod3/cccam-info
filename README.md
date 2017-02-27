# cccam-info
A python script that gets CCcam information

# Sample Output

```
➜  ccam-info git:(master) python ccaminfo.py

    ccaminfo - by Jay Turla @shipcod3
    *********
    Usage:
    *********
    python ccaminfo.py <host> <command>
    example -> ccaminfo.py localhost clients

    *********
    Commands:
    *********    
    - activeclients
    - clients
    - servers
    - shares
    - providers
    - entitlements
    
➜  ccam-info git:(master) python ccaminfo.py 109.93.138.11 servers

CCcam 2.1.4

Server connections: 1
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+
| Host                 | Connected  | Type    | Version| NodeID         | Cards | CAID/Idents                   |
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+
|xxx.homedns.me:12000  |00d 17:46:49|CCcam-s2s|2.1.4   |b3f5ede510f416b2|    38 |local 1815:000000 10278(10278) |
|                      |            |         |        |                |       |local 1802:000000 5(5)         |
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+


```

