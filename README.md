# cccam-info
A python script that scrapes CCcam information mostly from satellite receivers

# Sample Output

```
[+] Getting information on the receiver


CCcam 2.1.4
Current time 21:01:11
NodeID: 380ceca0f39150d3
Uptime: 17231d 20:00:52
Connected clients: 0
Active clients: 0
Total handled client ecm's: 0
Total handled client emm's: 0
Peak load (max queued requests per workerthread):



[+] Active clients


CCcam 2.1.4

Connected clients: 0
0 ACTIVE CLIENTS IN LAST 20 SECONDS
+---------+---------------+------------+------------+-----+-----+--------+----------------------+
| Username| Host          | Connected  | Idle time  | ECM | EMM | Version| Last used share      |
+---------+---------------+------------+------------+-----+-----+--------+----------------------+
+---------+---------------+------------+------------+-----+-----+--------+----------------------+

+---------+---------------------------------------+
| Username| Shareinfo                             |
+---------+---------------------------------------+
+---------+---------------------------------------+

[+] Clients


CCcam 2.1.4

Connected clients: 0
+---------+---------------+------------+------------+-----+-----+--------+----------------------+
| Username| Host          | Connected  | Idle time  | ECM | EMM | Version| Last used share      |
+---------+---------------+------------+------------+-----+-----+--------+----------------------+
+---------+---------------+------------+------------+-----+-----+--------+----------------------+

+---------+---------------------------------------+
| Username| Shareinfo                             |
+---------+---------------------------------------+
+---------+---------------------------------------+

[+] Servers


CCcam 2.1.4

Server connections: 1
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+
| Host                 | Connected  | Type    | Version| NodeID         | Cards | CAID/Idents                   |
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+
|xxx.homedns.me:12000  |00d 02:53:46|CCcam-s2s|2.1.4   |b3f5ede510f416b2|    38 |local 1815:000000 23415(23411) |
|                      |            |         |        |                |       |local 1802:000000 28(28)       |
+----------------------+------------+---------+--------+----------------+-------+-------------------------------+


[+] Active clients



Available shares: 38

+----------------------+---------+----+-----------+-----------------------------------------------+-------+------------------------+
| Host                 | Type    |Caid| System    | Providers                                     |Uphops | Nodes                  |
|                      |         |    |           |                                               |Maxdown|                        |
+----------------------+---------+----+-----------+-----------------------------------------------+-------+------------------------+
|xxx.homedns.me:12000  |CCcam-s2s| 100|seca       |6a                                             |1   0  |b3f5ede510f416b2_90000  |
|xxx.homedns.me:12000  |CCcam-s2s| 100|seca       |6a,6c                                          |1   0  |b3f5ede510f416b2_120000 |
|xxx.homedns.me:12000  |CCcam-s2s| 100|seca       |3311                                           |1   0  |b3f5ede510f416b2_1b0000 |
|xxx.homedns.me:12000  |CCcam-s2s| 100|seca       |68,6d                                          |1   0  |b3f5ede510f416b2_2f0000 |
|xxx.homedns.me:12000  |CCcam-s2s| 100|seca       |                                               |1   0  |b3f5ede510f416b2_40000  |
|xxx.homedns.me:12000  |CCcam-s2s| 100|seca       |3317                                           |1   0  |b3f5ede510f416b2_1c0000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |32830,32940,51700                              |1   0  |b3f5ede510f416b2_370001 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |42800                                          |1   0  |b3f5ede510f416b2_1d0000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |32830                                          |1   0  |b3f5ede510f416b2_100000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |32920                                          |1   0  |b3f5ede510f416b2_380000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |43800,41700,42700,42200,41200,32500,32920,42820|1   0  |b3f5ede510f416b2_200000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |30b00                                          |1   0  |b3f5ede510f416b2_2c0000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |42800,42820                                    |1   0  |b3f5ede510f416b2_2e0000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |32940                                          |1   0  |b3f5ede510f416b2_390000 |
|xxx.homedns.me:12000  |CCcam-s2s| 500|viaccess   |23800,50800,40810,60200                        |1   0  |b3f5ede510f416b2_2d0000 |
|xxx.homedns.me:12000  |CCcam-s2s| 629|irdeto     |                                               |1   0  |b3f5ede510f416b2_140003 |
|xxx.homedns.me:12000  |CCcam-s2s| 93e|nds        |0                                              |1   0  |b3f5ede510f416b2_80000  |
|xxx.homedns.me:12000  |CCcam-s2s| 963|nds        |0                                              |1   0  |b3f5ede510f416b2_280000 |
|xxx.homedns.me:12000  |CCcam-s2s| 963|nds        |                                               |1   0  |b3f5ede510f416b2_70000  |
|xxx.homedns.me:12000  |CCcam-s2s| 98c|nds        |0                                              |1   0  |b3f5ede510f416b2_270000 |
|xxx.homedns.me:12000  |CCcam-s2s| 9c4|nds        |0                                              |1   0  |b3f5ede510f416b2_50000  |
|xxx.homedns.me:12000  |CCcam-s2s| 9cd|nds        |                                               |1   0  |b3f5ede510f416b2_140000 |
|xxx.homedns.me:12000  |CCcam-s2s| b00|conax      |0                                              |1   0  |b3f5ede510f416b2_160000 |
|xxx.homedns.me:12000  |CCcam-s2s| b01|conax      |0                                              |1   0  |b3f5ede510f416b2_260000 |
|xxx.homedns.me:12000  |CCcam-s2s| d00|cryptoworks|c0,c4,c8,cc                                    |1   0  |b3f5ede510f416b2_250000 |
|xxx.homedns.me:12000  |CCcam-s2s| d95|cryptoworks|4,8,c,10                                       |1   0  |b3f5ede510f416b2_110000 |
|xxx.homedns.me:12000  |CCcam-s2s| d96|cryptoworks|                                               |1   0  |b3f5ede510f416b2_210000 |
|xxx.homedns.me:12000  |CCcam-s2s| d96|cryptoworks|0,4,8,c,10,24,28                               |1   0  |b3f5ede510f416b2_1a0000 |
|xxx.homedns.me:12000  |CCcam-s2s|1702|betacrypt  |                                               |1   0  |b3f5ede510f416b2_140002 |
|xxx.homedns.me:12000  |CCcam-s2s|1802|nagra      |2111,2011,0                                    |1   0  |b3f5ede510f416b2_f0000  |
|xxx.homedns.me:12000  |CCcam-s2s|1803|nagra      |0                                              |1   0  |b3f5ede510f416b2_3c0000 |
|xxx.homedns.me:12000  |CCcam-s2s|1810|nagra      |0                                              |1   0  |b3f5ede510f416b2_10000  |
|xxx.homedns.me:12000  |CCcam-s2s|1810|nagra      |0,4001,4101                                    |1   0  |b3f5ede510f416b2_220000 |
|xxx.homedns.me:12000  |CCcam-s2s|1815|nagra      |                                               |1   0  |b3f5ede510f416b2_330000 |
|xxx.homedns.me:12000  |CCcam-s2s|1830|nagra      |aa80,aa81,0                                    |1   0  |b3f5ede510f416b2_290000 |
|xxx.homedns.me:12000  |CCcam-s2s|1830|nagra      |                                               |1   0  |b3f5ede510f416b2_140001 |
|xxx.homedns.me:12000  |CCcam-s2s|183d|nagra      |0                                              |1   0  |b3f5ede510f416b2_150000 |
|xxx.homedns.me:12000  |CCcam-s2s|4aee|Unknown    |0                                              |1   0  |b3f5ede510f416b2_190000 |
+----------------------+---------+----+-----------+-----------------------------------------------+-------+------------------------+

[+] Providers


Available providers: 

+----+----------+--------------+-----------+
|Caid| Provider | Provider Name| System    |
+----+----------+--------------+-----------+
| 100|        6a|Unknown       |seca       |
| 100|        6c|Unknown       |seca       |
| 100|      3311|Unknown       |seca       |
| 100|        68|Unknown       |seca       |
| 100|        6d|Unknown       |seca       |
| 100|      3317|Unknown       |seca       |
| 500|     32830|Unknown       |viaccess   |
| 500|     32940|Unknown       |viaccess   |
| 500|     51700|Unknown       |viaccess   |
| 500|     42800|Unknown       |viaccess   |
| 500|     32920|Unknown       |viaccess   |
| 500|     43800|Unknown       |viaccess   |
| 500|     41700|Unknown       |viaccess   |
| 500|     42700|Unknown       |viaccess   |
| 500|     42200|Unknown       |viaccess   |
| 500|     41200|Unknown       |viaccess   |
| 500|     32500|Unknown       |viaccess   |
| 500|     42820|Unknown       |viaccess   |
| 500|     30b00|Unknown       |viaccess   |
| 500|     23800|Unknown       |viaccess   |
| 500|     50800|Unknown       |viaccess   |
| 500|     40810|Unknown       |viaccess   |
| 500|     60200|Unknown       |viaccess   |
| 93e|          |Unknown       |nds        |
| 963|          |Unknown       |nds        |
| 98c|          |Unknown       |nds        |
| 9c4|          |Unknown       |nds        |
| b00|          |Unknown       |conax      |
| b01|          |Unknown       |conax      |
| d00|        c0|Unknown       |cryptoworks|
| d00|        c4|Unknown       |cryptoworks|
| d00|        c8|Unknown       |cryptoworks|
| d00|        cc|Unknown       |cryptoworks|
| d95|         4|Unknown       |cryptoworks|
| d95|         8|Unknown       |cryptoworks|
| d95|         c|Unknown       |cryptoworks|
| d95|        10|Unknown       |cryptoworks|
| d96|          |Unknown       |cryptoworks|
| d96|         4|Unknown       |cryptoworks|
| d96|         8|Unknown       |cryptoworks|
| d96|         c|Unknown       |cryptoworks|
| d96|        10|Unknown       |cryptoworks|
| d96|        24|Unknown       |cryptoworks|
| d96|        28|Unknown       |cryptoworks|
|1802|      2111|Unknown       |nagra      |
|1802|      2011|Unknown       |nagra      |
|1802|          |Unknown       |nagra      |
|1803|          |Unknown       |nagra      |
|1810|          |Unknown       |nagra      |
|1810|      4001|Unknown       |nagra      |
|1810|      4101|Unknown       |nagra      |
|1830|      aa80|Unknown       |nagra      |
|1830|      aa81|Unknown       |nagra      |
|1830|          |Unknown       |nagra      |
|183d|          |Unknown       |nagra      |
|4aee|          |Unknown       |Unknown    |
+----+----------+--------------+-----------+

[+] Entitlements


card reader /dev/sci0
no or unknown card inserted

```

