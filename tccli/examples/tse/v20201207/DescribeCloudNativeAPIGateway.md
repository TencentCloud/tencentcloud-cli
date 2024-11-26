**Example 1: 测试获取云原生API网关基础信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGateway --cli-unfold-argument  \
    --GatewayId gateway-dde03767
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-dde03767",
            "Status": "Running",
            "Name": "公网入口网关",
            "Type": "kong",
            "GatewayVersion": "2.5.1",
            "NodeConfig": {
                "Specification": "1c2g",
                "Number": 2
            },
            "VpcConfig": {
                "VpcId": "vpc-83p0o405",
                "SubnetId": "subnet-8tzp8ugg"
            },
            "Description": "公网入口网关",
            "CreateTime": "2024-10-08 20:27:38",
            "Tags": [
                {
                    "TagKey": "app",
                    "TagValue": "learn"
                }
            ],
            "EnableCls": true,
            "TradeType": 0,
            "FeatureVersion": "STANDARD",
            "InternetMaxBandwidthOut": 1,
            "AutoRenewFlag": 0,
            "CurDeadline": "2024-12-02 16:11:41",
            "IsolateTime": "2024-10-08 20:27:38",
            "EnableInternet": true,
            "EngineRegion": "ap-guangzhou",
            "IngressClassName": "kong",
            "InternetPayMode": "TRAFFIC",
            "GatewayMinorVersion": "2.5.1.11",
            "InstancePort": {
                "HttpPort": "80",
                "HttpsPort": "443",
                "TcpPort": "8000",
                "UdpPort": "7000"
            },
            "LoadBalancerType": "L7"
        },
        "RequestId": "9b2bc5f8-0c9f-43b4-8517-3e6cf6c6a7a0"
    }
}
```

