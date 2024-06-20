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
        "Result": {
            "TotalCount": 0,
            "Content": [
                {
                    "InstanceId": "abc",
                    "InstanceName": "abc",
                    "Port": "abc",
                    "LanIp": "abc",
                    "WanIp": "abc",
                    "InstanceAvailableStatus": "abc",
                    "ServiceInstanceStatus": "abc",
                    "ApplicationId": "abc",
                    "ApplicationName": "abc",
                    "ClusterId": "abc",
                    "ClusterName": "abc",
                    "NamespaceId": "abc",
                    "NamespaceName": "abc",
                    "GroupId": "abc",
                    "GroupName": "abc",
                    "InstanceStatus": "abc",
                    "HealthCheckUrl": "abc",
                    "ClusterType": "abc",
                    "ApplicationPackageVersion": "abc",
                    "ApplicationType": "abc",
                    "ServiceStatus": "abc",
                    "RegistrationTime": 0,
                    "LastHeartbeatTime": 0,
                    "RegistrationId": "abc",
                    "HiddenStatus": "abc",
                    "MetaJson": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

