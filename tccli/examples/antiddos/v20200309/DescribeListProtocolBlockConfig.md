**Example 1: 获取DDoS防护的协议封禁配置列表**



Input: 

```
tccli antiddos DescribeListProtocolBlockConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-0000011x
```

Output: 
```
{
    "Response": {
        "RequestId": "70a4b0a9-4dc9-4a29-ae47-ce1c498b176a",
        "ConfigList": [
            {
                "ProtocolBlockConfig": {
                    "DropTcp": 0,
                    "DropUdp": 0,
                    "DropIcmp": 0,
                    "DropOther": 0,
                    "CheckExceptNullConnect": 0
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

