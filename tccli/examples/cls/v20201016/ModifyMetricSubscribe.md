**Example 1: 修改指标订阅配置**

修改指标订阅配置

Input: 

```
tccli cls ModifyMetricSubscribe --cli-unfold-argument  \
    --TopicId 715094e3-01b0-4aeb-91f5-ee9f46a4a13c \
    --TaskId 5871c48d-219b-4274-829b-5aa7fb24229b \
    --Name metric_subscribe_name \
    --Namespace QCE/CVM \
    --Metrics.0.MetricName metric name \
    --Metrics.0.Periods 60 120 \
    --Metrics.0.MetricLabels.0.Key label_key \
    --Metrics.0.MetricLabels.0.Value label_value \
    --InstanceInfo.InstanceDimension bucket appid \
    --InstanceInfo.Instances.0.Values bucket_asdfa-asdf-asdf-ads 12325435 \
    --Enable 2
```

Output: 
```
{
    "Response": {
        "RequestId": "4a3c7ea9-02fa-4d33-b626-6cd496d0e300"
    }
}
```

