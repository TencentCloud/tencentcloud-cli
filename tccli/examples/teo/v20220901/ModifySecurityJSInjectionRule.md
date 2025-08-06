**Example 1: 修改 JavaScript 注入规则**

修改某个 JavaScript 注入规则。

Input: 

```
tccli teo ModifySecurityJSInjectionRule --cli-unfold-argument  \
    --ZoneId zone-123123322 \
    --JSInjectionRules.0.RuleId injection-123219329 \
    --JSInjectionRules.0.Name test \
    --JSInjectionRules.0.Condition ${http.request.host} in ['www.test.com'] and ${http.request.uri.path} in ['/atteffa/geo-info'] \
    --JSInjectionRules.0.InjectJS inject-sdk-only \
    --JSInjectionRules.0.Priority 2
```

Output: 
```
{
    "Response": {
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

