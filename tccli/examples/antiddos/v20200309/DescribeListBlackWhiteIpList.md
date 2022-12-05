**Example 1: 获取DDoS防护的IP黑白名单列表**



Input: 

```
tccli antiddos DescribeListBlackWhiteIpList --cli-unfold-argument  \
    --FilterInstanceId bgpip-0000011x \
    --FilterIp 1.1.1.1 \
    --Limit 25 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "IpList": [
            {
                "InstanceDetailList": [
                    {
                        "InstanceId": "bgpip-0000011x",
                        "EipList": [
                            "1.2.2.19"
                        ]
                    }
                ],
                "Ip": "1.1.4.1",
                "Type": "white",
                "Mask": 1,
                "ModifyTime": "2022-11-29 18:34:13"
            }
        ],
        "Total": 1,
        "RequestId": "j5RV4a5576e8cf46f24e3bae026ebb391a"
    }
}
```

