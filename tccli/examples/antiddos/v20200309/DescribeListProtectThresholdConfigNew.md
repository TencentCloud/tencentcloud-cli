**Example 1: 获取防护阈值配置列表**

获取防护阈值配置列表

Input: 

```
tccli antiddos DescribeListProtectThresholdConfigNew --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --FilterIp abc \
    --FilterInstanceId abc \
    --FilterDomain abc \
    --FilterProtocol abc
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "ConfigList": [
            {
                "DDoSLevel": "abc",
                "DDoSThreshold": 1,
                "DDoSAI": "abc",
                "CCEnable": 1,
                "CCThreshold": 1,
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "abc"
                        ],
                        "InstanceId": "abc"
                    }
                ],
                "ListenerCcThresholdList": [
                    {
                        "Domain": "abc",
                        "Protocol": "abc",
                        "CCEnable": 0,
                        "CCThreshold": 0
                    }
                ],
                "SynFloodThreshold": 1,
                "SynFloodPktThreshold": 1,
                "UdpFloodThreshold": 1,
                "UdpFloodPktThreshold": 1,
                "AckFloodThreshold": 1,
                "AckFloodPktThreshold": 1,
                "SynAckFloodThreshold": 1,
                "SynAckFloodPktThreshold": 1,
                "RstFloodThreshold": 1,
                "RstFloodPktThreshold": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

