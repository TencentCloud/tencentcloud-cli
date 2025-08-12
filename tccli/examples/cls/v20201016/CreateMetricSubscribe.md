**Example 1: 创建指标订阅配置**

创建指标订阅配置

Input: 

```
tccli cls CreateMetricSubscribe --cli-unfold-argument  \
    --Name metric_subscribe_name \
    --TopicId 715094e3-01b0-4aeb-91f5-ee9f46a4a13c \
    --Namespace QCE/CVM \
    --Metrics.0.MetricName metric name \
    --Metrics.0.Periods 60 120 \
    --Metrics.0.MetricLabels.0.Key label_key \
    --Metrics.0.MetricLabels.0.Value label_value \
    --InstanceInfo.InstanceDimension bucket appid \
    --InstanceInfo.Instances.0.Values bucket_asdfa-asdf-asdf-ads 12325435
```

Output: 
```
{
    "Response": {
        "TaskId": "c03bf755-0482-4903-a210-2a318cde922e",
        "RequestId": "4a3c7ea9-02fa-4d33-b626-6cd496d0e300"
    }
}
```

