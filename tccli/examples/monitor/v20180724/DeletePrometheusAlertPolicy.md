**Example 1: 删除Prometheus告警规则**

删除Prometheus告警规则

Input: 

```
tccli monitor DeletePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId abc \
    --AlertIds abc \
    --Names abc
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

