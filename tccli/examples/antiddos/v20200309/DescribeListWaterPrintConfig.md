**Example 1: 获取DDoS防护的水印防护配置列表**



Input: 

```
tccli antiddos DescribeListWaterPrintConfig --cli-unfold-argument  \
    --FilterInstanceId bgpip-0000011x \
    --FilterIp 1.1.1.1 \
    --Limit 25 \
    --Offset 0
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
                            "KeyVersion": "fbf1",
                            "KeyContent": "82e352b956e8d512-fbf1-82e352b956e8d512eeb95315d5772e86fac99256",
                            "KeyId": "000005hj",
                            "KeyOpenStatus": 0,
                            "CreateTime": "2020-09-22 00:00:00"
                        }
                    ],
                    "Verify": "checkall",
                    "Listeners": [
                        {
                            "ForwardProtocol": "TCP",
                            "FrontendPort": 80,
                            "FrontendPortEnd": 0
                        }
                    ],
                    "OpenStatus": 0,
                    "Offset": 30
                },
                "InstanceDetailList": [
                    {
                        "InstanceId": "bgpip-0000011x",
                        "EipList": [
                            "1.1.1.1"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "c5ff0d5d-d2bd-4b34-b081-4acd4cf7be1f"
    }
}
```

