# cccam-info
A python script that scrapes CCcam information mostly from satellite receivers

# Sample Output

```
➜  cccam-info git:(master) python cccaminfo.py                     

    cccaminfo - by Jay Turla @shipcod3
    *********
    Usage:
    *********
    python cccaminfo.py <host> <command>
    example -> cccaminfo.py localhost clients

    *********
    Commands:
    *********
    - info
    - activeclients
    - clients
    - servers
    - shares
    - providers
    - entitlements
    
➜  cccam-info git:(master) python cccaminfo.py 109.93.138.11 servers

CCcam 2.1.4

Server connections: 1
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+
| Host                 | Connected  | Type    | Version| NodeID         | Cards | CAID/Idents                   |
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+
|xxx.homedns.me:12000  |00d 15:22:38|CCcam-s2s|2.1.4   |b3f5ede510f416b2|    38 |local 1815:000000 21631(21631) |
|                      |            |         |        |                |       |local 1802:000000 2827(2825)   |
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+
```

