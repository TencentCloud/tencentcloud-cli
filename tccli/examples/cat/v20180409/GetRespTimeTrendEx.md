**Example 1: 查询拨测任务的走势数据示例**



Input: 

```
tccli cat GetRespTimeTrendEx --cli-unfold-argument  \
    --TaskId 226791 \
    --Period 1 \
    --Date 22019-12-12 \
    --MetricName availRatio \
    --Dimensions.Province Avg \
    --Dimensions.Isp Avg
```

Output: 
```
{
    "Response": {
        "DataPoints": [
            {
                "LogTime": "2019-12-12 00:00:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            },
            {
                "LogTime": "2019-12-12 00:01:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            },
            {
                "LogTime": "2019-12-12 00:02:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            },
            {
                "LogTime": "2019-12-12 00:03:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            },
            {
                "LogTime": "2019-12-12 00:04:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            },
            {
                "LogTime": "2019-12-12 00:05:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            },
            {
                "LogTime": "2019-12-12 00:06:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 0.9459
            },
            {
                "LogTime": "2019-12-12 00:07:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 0.9714
            },
            {
                "LogTime": "2019-12-12 23:58:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            },
            {
                "LogTime": "2019-12-12 23:59:00",
                "MetricName": "Avg_Avg",
                "MetricValue": 1
            }
        ],
        "RequestId": "af4205fa-de57-48af-a6ce-0c4b5593d1cb"
    }
}
```

