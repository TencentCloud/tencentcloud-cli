**Example 1: 查询DDos攻击源信息**



Input: 

```
tccli teo DescribeDDosAttackSourceEvent --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 1 \
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

