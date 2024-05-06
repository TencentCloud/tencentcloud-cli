**Example 1: 查询 Gateway 列表**



Input: 

```
tccli tcm DescribeIstioGatewayList --cli-unfold-argument  \
    --MeshID mesh-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "GatewayList": [
            {
                "GatewayNamespace": "namespace",
                "GatewayName": "name",
                "GatewayServers": [
                    {
                        "Name": "gs-name",
                        "Bind": "xxxx",
                        "CertID": "xxxx",
                        "Port": {
                            "Number": 80,
                            "Protocol": "HTTP",
                            "Name": "p-name",
                            "TargetPort": 8080
                        }
                    }
                ]
            }
        ],
        "RequestId": "xxxxxxx"
    }
}
```

