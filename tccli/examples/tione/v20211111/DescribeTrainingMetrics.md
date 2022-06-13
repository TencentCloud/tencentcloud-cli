**Example 1: 查询训练自定义指标**



Input: 

```
tccli tione DescribeTrainingMetrics --cli-unfold-argument  \
    --TaskId taskid-xyz
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Metrics": [
                    {
                        "Points": [
                            {
                                "XValue": 1641002400.0,
                                "YValue": 0.0
                            },
                            {
                                "XValue": 1641002460.0,
                                "YValue": 0.0
                            }
                        ],
                        "XType": "Timestamp"
                    }
                ],
                "MetricName": "loss"
            }
        ],
        "RequestId": "1yzfdfa32",
        "TaskId": "taskid-xyz"
    }
}
```

