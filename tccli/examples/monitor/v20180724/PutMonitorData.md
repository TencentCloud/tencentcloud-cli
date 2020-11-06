**Example 1: 客户端上报指标**



Input: 

```
tccli monitor PutMonitorData --cli-unfold-argument  \
    --Version 2018-07-24 \
    --AnnounceIp 10.0.0.1 \
    --AnnounceTimestamp 1569379988 \
    --Metrics.0.MetricName name1 \
    --Metrics.0.Value value1 \
    --Metrics.1.MetricName name2 \
    --Metrics.1.Value value2
```

Output: 
```
{
    "Response": {
        "RequestId": "7cc6ae87-2aae-4394-8ccb-29777f5aeadx"
    }
}
```

