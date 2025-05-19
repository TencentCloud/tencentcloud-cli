**Example 1: 删除Prometheus告警规则**



Input: 

```
tccli tke DeletePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId abc \
    --AlertIds abc \
    --Names abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

