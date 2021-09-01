**Example 1: 获取DDoS防护的访问限速配置列表**



Input: 

```
tccli antiddos DescribeListDDoSSpeedLimitConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-*
```

Output: 
```
{
    "Response": {
        "RequestId": "bcfa39ae-5b8b-4b5b-9e53-016176e54b59",
        "ConfigList": [
            {
                "SpeedLimitConfig": {
                    "Mode": 1,
                    "DstPortList": "0-65535",
                    "ProtocolList": "ALL",
                    "SpeedValues": [
                        {
                            "Type": 1,
                            "Value": 1200
                        }
                    ],
                    "Id": "00000001"
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

