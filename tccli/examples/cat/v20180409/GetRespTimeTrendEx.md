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
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            },
            {
                "MetricName": "Avg_Avg"
            }
        ],
        "RequestId": "af4205fa-de57-48af-a6ce-0c4b5593d1cb"
    }
}
```

