**Example 1: 获取DDoS防护的AI防护开关列表**



Input: 

```
tccli antiddos DescribeListDDoSAI --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-0000011x
```

Output: 
```
{
    "Response": {
        "RequestId": "c8c3f585-dd94-4d99-b877-f2c612445630",
        "ConfigList": [
            {
                "DDoSAI": "off",
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.1.1.1"
                        ],
                        "InstanceId": "bgpip-0000011y"
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```

