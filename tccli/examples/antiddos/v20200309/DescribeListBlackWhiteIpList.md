**Example 1: 获取DDoS防护的IP黑白名单列表**



Input: 

```
tccli antiddos DescribeListBlackWhiteIpList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-0000011x
```

Output: 
```
{
    "Response": {
        "IpList": [
            {
                "InstanceDetailList": [
                    {
                        "InstanceId": "xx",
                        "EipList": [
                            "1.2.2.19"
                        ]
                    }
                ],
                "Ip": "xx",
                "Type": "xx",
                "Mask": 1,
                "ModifyTime": "xx"
            },
            {
                "InstanceDetailList": [
                    {
                        "InstanceId": "xx",
                        "EipList": [
                            "1.2.2.19"
                        ]
                    }
                ],
                "Ip": "xx",
                "Type": "xx",
                "Mask": 1,
                "ModifyTime": "xx"
            }
        ],
        "Total": 2,
        "RequestId": "xx"
    }
}
```

