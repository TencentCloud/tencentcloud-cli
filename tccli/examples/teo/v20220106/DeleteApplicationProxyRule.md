**Example 1: 删除应用代理规则**



Input: 

```
tccli teo DeleteApplicationProxyRule --cli-unfold-argument  \
    --ZoneId zone-id123 \
    --ProxyId proxy-id123 \
    --RuleId rule-id123
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

