**Example 1: DescribeContainerGroupDeployInfo**



Input: 

```
tccli tsf DescribeContainerGroupDeployInfo --cli-unfold-argument  \
    --GroupId group-gyqpkzda
```

Output: 
```
{
    "Response": {
        "Result": {
            "HealthCheckSettings": {
                "ReadinessProbe": {
                    "TimeoutSeconds": 1,
                    "InitialDelaySeconds": 1,
                    "PeriodSeconds": 1,
                    "ActionType": "xx",
                    "Path": "xx",
                    "Command": [
                        "xx"
                    ],
                    "SuccessThreshold": 1,
                    "Scheme": "xx",
                    "Type": "xx",
                    "Port": 1,
                    "FailureThreshold": 1
                },
                "LivenessProbe": {
                    "TimeoutSeconds": 1,
                    "InitialDelaySeconds": 1,
                    "PeriodSeconds": 1,
                    "ActionType": "xx",
                    "Path": "xx",
                    "Command": [
                        "xx"
                    ],
                    "SuccessThreshold": 1,
                    "Scheme": "xx",
                    "Type": "xx",
                    "Port": 1,
                    "FailureThreshold": 1
                }
            },
            "InstanceNum": 1,
            "AgentMemLimit": "xx",
            "HeadlessService": true,
            "CurrentNum": 0,
            "MemRequest": "xx",
            "IstioCpuRequest": "xx",
            "AccessType": 2,
            "UpdateIvl": 10,
            "JvmOpts": "xx",
            "IstioCpuLimit": "xx",
            "SubnetId": "xx",
            "AgentCpuRequest": "xx",
            "MemLimit": "xx",
            "CpuLimit": "xx",
            "Envs": [
                {
                    "ValueFrom": {
                        "FieldRef": {
                            "FieldPath": "xx"
                        },
                        "ResourceFieldRef": {
                            "Resource": "xx"
                        }
                    },
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "ProtocolPorts": [
                {
                    "TargetPort": 30032,
                    "Protocol": "xx",
                    "Port": 30032,
                    "NodePort": 0
                }
            ],
            "AgentMemRequest": "xx",
            "IstioMemLimit": "xx",
            "UpdateType": 1,
            "Server": "xx",
            "GroupName": "xx",
            "TcrRepoInfo": {
                "RegistryName": "xx",
                "Namespace": "xx",
                "Region": "xx",
                "RegistryId": "xx",
                "RepoName": "xx"
            },
            "DisableService": true,
            "IstioMemRequest": "xx",
            "Alias": "xx",
            "DeployAgent": true,
            "AgentCpuLimit": "xx",
            "Reponame": "xx",
            "CpuRequest": "xx",
            "GroupId": "xx",
            "TagName": "xx"
        },
        "RequestId": "xx"
    }
}
```

