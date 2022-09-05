**Example 1: 查询DDos攻击事件**



Input: 

```
tccli teo DescribeDDosAttackEvent --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 1 \
    --ProtocolType tcp \
    --PolicyIds 1245 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --IsShowDetail N \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Msg": "success",
        "Data": {
            "TotalSize": 0,
            "List": [
                {
                    "EventId": "12214521",
                    "AttackPacketMaxRate": 10,
                    "AttackEndTime": 1659595468,
                    "AttackMaxBandWidth": 10,
                    "AttackStartTime": 1659595468,
                    "ZoneId": "zone-21xfqlh4qjee",
                    "PolicyId": 1245,
                    "AttackType": "UDPFLOOD",
                    "AttackStatus": 1
                }
            ],
            "PageSize": 1,
            "PageNo": 1,
            "Pages": 1
        },
        "RequestId": "c0ce8b7c-a48f-4eed-a0eb-c24177efc430"
    }
}
```

