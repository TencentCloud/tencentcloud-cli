**Example 1: 查询分析指标趋势**



Input: 

```
tccli rum DescribeTDEMMetricTrend --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1790050740000 \
    --EndTime 1790054340000 \
    --Granularity 1h \
    --EventType crash \
    --Filters [{"Key":"environment","Op":"in","Values":["production"]}] \
    --Metrics count
```

Output: 
```
{
    "Response": {
        "Granularity": "1h",
        "RequestId": "26594b06-cbdb-4844-9b38-d70ae8b88f19"
    }
}
```

