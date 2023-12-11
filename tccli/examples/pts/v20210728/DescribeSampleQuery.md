**Example 1: 查询总请求数**

查询某个任务总的请求数

Input: 

```
tccli pts DescribeSampleQuery --cli-unfold-argument  \
    --ProjectId project-xx \
    --JobId 123 \
    --ScenarioId 123 \
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
            "Value": "1159362",
            "Timestamp": 1631693039208
        },
        "RequestId": "70805f6a-d7e1-4247-9d5a-fde3afe2b377"
    }
}
```

