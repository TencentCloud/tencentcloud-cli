**Example 1: 批量预测任务实例列表**



Input: 

```
tccli tione DescribeBatchTaskInstances --cli-unfold-argument  \
    --BatchTaskId batch-78ugzrxxxx
```

Output: 
```
{
    "Response": {
        "BatchInstances": [
            {
                "BatchTaskInstanceId": "batch-78ugzrxxxx",
                "Status": "running",
                "StartTime": "2006-01-02 15:04:05",
                "EndTime": "2006-01-02 15:14:05",
                "RuntimeInSeconds": 600
            }
        ],
        "RequestId": "abc-123456"
    }
}
```

