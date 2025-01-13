**Example 1: 查询总请求数**

查询某个任务总的请求数

Input: 

```
tccli pts DescribeSampleQuery --cli-unfold-argument  \
    --ProjectId project-1a2b3c4d \
    --JobId job-1a2b3c4d \
    --ScenarioId scenario-1a2b3c4d \
    --Metric pts_engine_req_total \
    --Aggregation Count
```

Output: 
```
{
    "Response": {
        "MetricSample": {
            "Metric": "pts_engine_req_total",
            "Aggregation": "Count",
            "Unit": "reqs",
            "Labels": [
                {
                    "LabelName": "method",
                    "LabelValue": "GET"
                }
            ],
            "Value": "1100000",
            "Timestamp": 1631693000000
        },
        "RequestId": "abc-123-xyz"
    }
}
```

