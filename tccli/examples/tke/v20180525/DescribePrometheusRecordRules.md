**Example 1: 拉取聚合规则**



Input: 

```
tccli tke DescribePrometheusRecordRules --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Content": "xx",
                "UpdateTime": "xx",
                "ClusterId": "xx",
                "Name": "xx",
                "TemplateId": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

