**Example 1: 查询指标矩阵**



Input: 

```
tccli pts DescribeSampleMatrixQuery --cli-unfold-argument  \
    --ProjectId project-btksohr0 \
    --JobId job-61ovraba \
    --ScenarioId scenario-j1u85ixm \
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
        "RequestId": "70805f6a-d7e1-4247-9d5a-fde3afe2b377"
    }
}
```

