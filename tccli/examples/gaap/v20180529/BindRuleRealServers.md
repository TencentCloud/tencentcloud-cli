**Example 1: 转发规则绑定源站**

转发规则绑定源站

Input: 

```
tccli gaap BindRuleRealServers --cli-unfold-argument  \
    --RealServerBindSet.0.RealServerWeight 1 \
    --RealServerBindSet.0.RealServerId rs-i3658cdf \
    --RealServerBindSet.0.RealServerIP 1.1.1.1 \
    --RealServerBindSet.0.RealServerPort 80 \
    --RuleId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

