**Example 1: DDos查询主攻击事件**



Input: 

```
tccli teo DescribeDDosMajorAttackEvent --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 1 \
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
        "Status": 0,
        "Msg": "success",
        "Data": {
            "TotalSize": 36,
            "List": [
                {
                    "AttackMaxBandWidth": 10,
                    "PolicyId": 10,
                    "AttackTime": 10
                }
            ],
            "PageSize": 12,
            "PageNo": 2,
            "Pages": 3
        },
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

