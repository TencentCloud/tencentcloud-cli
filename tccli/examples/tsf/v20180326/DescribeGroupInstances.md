**Example 1: 查询虚拟机部署组云主机列表**



Input: 

```
tccli tsf DescribeGroupInstances --cli-unfold-argument  \
    --GroupId group-xxxxxxx \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "26528f55-0b7e-4f9c-a122-974fbccd2ab3",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "InstanceId": "ins-xxxxxxx",
                    "InstanceName": "test",
                    "LanIp": "10.3.0.9",
                    "WanIp": "",
                    "NamespaceId": "cluster-xxxxxxx",
                    "UpdateTime": null,
                    "InstanceDesc": null,
                    "ClusterId": null,
                    "ClusterName": null,
                    "InstanceStatus": "Running",
                    "InstanceAvailableStatus": "Running",
                    "ServiceInstanceStatus": "Running",
                    "ServiceSidecarStatus": "UnSupported",
                    "OperationState": 0,
                    "CountInTsf": null,
                    "GroupId": "group-ov6wl65y",
                    "GroupName": null,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "InstanceCreatedTime": null,
                    "InstanceExpiredTime": null,
                    "InstanceChargeType": null,
                    "InstanceTotalCpu": null,
                    "InstanceTotalMem": null,
                    "InstanceUsedCpu": null,
                    "InstanceUsedMem": null,
                    "InstanceLimitCpu": null,
                    "InstanceLimitMem": null,
                    "InstancePkgVersion": "20190527183200",
                    "ClusterType": null,
                    "InstanceZoneId": null,
                    "RestrictState": null,
                    "InstanceImportMode": "R",
                    "ApplicationType": null
                }
            ]
        }
    }
}
```

