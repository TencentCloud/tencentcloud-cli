**Example 1: 查询www.qq.com任务指标**



Input: 

```
tccli cat DescribeProbeMetricData --cli-unfold-argument  \
    --AnalyzeTaskType AnalyzeTaskType_Network \
    --MetricType gauge \
    --Field avg("query_time") \
    --GroupBy time(365d) \
    --Filters '"host" = 'www.qq.com''
```

Output: 
```
{
    "Response": {
        "MetricSet": "[{\"name\":\"netenv_request_gauge\",\"columns\":[\"time\",\"avg(query_time)\"],\"values\":[[1765987200,**.*************]],\"tags\":null}]",
        "RequestId": "144fa926-567c-4d91-9852-b1d226115adb"
    }
}
```

