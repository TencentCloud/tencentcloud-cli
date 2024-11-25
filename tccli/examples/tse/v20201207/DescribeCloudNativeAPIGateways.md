**Example 1: 测试获取云原生API网关实例列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGateways --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "67e07f5b-d31a-47b3-8a67-bf10e48fc1a6",
        "Result": {
            "TotalCount": 1,
            "GatewayList": [
                {
                    "GatewayId": "gateway-dde03767",
                    "Name": "公网入口网关",
                    "IngressClassName": "tse-nginx-ingress",
                    "Type": "kong",
                    "GatewayVersion": "2.5.1",
                    "GatewayMinorVersion": "",
                    "NodeConfig": {
                        "Specification": "1c2g",
                        "Number": 2
                    },
                    "VpcConfig": {
                        "VpcId": "vpc-83p0o405",
                        "SubnetId": "subnet-8tzp8ugg"
                    },
                    "Description": "",
                    "Status": "Running",
                    "EnableCls": false,
                    "CreateTime": "2024-10-08 20:27:38",
                    "Tags": [],
                    "TradeType": 0,
                    "FeatureVersion": "PROFESSIONAL",
                    "InternetMaxBandwidthOut": 1,
                    "AutoRenewFlag": 0,
                    "CurDeadline": "2024-10-08 20:27:38",
                    "IsolateTime": "2024-10-08 20:27:38",
                    "EnableInternet": true,
                    "EngineRegion": "ap-guangzhou",
                    "InternetPayMode": "TRAFFIC",
                    "LoadBalancerType": "",
                    "PublicIpAddresses": [
                        "193.112.82.224"
                    ]
                }
            ]
        }
    }
}
```

