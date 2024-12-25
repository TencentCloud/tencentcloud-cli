**Example 1: 查询虚拟机部署组详情**



Input: 

```
tccli tsf DescribeGroup --cli-unfold-argument  \
    --GroupId group-oydzed8v
```

Output: 
```
{
    "Response": {
        "RequestId": "69d37373-076d-4905-9cdd-7810878fd6f6",
        "Result": {
            "AgentProfileList": [],
            "Alias": null,
            "ApplicationId": "application-yx8kjmra",
            "ApplicationName": "mesh-no-spec",
            "ApplicationType": "C",
            "ClusterId": "cls-rawagafs",
            "ClusterName": "billow-ks8",
            "CreateTime": "2024-12-17 19:57:08",
            "DeployBatch": [
                1
            ],
            "DeployBetaEnable": false,
            "DeployDesc": null,
            "DeployExeMode": "auto",
            "DeployWaitTime": 0,
            "EnableBatchHealthCheck": false,
            "EnableHealthCheck": false,
            "GatewayConfig": null,
            "GroupDesc": null,
            "GroupId": "group-ab3pj26y",
            "GroupName": "user-with-nospec",
            "GroupResourceType": "DEF",
            "GroupStatus": "Paused",
            "HealthCheckSettings": null,
            "InstanceCount": 0,
            "MicroserviceType": "M",
            "NamespaceId": "namespace-y4n8xepv",
            "NamespaceName": "billow-ks8_default",
            "OffInstanceCount": 0,
            "PackageId": null,
            "PackageName": null,
            "PackageType": null,
            "PackageVersion": null,
            "RunInstanceCount": 0,
            "StartScript": null,
            "StartupParameters": null,
            "StopScript": null,
            "UpdateTime": "2024-12-17 19:57:30",
            "UpdateType": 1,
            "UpdatedTime": 1734436650000,
            "WarmupSetting": {
                "Curvature": 2,
                "Enabled": false,
                "EnabledProtection": true,
                "WarmupTime": 60
            }
        }
    }
}
```

