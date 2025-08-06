**Example 1: 查询 JavaScript 注入规则**

分页查询站点下 JavaScript 注入规则。

Input: 

```
tccli teo DescribeSecurityJSInjectionRule --cli-unfold-argument  \
    --ZoneId zone-123123232 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "JSInjectionRules": [
            {
                "RuleId": "injection-123219329",
                "Name": "test",
                "Condition": "${http.request.host} in ['www.test.com'] and ${http.request.uri.path} in ['/atteffa/geo-info']",
                "InjectJS": "inject-sdk-only",
                "Priority": 2
            }
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

