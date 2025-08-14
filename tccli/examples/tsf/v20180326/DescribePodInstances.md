**Example 1: DescribePodInstances**



Input: 

```
tccli tsf DescribePodInstances --cli-unfold-argument  \
    --GroupId group-6a73w4v5 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "Status": "Running",
                    "ReadyCount": 2,
                    "RestartCount": 0,
                    "ServiceInstanceStatus": "Running",
                    "PodId": "pod-sss",
                    "Ip": "10.0.1.1",
                    "Reason": "failed",
                    "InstanceAvailableStatus": "Running",
                    "PodName": "pod-sss",
                    "InstanceStatus": "Running",
                    "NodeIp": "10.0.1.0",
                    "Runtime": "runtime",
                    "NodeInstanceId": "id",
                    "CreatedAt": "time"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "6d7e580e-4b1c-49a7-8ffd-21551f865643"
    }
}
```

