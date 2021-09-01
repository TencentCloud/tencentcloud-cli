**Example 1: 获取DDoS防护的水印防护配置列表**



Input: 

```
tccli antiddos DescribeListWaterPrintConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-0000011x
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "ConfigList": [
            {
                "WaterPrintConfig": {
                    "Keys": [
                        {
                            "KeyVersion": "xx",
                            "KeyContent": "xx",
                            "KeyId": "xx",
                            "CreateTime": "2020-09-22 00:00:00"
                        }
                    ],
                    "Listeners": [
                        {
                            "ForwardProtocol": "xx",
                            "FrontendPort": 80
                        }
                    ],
                    "OpenStatus": 0,
                    "Offset": 30
                },
                "InstanceDetailList": [
                    {
                        "InstanceId": "xx",
                        "EipList": [
                            "1.1.1.1"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

