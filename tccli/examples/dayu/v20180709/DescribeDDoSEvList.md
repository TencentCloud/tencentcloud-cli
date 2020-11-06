**Example 1: 获取DDoS攻击事件列表**



Input: 

```
tccli dayu DescribeDDoSEvList --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-00000010 \
    --IpList 3.3.3.3 \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10' \
    --OverLoad no \
    --Limit 30 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Business": "bgpip",
        "Data": [
            {
                "Business": "bgp",
                "Id": "bgp-00000010",
                "Vip": "3.3.3.3",
                "StartTime": "2018-08-27 15:05:10",
                "EndTime": "2018-08-27 16:05:10",
                "Mbps": 231,
                "Pps": 13232,
                "AttackType": "UDPFLOOD",
                "AttackStatus": 1,
                "BlockFlag": 0,
                "OverLoad": "no"
            }
        ],
        "EndTime": "2019-03-07 14:50:00",
        "Id": "bgpip-000000y0",
        "IpList": [
            "3.3.3.3"
        ],
        "RequestId": "69b1692b-4b6e-47c0-a7d6-0ff0da286874",
        "StartTime": "2019-03-07 00:00:00",
        "Total": 1
    }
}
```

