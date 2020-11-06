**Example 1: 根据ID查询网络探测验证结果列表**



Input: 

```
tccli vpc DescribeNetDetectStates --cli-unfold-argument  \
    --Version 2017-03-12 \
    --NetDetectIds netd-12345678
```

Output: 
```
{
    "NetDetectStateSet": [
        {
            "NetDetectId": "netd-2owwwwd0",
            "NetDetectIpStateSet": [
                {
                    "DetectDestinationIp": "10.0.0.2",
                    "State": 0,
                    "Delay": 0,
                    "PacketLossRate": 0
                },
                {
                    "DetectDestinationIp": "10.0.0.3",
                    "State": 0,
                    "Delay": 0,
                    "PacketLossRate": 0
                }
            ]
        }
    ],
    "TotalCount": 1,
    "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
}
```

