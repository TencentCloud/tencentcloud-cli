**Example 1: 查询DDos攻击事件**



Input: 

```
tccli teo DescribeDDosAttackEvent --cli-unfold-argument  \
    --PageNo 0 \
    --PageSize 0 \
    --ProtocolType xx \
    --PolicyIds 12 45 78 \
    --ZoneIds zoneId1 zoneid2 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --IsShowDetail N
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Msg": "xx",
        "Data": {
            "TotalSize": 0,
            "List": [
                {
                    "EventId": "xx",
                    "AttackPacketMaxRate": 0,
                    "AttackEndTime": 0,
                    "AttackMaxBandWidth": 0,
                    "AttackStartTime": 0,
                    "ZoneId": "xx",
                    "PolicyId": 0,
                    "AttackType": "xx",
                    "AttackStatus": 0
                }
            ],
            "PageSize": 0,
            "PageNo": 0,
            "Pages": 0
        },
        "RequestId": "xx"
    }
}
```

