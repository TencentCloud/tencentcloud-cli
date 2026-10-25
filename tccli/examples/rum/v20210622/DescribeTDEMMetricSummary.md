**Example 1: 查询分析指标合计**



Input: 

```
tccli rum DescribeTDEMMetricSummary --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1790050740000 \
    --EndTime 1790054340000 \
    --EventType api_call \
    --Filters [{"Key":"environment","Op":"in","Values":["production"]}] \
    --Metrics avg \
    --MeasurementKey duration
```

Output: 
```
{
    "Response": {
        "Metrics": [
            {
                "Name": "Avg",
                "Value": 0
            }
        ],
        "RequestId": "37858f63-fa66-42f2-86af-52a83f742841"
    }
}
```

