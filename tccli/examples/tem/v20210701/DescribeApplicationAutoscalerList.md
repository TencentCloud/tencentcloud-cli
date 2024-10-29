**Example 1: 获取应用弹性策略组合**

获取应用弹性策略组合

Input: 

```
tccli tem DescribeApplicationAutoscalerList --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "MinReplicas": 0,
                "MaxReplicas": 0,
                "HorizontalAutoscaler": [
                    {
                        "MinReplicas": 0,
                        "MaxReplicas": 0,
                        "Metrics": "abc",
                        "Threshold": 0,
                        "Enabled": true,
                        "DoubleThreshold": 0
                    }
                ],
                "CronHorizontalAutoscaler": [
                    {
                        "Name": "abc",
                        "Period": "abc",
                        "Schedules": [
                            {
                                "StartAt": "abc",
                                "TargetReplicas": 0
                            }
                        ],
                        "Enabled": true,
                        "Priority": 0
                    }
                ],
                "AutoscalerId": "abc",
                "AutoscalerName": "abc",
                "Description": "abc",
                "CreateDate": "abc",
                "ModifyDate": "abc",
                "EnableDate": "abc",
                "Enabled": true
            }
        ],
        "RequestId": "abc"
    }
}
```

