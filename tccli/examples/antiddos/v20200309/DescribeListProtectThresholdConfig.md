**Example 1: 获取防护阈值配置列表**



Input: 

```
tccli antiddos DescribeListProtectThresholdConfig --cli-unfold-argument  \
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
                "DDoSThreshold": 1,
                "DDoSAI": "xx",
                "CCEnable": 1,
                "CCThreshold": 1,
                "InstanceDetailList": [
                    {
                        "InstanceId": "xx",
                        "EipList": [
                            "1.1.1.1"
                        ]
                    }
                ],
                "ListenerCcThresholdList": [
                    {
                        "CCThreshold": 0,
                        "Domain": "xx",
                        "Protocol": "xx",
                        "CCEnable": 0
                    }
                ],
                "DDoSLevel": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

