**Example 1: 根据网络探测ID验证探测参数**



Input: 

```
tccli vpc CheckNetDetectState --cli-unfold-argument  \
    --Version 2017-03-12\
    --NetDetectId netd-12345678\
    --DetectDestinationIp 10.0.0.2 10.0.0.3\
    --NextHopType NORMAL_CVM\
    --NextHopDestination 10.0.0.4
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

**Example 2: 根据输入信息验证探测参数**



Input: 

```
tccli vpc CheckNetDetectState --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcId vpc-12345678\
    --SubnetId subnet-12345678\
    --NetDetectName test\
    --DetectDestinationIp 10.0.0.5 10.0.0.6\
    --NextHopType NORMAL_CVM\
    --NextHopDestination 10.0.0.4
```

Output: 
```
{
    "Response": {
        "NetDetectIpStateSet": [
            {
                "DetectDestinationIp": "10.0.0.5",
                "State": 0,
                "Delay": 0,
                "PacketLossRate": 0
            },
            {
                "DetectDestinationIp": "10.0.0.6",
                "State": 0,
                "Delay": 0,
                "PacketLossRate": 0
            }
        ],
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

