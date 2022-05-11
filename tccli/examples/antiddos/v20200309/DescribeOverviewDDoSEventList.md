**Example 1: 获取防护概览的ddos攻击事件**



Input: 

```
tccli antiddos DescribeOverviewDDoSEventList --cli-unfold-argument  \
    --StartTime '2020-02-01 12:04:12' \
    --EndTime '2020-02-03 18:03:23'
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1,
        "EventList": [
            {
                "Id": "ddosev-00000421",
                "Vip": "10.143.145.42",
                "StartTime": "2021-04-14 14:14:54",
                "EndTime": "2021-04-14 14:16:23",
                "AttackType": "SYNFLOOD",
                "AttackStatus": 0,
                "Mbps": 23414,
                "Pps": 2313,
                "Business": "bgpip",
                "InstanceId": "bgpip-00000143",
                "InstanceName": "test"
            }
        ]
    }
}
```

