**Example 1: 查询指标矩阵**



Input: 

```
tccli pts DescribeSampleMatrixQuery --cli-unfold-argument  \
    --ProjectId project-xx \
    --JobId 123 \
    --ScenarioId 123 \
    --Metric pts_engine_req_duration_seconds \
    --Aggregation P50
```

Output: 
```
{
    "Response": {
        "MetricSampleMatrix": {
            "Metric": "pts_engine_req_duration_seconds",
            "Aggregation": "P50",
            "Unit": "s",
            "Streams": [
                {
                    "Name": "响应时间P50",
                    "Labels": null,
                    "Values": [
                        {
                            "Timestamp": 1650517296000,
                            "Value": 0.032142349260523326
                        },
                        {
                            "Timestamp": 1650517299000,
                            "Value": 0.03377059214626565
                        },
                        {
                            "Timestamp": 1650517302000,
                            "Value": 0.03206904981580744
                        },
                        {
                            "Timestamp": 1650518490000,
                            "Value": 0.05
                        }
                    ]
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

