**Example 1: 获取应用弹性策略组合**

获取应用弹性策略组合

Input: 

```
tccli tem DescribeApplicationAutoscalerList --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId xx \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "MinReplicas": 0,
                "HorizontalAutoscaler": [
                    {
                        "MinReplicas": 0,
                        "Metrics": "xx",
                        "Threshold": 0,
                        "MaxReplicas": 0
                    }
                ],
                "MaxReplicas": 0,
                "CronHorizontalAutoscaler": [
                    {
                        "Priority": 0,
                        "Schedules": [
                            {
                                "StartAt": "xx",
                                "TargetReplicas": 0
                            }
                        ],
                        "Enabled": true,
                        "Period": "xx",
                        "Name": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

