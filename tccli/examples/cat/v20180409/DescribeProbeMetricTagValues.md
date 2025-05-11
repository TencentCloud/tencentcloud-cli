**Example 1: 请求域名数据**

请求域名数据


Input: 

```
tccli cat DescribeProbeMetricTagValues --cli-unfold-argument  \
    --AnalyzeTaskType AnalyzeTaskType_Network \
    --Key area \
    --Filter host = 'baidu.com' \
    --TimeRange now()-30d
```

Output: 
```
{
    "Response": {
        "TagValueSet": "{\"name\":\"netenv_request_gauge\",\"columns\":[\"key\",\"value\"],\"values\":[[\"area\",\"上海\"]],\"tags\":null}",
        "RequestId": "asd"
    }
}
```

