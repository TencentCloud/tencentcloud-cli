**Example 1: 查询DDoS攻击事件**

查询DDoS攻击事件

Input: 

```
tccli teo DescribeDDoSAttackEvent --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1 \
    --PolicyIds 1245 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --ShowDetail False \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "EventId": "12214521",
                "AttackPacketMaxRate": 10,
                "AttackEndTime": 1659595468,
                "AttackMaxBandWidth": 10,
                "AttackStartTime": 1659595468,
                "ZoneId": "zone-21xfqlh4qjee",
                "PolicyId": 1245,
                "AttackType": "UDPFLOOD",
                "AttackStatus": 1,
                "Area": "mainland",
                "DDoSBlockData": [
                    {
                        "StartTime": 1659595468,
                        "EndTime": 0,
                        "BlockArea": "Access resitricted in some regions."
                    }
                ]
            }
        ],
        "RequestId": "c0ce8b7c-a48f-4eed-a0eb-c24177efc430"
    }
}
```

