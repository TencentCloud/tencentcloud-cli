**Example 1: 查询微服务实例详情**



Input: 

```
tccli tsf DescribeMicroservice --cli-unfold-argument  \
    --MicroserviceId ms-xxxxxxx \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4d967308-2667-4fa3-ae84-d3fb19960c37",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "InstanceId": "ins-xxxxxxx",
                    "InstanceName": "test3",
                    "Port": "18083",
                    "LanIp": "172.30.0.10",
                    "WanIp": "94.191.90.25",
                    "ApplicationId": "application-xxxxxxx",
                    "ApplicationName": "test",
                    "GroupId": "group-xxxxxxx",
                    "GroupName": "coumser-test",
                    "NamespaceId": null,
                    "NamespaceName": null,
                    "ClusterId": null,
                    "ClusterName": null,
                    "ClusterType": "V",
                    "InstanceStatus": null,
                    "InstanceAvailableStatus": null,
                    "ServiceInstanceStatus": "Running",
                    "HealthCheckUrl": null,
                    "ApplicationPackageVersion": "1.14.1_Finchley",
                    "ApplicationType": "V"
                }
            ]
        }
    }
}
```

