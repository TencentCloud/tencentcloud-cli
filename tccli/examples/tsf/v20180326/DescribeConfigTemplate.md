**Example 1: 导入配置模板**



Input: 

```
tccli tsf DescribeConfigTemplate --cli-unfold-argument  \
    --ConfigTemplateId abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "ConfigTemplateId": "abc",
            "ConfigTemplateName": "abc",
            "ConfigTemplateDesc": "abc",
            "ConfigTemplateType": "abc",
            "ConfigTemplateValue": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc"
        },
        "RequestId": "abc"
    }
}
```

