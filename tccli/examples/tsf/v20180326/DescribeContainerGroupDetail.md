**Example 1: DescribeContainerGroupDetail**



Input: 

```
tccli tsf DescribeContainerGroupDetail --cli-unfold-argument  \
    --GroupId group-xxxxxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "UpdatedTime": 0,
            "HealthCheckSettings": {
                "ReadinessProbe": {
                    "TimeoutSeconds": 1,
                    "InitialDelaySeconds": 1,
                    "ActionType": "xx",
                    "Command": [
                        "xx"
                    ],
                    "PeriodSeconds": 1,
                    "Path": "xx",
                    "SuccessThreshold": 1,
                    "Scheme": "xx",
                    "Port": 1,
                    "FailureThreshold": 1
                },
                "LivenessProbe": {
                    "TimeoutSeconds": 1,
                    "InitialDelaySeconds": 1,
                    "ActionType": "xx",
                    "Command": [
                        "xx"
                    ],
                    "PeriodSeconds": 1,
                    "Path": "xx",
                    "SuccessThreshold": 1,
                    "Scheme": "xx",
                    "Port": 1,
                    "FailureThreshold": 1
                }
            },
            "InstanceNum": 1,
            "NamespaceName": "xx",
            "MaxUnavailable": "xx",
            "ApplicationType": "xx",
            "CurrentNum": 1,
            "MicroserviceType": "xx",
            "Status": "xx",
            "LbIp": "xx",
            "MemRequest": "xx",
            "AccessType": 1,
            "UpdateIvl": 10,
            "Envs": [
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                },
                {
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "TagName": "xx",
            "ClusterIp": "xx",
            "MemLimit": "xx",
            "CpuLimit": "xx",
            "ApplicationId": "xx",
            "ApplicationName": "xx",
            "ProtocolPorts": [
                {
                    "TargetPort": 30032,
                    "Protocol": "xx",
                    "Port": 30032,
                    "NodePort": 0
                }
            ],
            "UpdateType": 1,
            "ClusterId": "xx",
            "MaxSurge": "xx",
            "Server": "xx",
            "SubnetId": "xx",
            "NodePort": 30870,
            "GroupId": "xx",
            "GroupResourceType": "xx",
            "InstanceCount": 1,
            "GroupName": "xx",
            "ClusterName": "xx",
            "CreateTime": "xx",
            "Reponame": "xx",
            "CpuRequest": "xx",
            "Message": "xx",
            "NamespaceId": "xx"
        },
        "RequestId": "xx"
    }
}
```

