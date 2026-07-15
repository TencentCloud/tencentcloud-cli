**Example 1: 获取指定类型的API安全相关规则**

获取指定类型的API安全相关规则

Input: 

```
tccli waf DescribeApiSecSensitiveRuleList --cli-unfold-argument  \
    --Domain xxx.testwaf.com \
    --IsQueryApiExtractRule True
```

Output: 
```
{
    "Response": {
        "ApiExcludeRule": null,
        "ApiExtractRule": null,
        "ApiSecCustomEventRule": null,
        "ApiSecPrivilegeRule": null,
        "ApiSecSceneRule": null,
        "Data": null,
        "RuleNameList": null,
        "Status": 1,
        "Total": 0,
        "RequestId": "56b9948c-9b1d-4839-9e21-857a266db0d9"
    }
}
```

