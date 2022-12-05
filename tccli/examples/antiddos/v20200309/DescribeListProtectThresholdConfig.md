**Example 1: 获取防护阈值配置列表**



Input: 

```
tccli antiddos DescribeListProtectThresholdConfig --cli-unfold-argument  \
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
                "DDoSThreshold": 1,
                "RstFloodPktThreshold": 1,
                "SynAckFloodThreshold": 1,
                "DDoSAI": "om",
                "CCEnable": 1,
                "ListenerCcThresholdList": [
                    {
                        "CCThreshold": 0,
                        "Domain": "*.examw.com",
                        "Protocol": "http",
                        "CCEnable": 0
                    }
                ],
                "AckFloodThreshold": 1,
                "SynFloodThreshold": 1,
                "InstanceDetailList": [
                    {
                        "InstanceId": "bgpip-0000011x",
                        "EipList": [
                            "1.1.1.1"
                        ]
                    }
                ],
                "CCThreshold": 1,
                "UdpFloodPktThreshold": 1,
                "AckFloodPktThreshold": 1,
                "UdpFloodThreshold": 1,
                "SynAckFloodPktThreshold": 1,
                "RstFloodThreshold": 1,
                "DDoSLevel": "middle",
                "SynFloodPktThreshold": 1
            }
        ],
        "RequestId": "f56cc9dc-29d9-4594-b12d-22239c7bc888"
    }
}
```

