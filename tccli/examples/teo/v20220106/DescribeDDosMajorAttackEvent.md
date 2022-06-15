**Example 1: DDos查询主攻击事件**



Input: 

```
tccli teo DescribeDDosMajorAttackEvent --cli-unfold-argument  \
    --PageNo 0 \
    --PageSize 0 \
    --ProtocolType xx \
    --PolicyIds 0 \
    --ZoneIds zoneId1 zoneid2 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00
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
                    "AttackMaxBandWidth": 0,
                    "PolicyId": 0,
                    "AttackTime": 0
                }
            ],
            "PageSize": 12,
            "PageNo": 2,
            "Pages": 3
        },
        "RequestId": "xx"
    }
}
```

