**Example 1: DescribeSampleMatrixBatchQuery**



Input: 

```
tccli pts DescribeSampleMatrixBatchQuery --cli-unfold-argument  \
    --JobId job-6pmj0oae \
    --ScenarioId scenario-oienak6y \
    --Queries.0.Metric pts_engine_req_duration_seconds \
    --Queries.0.Aggregation P50 \
    --ProjectId project-m51m6h0a
```

Output: 
```
{
    "Response": {
        "MetricSampleMatrixSet": [
            {
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
                                "Timestamp": 1650517344000,
                                "Value": 0.025
                            },
                            {
                                "Timestamp": 1650518490000,
                                "Value": 0.05
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

