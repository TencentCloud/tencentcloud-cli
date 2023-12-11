**Example 1: 批量查询指标**

查询请求速率&请求总数

Input: 

```
tccli pts DescribeSampleBatchQuery --cli-unfold-argument  \
    --ProjectId project-btksohr0 \
    --JobId job-61ovraba \
    --ScenarioId scenario-j1u85ixm \
    --Queries.0.Metric pts_engine_req_total \
    --Queries.0.Aggregation Rate \
    --Queries.1.Metric pts_engine_req_total \
    --Queries.1.Aggregation Count
```

Output: 
```
{
    "Response": {
        "MetricSampleSet": [
            {
                "Metric": "pts_engine_req_total",
                "Aggregation": "Rate",
                "Unit": "reqs/s",
                "Labels": null,
                "Value": "30.34732915216155",
                "Timestamp": 1631694009709
            },
            {
                "Metric": "pts_engine_req_total",
                "Aggregation": "Count",
                "Unit": "reqs",
                "Labels": null,
                "Value": "1193277",
                "Timestamp": 1631694009709
            }
        ],
        "RequestId": "70805f6a-d7e1-4247-9d5a-fde3afe2b377"
    }
}
```

