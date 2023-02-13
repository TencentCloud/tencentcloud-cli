**Example 1: 根据网络探测ID验证探测参数**

根据网络探测ID验证探测参数

Input: 

```
tccli vpc CheckNetDetectState --cli-unfold-argument  \
    --NetDetectId netd-12345678 \
    --NextHopType NORMAL_CVM \
    --NextHopDestination 10.0.0.4 \
    --DetectDestinationIp 10.0.0.3 10.0.0.2
```

Output: 
```
{
    "Response": {
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
        ],
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

