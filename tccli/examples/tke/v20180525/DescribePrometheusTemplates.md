**Example 1: 拉取模板列表**



Input: 

```
tccli tke DescribePrometheusTemplates --cli-unfold-argument  \
    --Filters.0.Name Type \
    --Filters.0.Values ServiceMonitor
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "UpdateTime": "xx",
                "RecordRules": [
                    {
                        "Config": "xx",
                        "Name": "xx"
                    }
                ],
                "Version": "xx",
                "Name": "xx",
                "Level": "xx",
                "Describe": "xx",
                "RawJobs": [
                    {
                        "Config": "xx",
                        "Name": "xx"
                    }
                ],
                "AlertRules": [
                    {
                        "Template": "xx",
                        "Labels": [
                            {
                                "Name": "xx",
                                "Value": "xx"
                            }
                        ],
                        "For": "xx",
                        "Rule": "xx",
                        "Name": "xx"
                    }
                ],
                "PodMonitors": [
                    {
                        "Config": "xx",
                        "Name": "xx"
                    }
                ],
                "TemplateId": "xx",
                "IsDefault": true,
                "ServiceMonitors": [
                    {
                        "Config": "xx",
                        "Name": "xx"
                    }
                ]
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

