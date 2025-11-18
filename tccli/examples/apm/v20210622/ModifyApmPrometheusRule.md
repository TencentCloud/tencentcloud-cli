**Example 1: test**

修改apm业务系统与Prometheus实例的指标匹配规则

Input: 

```
tccli apm ModifyApmPrometheusRule --cli-unfold-argument  \
    --Id 2 \
    --Name MyRule \
    --Status 2 \
    --ServiceName profile-service \
    --MetricMatchType 0 \
    --MetricNameRule task.duration \
    --InstanceId apm-059oXBfTL
```

Output: 
```
{
    "Response": {
        "RequestId": "be4c9cea-5b0f-4b96-93d6-59c840a4c096"
    }
}
```

