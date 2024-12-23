**Example 1: 查询虚拟机部署组云主机列表**

查询虚拟机部署组云主机列表

Input: 

```
tccli tsf DescribeGroupInstances --cli-unfold-argument  \
    --GroupId group-v6743bka
```

Output: 
```
{
    "Response": {
        "RequestId": "57578845-90a3-4f98-b166-a1822f3a7223",
        "Result": {
            "Content": [
                {
                    "AgentVersion": "1.44.0",
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "ApplicationResourceType": null,
                    "ApplicationType": null,
                    "ClusterId": "cluster-y4rb3qja",
                    "ClusterName": null,
                    "ClusterType": null,
                    "CountInTsf": null,
                    "GroupId": "group-v6743bka",
                    "GroupName": null,
                    "InstanceAvailableStatus": "Running",
                    "InstanceChargeType": null,
                    "InstanceCreatedTime": null,
                    "InstanceDesc": null,
                    "InstanceExpiredTime": null,
                    "InstanceId": "ins-660yl495",
                    "InstanceImportMode": "M",
                    "InstanceLimitCpu": null,
                    "InstanceLimitMem": null,
                    "InstanceName": "pepyzhang-Mesh升级测试1-勿删",
                    "InstancePkgVersion": "20210826163718",
                    "InstanceStatus": "Running",
                    "InstanceTotalCpu": null,
                    "InstanceTotalMem": null,
                    "InstanceUsedCpu": null,
                    "InstanceUsedMem": null,
                    "InstanceZoneId": null,
                    "LanIp": "10.0.1.16",
                    "NamespaceId": null,
                    "NamespaceName": null,
                    "NodeInstanceId": null,
                    "OperationState": 0,
                    "Reason": "请启用健康检查，以便更精确地反映应用运行状态",
                    "RestrictState": null,
                    "ServiceInstanceStatus": "Running",
                    "ServiceSidecarStatus": "Running",
                    "UpdateTime": null,
                    "WanIp": "121.4.178.105"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

