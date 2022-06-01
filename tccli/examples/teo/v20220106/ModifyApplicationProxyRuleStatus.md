**Example 1: 修改应用代理规则的状态**



Input: 

```
tccli teo ModifyApplicationProxyRuleStatus --cli-unfold-argument  \
    --ZoneId zone-id123 \
    --ProxyId proxy-id123 \
    --RuleId rule-id123 \
    --Status offline
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "RuleId": "rule-xxx"
    }
}
```

