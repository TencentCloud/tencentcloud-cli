**Example 1: 获取DDoS连接抑制配置列表**



Input: 

```
tccli antiddos DescribeDDoSConnectLimitList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
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
        "RequestId": "xx"
    }
}
```

