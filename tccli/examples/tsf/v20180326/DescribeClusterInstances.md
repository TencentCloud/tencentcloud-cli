**Example 1: 查询集群机器列表**



Input: 

```
tccli tsf DescribeClusterInstances --cli-unfold-argument  \
    --Limit 20 \
    --ClusterId cluster-xxxxxxx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a92e58d4-b415-4069-910e-c84e60233019",
        "Result": {
            "TotalCount": 2,
            "Content": [
                {
                    "InstanceId": "ins-6a79x94v",
                    "NodeInstanceId": "ins-6a79x94v",
                    "InstanceName": "consumer",
                    "LanIp": "172.16.0.7",
                    "WanIp": "193.112.32.241",
                    "NamespaceId": "namespace-6a79x94v",
                    "NamespaceName": "test-namespace",
                    "UpdateTime": null,
                    "InstanceDesc": null,
                    "ClusterId": null,
                    "ClusterName": null,
                    "InstanceStatus": null,
                    "InstanceAvailableStatus": "Abnormal",
                    "ServiceInstanceStatus": "Stopped",
                    "ServiceSidecarStatus": "UnSupported",
                    "OperationState": 6,
                    "CountInTsf": null,
                    "GroupId": "",
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
                    "InstancePkgVersion": "",
                    "ClusterType": null,
                    "InstanceZoneId": null,
                    "RestrictState": null,
                    "InstanceImportMode": "R",
                    "Reason": "R",
                    "ApplicationResourceType": "def",
                    "AgentVersion": "1.46.0",
                    "ApplicationType": null
                }
            ]
        }
    }
}
```

