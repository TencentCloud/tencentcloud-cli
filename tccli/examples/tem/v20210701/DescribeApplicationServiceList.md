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
        "RequestId": "7003cb9f-0932-4cba-b15a-21788df3a8fb",
        "Result": {
            "PortMappings": [],
            "LoadBalanceId": "",
            "SubnetId": "",
            "Type": "",
            "Name": "",
            "ApplicationName": "app0925",
            "ClusterIp": [],
            "ExternalIp": "",
            "ExternalDomain": "",
            "VersionName": "",
            "Ports": [],
            "Yaml": "",
            "ApplicationId": "app-5vaz8x85",
            "ServicePortMappingList": [
                {
                    "Type": "CLUSTER",
                    "ServiceName": "k8s-svc-test",
                    "ClusterIp": "172.16.56.122",
                    "ExternalIp": "",
                    "ExternalDomain": "",
                    "SubnetId": "",
                    "VpcId": "",
                    "LoadBalanceId": "",
                    "Yaml": "apiVersion: xxx",
                    "Ports": [
                        8080
                    ],
                    "PortMappingItemList": [
                        {
                            "Port": 8080,
                            "TargetPort": 8080,
                            "Protocol": "TCP"
                        }
                    ]
                },
                {
                    "Type": "CLUSTER",
                    "ServiceName": "pk-svc",
                    "ClusterIp": "172.16.52.35",
                    "ExternalIp": "",
                    "ExternalDomain": "",
                    "SubnetId": "",
                    "VpcId": "",
                    "LoadBalanceId": "",
                    "Yaml": "apiVersion: xxx",
                    "Ports": [
                        8080
                    ],
                    "PortMappingItemList": [
                        {
                            "Port": 8080,
                            "TargetPort": 8080,
                            "Protocol": "TCP"
                        }
                    ]
                }
            ],
            "FlushAll": false,
            "EnableRegistryNextDeploy": 0,
            "AllIpDone": true
        }
    }
}
```

