**Example 1: 部署组列表**



Input: 

```
tccli tsf DescribeContainerGroupAttribute --cli-unfold-argument  \
    --GroupId group-gvkwqkjv
```

Output: 
```
{
    "Response": {
        "Result": {
            "InstanceNum": 0,
            "CurrentNum": 0,
            "LbDns": "abc",
            "LbIp": "abc",
            "ClusterIp": "abc",
            "Status": "abc",
            "Message": "abc",
            "Envs": [
                {
                    "Name": "abc",
                    "Value": "abc",
                    "ValueFrom": {
                        "FieldRef": {
                            "FieldPath": "abc"
                        },
                        "ResourceFieldRef": {
                            "Resource": "abc"
                        }
                    }
                }
            ],
            "NodePort": 1,
            "SubnetId": "abc",
            "HealthCheckSettings": {
                "LivenessProbe": {
                    "ActionType": "abc",
                    "InitialDelaySeconds": 1,
                    "TimeoutSeconds": 1,
                    "PeriodSeconds": 1,
                    "SuccessThreshold": 1,
                    "FailureThreshold": 1,
                    "Scheme": "abc",
                    "Port": 1,
                    "Path": "abc",
                    "Command": [
                        "abc"
                    ],
                    "Type": "abc"
                },
                "ReadinessProbe": {
                    "ActionType": "abc",
                    "InitialDelaySeconds": 1,
                    "TimeoutSeconds": 1,
                    "PeriodSeconds": 1,
                    "SuccessThreshold": 1,
                    "FailureThreshold": 1,
                    "Scheme": "abc",
                    "Port": 1,
                    "Path": "abc",
                    "Command": [
                        "abc"
                    ],
                    "Type": "abc"
                }
            },
            "IsNotEqualServiceConfig": true
        },
        "RequestId": "abc"
    }
}
```

