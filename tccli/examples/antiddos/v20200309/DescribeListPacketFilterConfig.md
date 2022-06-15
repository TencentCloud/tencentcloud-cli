**Example 1: 获取DDoS防护的特征过滤规则列表**



Input: 

```
tccli antiddos DescribeListPacketFilterConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-0000011x
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "ConfigList": [
            {
                "InstanceDetailList": [
                    {
                        "InstanceId": "xx",
                        "EipList": [
                            "1.1.1.1"
                        ]
                    }
                ],
                "PacketFilterConfig": {
                    "MatchType2": "xx",
                    "MatchBegin2": "xx",
                    "Str2": "xx",
                    "SportEnd": 0,
                    "IsNot": 0,
                    "PktlenMax": 1500,
                    "MatchLogic": "xx",
                    "MatchBegin": "xx",
                    "Offset": 0,
                    "SportStart": 0,
                    "DportStart": 0,
                    "PktlenMin": 0,
                    "IsNot2": 0,
                    "Depth": 20,
                    "Str": "xx",
                    "Action": "xx",
                    "Protocol": "xx",
                    "MatchType": "xx",
                    "DportEnd": 0,
                    "Offset2": 5,
                    "Depth2": 20,
                    "Id": "xx"
                },
                "ModifyTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

