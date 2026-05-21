**Example 1: 获取 Prometheus Alertmanager 配置**



Input: 

```
tccli monitor DescribePrometheusAlertmanagerConfig --cli-unfold-argument  \
    --InstanceId prom-youguess
```

Output: 
```
{
    "Response": {
        "AlertmanagerConfig": {
            "InhibitRules": [
                {
                    "SourceMatchers": [
                        "severity=\"warning\""
                    ],
                    "TargetMatchers": [
                        "severity=\"critical\""
                    ],
                    "Equal": [
                        "alertname",
                        "cluster"
                    ]
                }
            ]
        },
        "RequestId": "b61cbm7l5toolongdqj3-586x"
    }
}
```

