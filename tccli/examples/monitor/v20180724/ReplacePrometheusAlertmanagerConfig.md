**Example 1: 更新 Prometheus Alertmanager 配置**



Input: 

```
tccli monitor ReplacePrometheusAlertmanagerConfig --cli-unfold-argument  \
    --InstanceId prom-youguess \
    --AlertmanagerConfig.InhibitRules.0.SourceMatchers severity=warning \
    --AlertmanagerConfig.InhibitRules.0.TargetMatchers severity=critical \
    --AlertmanagerConfig.InhibitRules.0.Equal alertname cluster
```

Output: 
```
{
    "Response": {
        "RequestId": "vbamvs77dsolongkskc9ruhuji"
    }
}
```

