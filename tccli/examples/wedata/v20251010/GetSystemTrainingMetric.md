**Example 1: 查询训练系统监控指标数据**

查询训练系统监控指标数据

Input: 

```
tccli wedata GetSystemTrainingMetric --cli-unfold-argument  \
    --WorkspaceId 10086 \
    --RunId 5ba6863c72fd4abda3bd5a67027649f6 \
    --MetricName accuracy
```

Output: 
```
{
    "Response": {
        "Data": {
            "DataPoints": [
                {
                    "InstanceIdOrGpuId": "",
                    "Timestamps": [],
                    "Values": []
                }
            ],
            "EndTime": "",
            "MetricName": "accuracy",
            "Period": "0",
            "StartTime": ""
        },
        "RequestId": "a0249e22-2e17-4564-ad46-24abf0dd7de7"
    }
}
```

