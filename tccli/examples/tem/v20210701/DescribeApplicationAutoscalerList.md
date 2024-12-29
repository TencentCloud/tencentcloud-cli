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
                "AutoscalerId": "scaler-3j2o6ypg",
                "AutoscalerName": "elastic-test",
                "MinReplicas": 0,
                "MaxReplicas": 4,
                "CreateDate": "2024-12-05 11:10:19",
                "ModifyDate": "2024-12-20 17:00:23",
                "EnableDate": "2024-12-20 17:00:23",
                "Description": "这是一个描述",
                "Enabled": true,
                "HorizontalAutoscaler": [
                    {
                        "MinReplicas": 0,
                        "MaxReplicas": 4,
                        "Metrics": "CPU",
                        "Threshold": 0,
                        "DoubleThreshold": 60,
                        "Enabled": true
                    }
                ],
                "CronHorizontalAutoscaler": []
            },
            {
                "AutoscalerId": "scaler-b5q33njo",
                "AutoscalerName": "pk-test-clb",
                "MinReplicas": 0,
                "MaxReplicas": 4,
                "CreateDate": "2024-10-25 16:36:10",
                "ModifyDate": "2024-11-29 10:35:52",
                "EnableDate": "2024-11-29 10:35:52",
                "Description": "这是一个描述",
                "Enabled": false,
                "HorizontalAutoscaler": [
                    {
                        "MinReplicas": 0,
                        "MaxReplicas": 4,
                        "Metrics": "CPU",
                        "Threshold": 0,
                        "DoubleThreshold": 50,
                        "Enabled": true
                    }
                ],
                "CronHorizontalAutoscaler": [
                    {
                        "Name": "pk-test",
                        "Period": "* * *",
                        "Schedules": [
                            {
                                "StartAt": "02:00",
                                "TargetReplicas": 1
                            }
                        ],
                        "Enabled": false,
                        "Priority": 0
                    }
                ]
            },
            {
                "AutoscalerId": "scaler-ojr3nlj9",
                "AutoscalerName": "pk-test-1",
                "MinReplicas": 1,
                "MaxReplicas": 3,
                "CreateDate": "2024-12-19 23:38:45",
                "ModifyDate": "2024-12-19 23:38:45",
                "EnableDate": null,
                "Description": "",
                "Enabled": false,
                "HorizontalAutoscaler": [
                    {
                        "MinReplicas": 1,
                        "MaxReplicas": 3,
                        "Metrics": "CPU",
                        "Threshold": 0,
                        "DoubleThreshold": 50,
                        "Enabled": true
                    }
                ],
                "CronHorizontalAutoscaler": [
                    {
                        "Name": "policy-test",
                        "Period": "* * *",
                        "Schedules": [
                            {
                                "StartAt": "00:00",
                                "TargetReplicas": 1
                            }
                        ],
                        "Enabled": true,
                        "Priority": 0
                    }
                ]
            }
        ],
        "RequestId": "c1d58f12-420f-464c-ac3e-f4f6a77284b0"
    }
}
```

