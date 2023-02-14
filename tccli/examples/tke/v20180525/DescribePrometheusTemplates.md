**Example 1: 拉取模板列表**

拉取模板列表

Input: 

```
tccli tke DescribePrometheusTemplates --cli-unfold-argument  \
    --Filters.0.Name Level \
    --Filters.0.Values ' instance'
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "UpdateTime": "2022-08-11T06:27:47Z",
                "RecordRules": [
                    {
                        "Config": "apiVersion: monitoring.coreos.com/v1\nkind: PrometheusRule\nmetadata:\n  name: example-record\nspec:\n  groups:\n    - name: test-limit\n      rules:\n        - expr: sum(metrics_test)\n          labels:\n            verb: read\n          record: 'apiserver_request:burnrate1d'\n        - expr: sum(metrics_test)\n          labels:\n            verb: read\n          record: 'apiserver_request:burnrate1d'\n",
                        "Name": "test"
                    }
                ],
                "Version": "v3",
                "Name": "test",
                "Level": "instance",
                "Describe": "测试",
                "TemplateId": "temp-dsfjgg",
                "IsDefault": true
            }
        ],
        "Total": 1,
        "RequestId": "a103e3cc-d0a9-4ff4-9e3b-dsjkalfdjlaf"
    }
}
```

