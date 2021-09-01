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
                    "Status": "xx",
                    "ReadyCount": 2,
                    "RestartCount": 0,
                    "ServiceInstanceStatus": "xx",
                    "PodId": "xx",
                    "Ip": "xx",
                    "Reason": "xx",
                    "InstanceAvailableStatus": "xx",
                    "PodName": "xx",
                    "InstanceStatus": "xx",
                    "NodeIp": "xx",
                    "Runtime": "xx",
                    "NodeInstanceId": "xx",
                    "CreatedAt": "xx"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "xx"
    }
}
```

