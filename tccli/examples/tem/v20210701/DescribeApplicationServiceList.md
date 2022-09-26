**Example 1: 查询应用访问方式列表**



Input: 

```
tccli tem DescribeApplicationServiceList --cli-unfold-argument  \
    --EnvironmentId xx \
    --ApplicationId xx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ApplicationName": "xx",
            "ExternalIp": "xx",
            "Name": "xx",
            "ApplicationId": "xx",
            "AllIpDone": true,
            "PortMappings": [
                {
                    "Protocol": "xx",
                    "ServiceName": "xx",
                    "TargetPort": 0,
                    "Port": 0
                }
            ],
            "Yaml": "xx",
            "LoadBalanceId": "xx",
            "ServicePortMappingList": [
                {
                    "ExternalIp": "xx",
                    "VpcId": "xx",
                    "PortMappingItemList": [
                        {
                            "Protocol": "xx",
                            "TargetPort": 0,
                            "Port": 0
                        }
                    ],
                    "Yaml": "xx",
                    "LoadBalanceId": "xx",
                    "ServiceName": "xx",
                    "ClusterIp": "xx",
                    "SubnetId": "xx",
                    "Type": "xx",
                    "Ports": [
                        0
                    ]
                }
            ],
            "VersionName": "xx",
            "ClusterIp": [
                "xx"
            ],
            "SubnetId": "xx",
            "Type": "xx",
            "Ports": [
                0
            ],
            "EnableRegistryNextDeploy": 0,
            "FlushAll": true
        },
        "RequestId": "xx"
    }
}
```

