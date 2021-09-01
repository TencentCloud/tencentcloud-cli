**Example 1: 获取DDoS攻击源列表**



Input: 

```
tccli dayu DescribeDDoSAttackSource --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-0000000x \
    --IpList 1.1.1.1 \
    --StartTime '2019-07-23 11:32:12' \
    --EndTime '2019-07-27 13:35:16' \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1,
        "AttackSourceList": [
            {
                "SrcIp": "1.1.1.1",
                "Province": "浙江省",
                "Nation": "中国",
                "PacketSum": 132124,
                "PacketLen": 12512551
            }
        ]
    }
}
```

