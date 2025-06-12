**Example 1: 获取部署组其他属性**



Input: 

```
tccli tsf DescribeGroupAttribute --cli-unfold-argument  \
    --GroupId group-byxke4al
```

Output: 
```
{
    "Response": {
        "RequestId": "0bd33701-90d0-413f-9ae9-3a89df2fa6ad",
        "Result": {
            "InstanceCount": 1,
            "GroupId": "group-byxke4al",
            "PackageId": "pkg-278c1954",
            "PackageVersion": "1.12.0_E",
            "PackageName": "consumer-demo-1.12.0-Edgware-SNAPSHOT.jar",
            "RunInstanceCount": 0,
            "GroupStatus": "Updating",
            "OffInstanceCount": 1,
            "HealthCheckSettings": {
                "ReadinessProbe": {
                    "InitialDelaySeconds": 10,
                    "PeriodSeconds": 10,
                    "Port": 8000,
                    "ActionType": "tcp",
                    "SuccessThreshold": 3,
                    "Type": "TCP",
                    "TimeoutSeconds": 3,
                    "FailureThreshold": 3
                },
                "LivenessProbe": {
                    "ActionType": "tcp",
                    "InitialDelaySeconds": 180,
                    "TimeoutSeconds": 1,
                    "PeriodSeconds": 1,
                    "SuccessThreshold": 1,
                    "FailureThreshold": 1,
                    "Scheme": "http",
                    "Port": 1,
                    "Path": "/health",
                    "Command": [
                        "sh health.sh"
                    ],
                    "Type": "TCP"
                }
            },
            "IsNotEqualServiceConfig": false
        }
    }
}
```

