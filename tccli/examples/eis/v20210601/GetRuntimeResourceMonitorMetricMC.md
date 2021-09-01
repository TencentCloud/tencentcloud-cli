**Example 1: 获取运行时资源监控详情**



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
        "Values": [
            {
                "Time": 1619656971,
                "Val": 10.3
            },
            {
                "Time": 1619656972,
                "Val": 10.9
            }
        ],
        "RequestId": "xx",
        "MetricType": "K8sWorkloadNetworkReceiveBytesBw"
    }
}
```

