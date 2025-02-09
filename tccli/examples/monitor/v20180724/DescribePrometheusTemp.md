**Example 1: 拉取模板列表**

拉取模板列表

Input: 

```
tccli monitor DescribePrometheusTemp --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Name ID \
    --Filters.0.Values alert-test \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "Name": "template",
                "Describe": "template",
                "Level": "instance",
                "RecordRules": [],
                "RawJobs": [],
                "ServiceMonitors": [],
                "PodMonitors": [
                    {
                        "Name": "test-pm",
                        "Config": "apiVersion: monitoring.coreos.com/v1\nkind: PodMonitor\nmetadata:\n  name: example-app\n  labels:\n    team: frontend\nspec:\n  selector:\n    matchLabels:\n      app: example-app\n  podMetricsEndpoints:\n  - port: web",
                        "TemplateId": "temp-asdj",
                        "Targets": {
                            "Total": 1,
                            "Up": 1,
                            "Down": 1,
                            "Unknown": 1
                        }
                    }
                ],
                "TemplateId": "temp-asdj",
                "UpdateTime": "2024-07-16T08:28:54Z",
                "Version": "v1",
                "IsDefault": true,
                "AlertDetailRules": [],
                "TargetsTotal": 0
            }
        ],
        "Total": 1,
        "RequestId": "skdh-afbri"
    }
}
```

