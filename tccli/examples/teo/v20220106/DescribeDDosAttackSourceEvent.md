**Example 1: 查询DDos攻击源**



Input: 

```
tccli teo DescribeDDosAttackSourceEvent --cli-unfold-argument  \
    --PageNo 0 \
    --PageSize 0 \
    --ProtocolType xx \
    --PolicyIds 12 45 78 \
    --ZoneIds zoneId1 zoneid2 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "Status": 0,
        "Msg": "success",
        "Data": {
            "PageSize": 20,
            "PageNo": 1,
            "Pages": 1,
            "TotalSize": 1,
            "List": [
                {
                    "AttackSourceIp": "3.3.3.3",
                    "AttackRegion": "GB",
                    "AttackFlow": 4000,
                    "AttackPacketNum": 160000
                }
            ]
        }
    }
}
```

