**Example 1: 查询DDoS攻击事件详情**



Input: 

```
tccli teo DescribeDDoSAttackEventDetail --cli-unfold-argument  \
    --EventId 12314451244512 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "Data": {
            "EventId": "12314451244512",
            "PacketMaxRate": 10,
            "AttackType": "UDPFLOOD",
            "PolicyId": 1705,
            "StartTime": 1660010100,
            "MaxBandWidth": 100,
            "EndTime": 1660010160,
            "AttackStatus": 1
        },
        "RequestId": "dd54b175-5594-4acc-a230-75d8ae19b5bf"
    }
}
```

