**Example 1: 拉取聚合规则**

拉取聚合规则

Input: 

```
tccli monitor DescribePrometheusRecordRules --cli-unfold-argument  \
    --InstanceId xxx
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Content": "xdx",
                "UpdateTime": "xdx",
                "ClusterId": "xdx",
                "Name": "xdx",
                "TemplateId": "xdx",
                "Id": "de",
                "Status": 1,
                "Count": 1
            }
        ],
        "Total": 1,
        "RequestId": "xxx"
    }
}
```

