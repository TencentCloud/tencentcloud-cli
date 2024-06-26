**Example 1: 拉取聚合规则**



Input: 

```
tccli tke DescribePrometheusRecordRules --cli-unfold-argument  \
    --InstanceId abc \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Name": "abc",
                "UpdateTime": "abc",
                "TemplateId": "abc",
                "Content": "abc",
                "ClusterId": "abc"
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

