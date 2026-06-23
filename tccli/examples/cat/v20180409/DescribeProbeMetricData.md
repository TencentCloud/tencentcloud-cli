**Example 1: DescribeProbeMetricData接口调用示例**



Input: 

```
tccli cat DescribeProbeMetricData --cli-unfold-argument  \
    --AnalyzeTaskType AnalyzeTaskType_Transport \
    --MetricType gauge \
    --Field sum("error_count") \
    --Filter None \
    --GroupBy time(60m) \
    --Filters '"host" = 'https://www.test.com'' 'time >= now()-1h'
```

Output: 
```
{
    "Response": {
        "MetricSet": "[{\"name\":\"port_request_gauge\",\"columns\":[\"time\",\"sum(error_count)\"],\"values\":[[1781679600,0],[1781683200,null]],\"tags\":null}]",
        "RequestId": "xxxxx-xxxxx-xxxxx"
    }
}
```

