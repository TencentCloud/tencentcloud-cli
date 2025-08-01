**Example 1: 创建 JavaScript 注入规则**

创建一个 JavaScript 注入规则。

Input: 

```
tccli teo CreateSecurityJSInjectionRule --cli-unfold-argument  \
    --ZoneId zone-123123322 \
    --JSInjectionRules.0.Name test \
    --JSInjectionRules.0.Condition ${http.request.host} in ['www.test.com'] and ${http.request.uri.path} in ['/atteffa/geo-info'] \
    --JSInjectionRules.0.InjectJS inject-sdk-only \
    --JSInjectionRules.0.Priority 2
```

Output: 
```
{
    "Response": {
        "JSInjectionRuleIds": [
            "injection-2184008405"
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

