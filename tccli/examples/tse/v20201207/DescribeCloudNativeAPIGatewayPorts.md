**Example 1: 查询云原生网关端口协议列表**

查询云原生网关端口协议列表

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayPorts --cli-unfold-argument  \
    --GatewayId gateway-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx-xxx",
        "Result": {
            "GatewayId": "gateway-xxxxxx",
            "GatewayInstancePortList": [
                {
                    "Scheme": "HTTP",
                    "PortList": [
                        80
                    ]
                },
                {
                    "Scheme": "HTTPS",
                    "PortList": [
                        443
                    ]
                },
                {
                    "Scheme": "TCP",
                    "PortList": [
                        8001,
                        8002
                    ]
                },
                {
                    "Scheme": "UDP",
                    "PortList": [
                        7001,
                        7002
                    ]
                }
            ]
        }
    }
}
```

