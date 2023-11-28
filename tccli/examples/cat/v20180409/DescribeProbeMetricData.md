**Example 1: 请求浏览数据**

请求浏览数据

Input: 

```
tccli cat DescribeProbeMetricData --cli-unfold-argument  \
    --AnalyzeTaskType AnalyzeTaskType_Browse \
    --MetricType gauge \
    --Field avg("count") \
    --GroupBy time(30d), "operator" \
    --Filters '"host" = 'default-host'' 'time >= now()-3h'
```

Output: 
```
{
    "Response": {
        "MetricSet": "abc",
        "RequestId": "abc"
    }
}
```

