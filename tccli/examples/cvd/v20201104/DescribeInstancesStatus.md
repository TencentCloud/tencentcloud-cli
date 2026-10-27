**Example 1: DescribeInstancesStatus**



Input: 

```
tccli cvd DescribeInstancesStatus --cli-unfold-argument  \
    --InstanceIds cdi-yrsgnf7sza3b0n3
```

Output: 
```
{
    "Response": {
        "InstanceStatusList": [
            {
                "IdleSeconds": 0,
                "InstanceId": "cdi-yrsgnf7sza3b0n3",
                "LatestOperation": "BindInstances",
                "LatestOperationState": "SUCCESS",
                "SessionState": 2,
                "Status": "RUNNING",
                "StatusChangeTime": 1791970839
            }
        ],
        "RequestId": "fc9bfb93-de2b-4bcf-a7e0-161bdf2be43e"
    }
}
```

