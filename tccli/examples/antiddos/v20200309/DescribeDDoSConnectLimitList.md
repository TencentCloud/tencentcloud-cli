**Example 1: 获取DDoS连接抑制配置列表**



Input: 

```
tccli antiddos DescribeDDoSConnectLimitList --cli-unfold-argument  \
    --Limit 10 \
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
                        "InstanceId": "bgpip-111111q1",
                        "EipList": [
                            "1.1.1.1"
                        ]
                    }
                ],
                "ConnectLimitConfig": {
                    "SynLimit": 1,
                    "BadConnThreshold": 1,
                    "SdConnLimit": 1,
                    "SdNewLimit": 1,
                    "SynRate": 1,
                    "ConnTimeout": 1,
                    "DstConnLimit": 1,
                    "DstNewLimit": 1,
                    "NullConnEnable": 1
                }
            }
        ],
        "RequestId": "c9520936-381c-4c04-b535-c8f4df1f8059"
    }
}
```

