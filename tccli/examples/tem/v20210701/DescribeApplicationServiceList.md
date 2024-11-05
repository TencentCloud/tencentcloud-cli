**Example 1: 查询应用访问方式列表**



Input: 

```
tccli tem DescribeApplicationServiceList --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "Name": "abc",
            "Ports": [
                0
            ],
            "Yaml": "abc",
            "ApplicationName": "abc",
            "VersionName": "abc",
            "ClusterIp": [
                "abc"
            ],
            "ExternalIp": "xx-xx-xx-xx",
            "Type": "abc",
            "SubnetId": "abc",
            "LoadBalanceId": "VPC",
            "PortMappings": [
                {
                    "Port": 0,
                    "TargetPort": 0,
                    "Protocol": "abc",
                    "ServiceName": "abc"
                }
            ],
            "ServicePortMappingList": [
                {
                    "Type": "abc",
                    "ServiceName": "abc",
                    "ClusterIp": "abc",
                    "ExternalIp": "abc",
                    "SubnetId": "abc",
                    "VpcId": "abc",
                    "LoadBalanceId": "abc",
                    "Yaml": "abc",
                    "Ports": [
                        0
                    ],
                    "PortMappingItemList": [
                        {
                            "Port": 0,
                            "TargetPort": 0,
                            "Protocol": "abc"
                        }
                    ],
                    "ExternalDomain": "abc"
                }
            ],
            "FlushAll": true,
            "EnableRegistryNextDeploy": 0,
            "ApplicationId": "abc",
            "AllIpDone": true,
            "ExternalDomain": "abc"
        },
        "RequestId": "abc"
    }
}
```

