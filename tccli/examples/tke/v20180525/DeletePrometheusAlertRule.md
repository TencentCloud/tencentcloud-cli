**Example 1: 删除Prometheus告警规则**



Input: 

```
tccli tke DeletePrometheusAlertRule --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --AlertIds a1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

