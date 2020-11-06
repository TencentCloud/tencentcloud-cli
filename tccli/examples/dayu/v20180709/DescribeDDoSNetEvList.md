**Example 1: 获取高防IP专业版资源的DDoS攻击事件列表**



Input: 

```
tccli dayu DescribeDDoSNetEvList --cli-unfold-argument  \
    --Business net \
    --Id net-00000010 \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10' \
    --Limit 30 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Business": "net",
        "Data": [
            {
                "Business": "bgp",
                "Id": "bgp-00000010",
                "StartTime": "2018-08-27 15:05:10",
                "EndTime": "2018-08-27 16:05:10",
                "Mbps": 231,
                "Pps": 13232,
                "AttackType": "UDPFLOOD",
                "AttackStatus": 1,
                "BlockFlag": 2,
                "OverLoad": ""
            }
        ],
        "EndTime": "2019-03-07 14:50:00",
        "Id": "net-000000y0",
        "RequestId": "69b1692b-4b6e-47c0-a7d6-0ff0da286874",
        "StartTime": "2019-03-07 00:00:00",
        "Total": 1
    }
}
```

