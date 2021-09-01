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
        "RequestId": "83978459-3a66-46e7-bb97-c946656d16eb",
        "IpList": [
            {
                "Ip": "123.123.123.2",
                "Type": "white",
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.2.2.19"
                        ],
                        "InstanceId": "bgpip-0000011x"
                    }
                ]
            },
            {
                "Ip": "123.123.123.1",
                "Type": "black",
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.2.2.19"
                        ],
                        "InstanceId": "bgpip-0000011x"
                    }
                ]
            }
        ],
        "Total": 2
    }
}
```

