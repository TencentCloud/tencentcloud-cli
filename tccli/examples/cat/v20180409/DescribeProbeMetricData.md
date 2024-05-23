**Example 1: 请求浏览数据**

请求浏览数据

Input: 

```
tccli cat DescribeProbeMetricData --cli-unfold-argument  \
    --AnalyzeTaskType AnalyzeTaskType_Network \
    --MetricType gauge \
    --Field sum("error_count") \
    --GroupBy time(30d), "operator" \
    --Filters '"host" = 'default-host'' 'time >= now()-1h'
```

Output: 
```
{
    "Response": {
        "MetricSet": "[{\"name\":\"netenv_request_gauge\",\"columns\":[\"time\",\"sum(error_count)\"],\"values\":[[xxxxx,xxxxx]],\"tags\":null}]",
        "RequestId": "xxxxx"
    }
}
```

