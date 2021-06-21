**Example 1: 获取转发监听器列表**



Input: 

```
tccli antiddos DescribeListListener --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "83ef9ee6-a46a-4aa7-b8aa-42c65637edad",
        "Layer4Listeners": [
            {
                "BackendPort": 12,
                "FrontendPort": 12,
                "Protocol": "TCP",
                "RealServers": [
                    {
                        "RealServer": "1.1.1.1",
                        "RsType": 2,
                        "Weight": 50
                    }
                ],
                "InstanceDetails": [
                    {
                        "EipList": [
                            "1.1.1.1"
                        ],
                        "InstanceId": "bgpip-0000011e"
                    }
                ]
            }
        ],
        "Layer7Listeners": [
            {
                "Domain": "121.test.com",
                "ProxyTypeList": [
                    {
                        "ProxyPorts": [
                            443
                        ],
                        "ProxyType": "https"
                    }
                ],
                "RealServers": [
                    {
                        "RealServer": "1.1.1.1",
                        "RsType": 2,
                        "Weight": 100
                    }
                ],
                "InstanceDetails": [
                    {
                        "EipList": [
                            "1.1.1.1"
                        ],
                        "InstanceId": "bgpip-000000y2"
                    }
                ]
            }
        ]
    }
}
```

