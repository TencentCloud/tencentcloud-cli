**Example 1: 获取DDoS防护的特征过滤规则列表**



Input: 

```
tccli antiddos DescribeListPacketFilterConfig --cli-unfold-argument  \
    --FilterInstanceId bgpip-0000011x \
    --FilterIp 1.1.1.1 \
    --Limit 25 \
    --Offset 0
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
                        "InstanceId": "bgpip-0000011x",
                        "EipList": [
                            "1.1.1.1"
                        ]
                    }
                ],
                "PacketFilterConfig": {
                    "MatchType2": "sunday",
                    "MatchBegin2": "begin-l5",
                    "Str2": "",
                    "SportEnd": 0,
                    "IsNot": 0,
                    "PktlenMax": 1500,
                    "MatchLogic": "none",
                    "MatchBegin": "begin-l5",
                    "Offset": 0,
                    "SportStart": 0,
                    "DportStart": 0,
                    "PktlenMin": 0,
                    "IsNot2": 0,
                    "Depth": 20,
                    "Str": "",
                    "Action": "drop",
                    "Protocol": "tcp",
                    "MatchType": "sunday",
                    "DportEnd": 0,
                    "Offset2": 5,
                    "Depth2": 20,
                    "Id": ""
                },
                "ModifyTime": "2022-01-29 17:47:48"
            }
        ],
        "RequestId": "3eb91f01-96dd-4ad3-9e16-edde46b8cf40"
    }
}
```

