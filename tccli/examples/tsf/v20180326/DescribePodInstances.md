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
        "RequestId": "4c78ccfd-c990-4182-bc53-2a9f417696cf",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "Reason": "",
                    "RestartCount": 0,
                    "Ip": "172.18.1.27",
                    "NodeIp": "10.2.12.141",
                    "Runtime": "7d 20h",
                    "InstanceStatus": null,
                    "CreatedAt": "2019-05-21 20:46:06",
                    "InstanceAvailableStatus": null,
                    "ServiceInstanceStatus": "Running",
                    "ReadyCount": 2,
                    "PodName": "prod-pay-center-a-2345103634-4x151",
                    "PodId": "6646495c-7bc6-11e9-b713-86e5a1f74de4",
                    "Status": "Running"
                }
            ]
        }
    }
}
```

