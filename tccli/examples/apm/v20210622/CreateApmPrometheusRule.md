**Example 1: test**

创建apm业务系统与Prometheus实例的指标匹配规则

Input: 

```
tccli apm CreateApmPrometheusRule --cli-unfold-argument  \
    --Name MyRuleTest \
    --ServiceName java-market-service \
    --MetricMatchType 1 \
    --MetricNameRule task.duration \
    --InstanceId apm-059oXBfTL
```

Output: 
```
{
    "Response": {
        "RequestId": "72159d4a-265c-43e8-b653-c62358f1e17b"
    }
}
```

