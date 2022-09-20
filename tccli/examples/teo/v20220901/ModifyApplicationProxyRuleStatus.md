**Example 1: 修改应用代理规则的状态**



Input: 

```
tccli teo ModifyApplicationProxyRuleStatus --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --ProxyId proxy-19389e5dwwxfs \
    --RuleId rule-19389e5a-118b-11ed-9951-525400655ede \
    --Status offline
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

