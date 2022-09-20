**Example 1: 查询DDoS攻击源信息**



Input: 

```
tccli teo DescribeDDoSAttackSourceEvent --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --ProtocolType tcp \
    --PolicyIds 1245 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "TotalCount": 1,
        "Data": [
            {
                "AttackSourceIp": "3.3.3.3",
                "AttackRegion": "GB",
                "AttackFlow": 4000,
                "AttackPacketNum": 160000
            }
        ]
    }
}
```

