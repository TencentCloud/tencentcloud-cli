**Example 1: DDoS查询主攻击事件**



Input: 

```
tccli teo DescribeDDoSMajorAttackEvent --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --ProtocolType tcp \
    --PolicyIds 1705 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "AttackMaxBandWidth": 10,
                "PolicyId": 10,
                "AttackTime": 10
            }
        ],
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

