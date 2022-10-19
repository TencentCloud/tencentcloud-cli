**Example 1: 批量查询指标**

查询请求速率&请求总数

Input: 

```
tccli pts DescribeSampleBatchQuery --cli-unfold-argument  \
    --ProjectId xx \
    --JobId 123 \
    --ScenarioId 123 \
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
        "RequestId": "xx"
    }
}
```

