**Example 1: 获取运行时资源监控详情**

获取运行时资源监控详情

Input: 

```
tccli eis GetRuntimeResourceMonitorMetricMC --cli-unfold-argument  \
    --RuntimeId 12 \
    --StartTime 1619656971 \
    --EndTime 1619656971 \
    --Interval 300 \
    --MetricType 2 \
    --RateType False
```

Output: 
```
{
    "Response": {
        "MetricType": "abc",
        "Values": [
            {
                "Time": 0,
                "Val": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

