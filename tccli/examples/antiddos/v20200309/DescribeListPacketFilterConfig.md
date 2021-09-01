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
        "RequestId": "53f8e307-fc36-41dd-99a4-0b8e3b3a9408",
        "ConfigList": [
            {
                "PacketFilterConfig": {
                    "Protocol": "",
                    "SportStart": 0,
                    "SportEnd": 0,
                    "DportStart": 0,
                    "DportEnd": 0,
                    "PktlenMin": 0,
                    "PktlenMax": 1500,
                    "Action": "drop",
                    "MatchBegin": "begin_l5",
                    "MatchType": "sunday",
                    "Str": "hello",
                    "Depth": 20,
                    "Offset": 0,
                    "IsNot": 0,
                    "MatchLogic": "and",
                    "MatchBegin2": "begin_l5",
                    "MatchType2": "sunday",
                    "Str2": "world",
                    "Depth2": 20,
                    "Offset2": 5,
                    "IsNot2": 0,
                    "Id": "00e8v4zj"
                },
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.1.1.1"
                        ],
                        "InstanceId": "bgpip-0000011x"
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```

