**Example 1: DDoS攻击源IP地域分布图**



Input: 

```
tccli dayu DescribeDDoSAttackIPRegionMap --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-0000000x \
    --IpList 1.1.1.1 \
    --StartTime '2019-07-23 11:32:12' \
    --EndTime '2019-07-27 13:35:16'
```

Output: 
```
{
    "Response": {
        "RequestId": "8466d9e1-70a9-4575-8e02-df15bd50bc49",
        "NationCount": [
            {
                "Record": [
                    {
                        "Key": "Nation",
                        "Value": "韩国"
                    },
                    {
                        "Key": "AttackCount",
                        "Value": "10"
                    },
                    {
                        "Key": "PacketCount",
                        "Value": "1350"
                    },
                    {
                        "Key": "PacketBytes",
                        "Value": "564090"
                    }
                ]
            },
            {
                "Record": [
                    {
                        "Key": "Nation",
                        "Value": "保加利亚"
                    },
                    {
                        "Key": "AttackCount",
                        "Value": "15"
                    },
                    {
                        "Key": "PacketCount",
                        "Value": "3520"
                    },
                    {
                        "Key": "PacketBytes",
                        "Value": "894090"
                    }
                ]
            }
        ],
        "ProvinceCount": [
            {
                "Record": [
                    {
                        "Key": "Province",
                        "Value": "浙江省"
                    },
                    {
                        "Key": "AttackCount",
                        "Value": "25"
                    },
                    {
                        "Key": "PacketCount",
                        "Value": "3460"
                    },
                    {
                        "Key": "PacketBytes",
                        "Value": "56790"
                    }
                ]
            },
            {
                "Record": [
                    {
                        "Key": "Province",
                        "Value": "台湾省"
                    },
                    {
                        "Key": "AttackCount",
                        "Value": "35"
                    },
                    {
                        "Key": "PacketCount",
                        "Value": "3590"
                    },
                    {
                        "Key": "PacketBytes",
                        "Value": "894990"
                    }
                ]
            }
        ]
    }
}
```

