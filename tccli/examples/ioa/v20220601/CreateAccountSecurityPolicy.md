**Example 1: 示例1**



Input: 

```
tccli ioa CreateAccountSecurityPolicy --cli-unfold-argument  \
    --Status 2 \
    --PolicyName 基础策略 \
    --ScopeItems.0.ScopeType 1 \
    --ScopeItems.0.List.0.Id 16529 \
    --PolicyPriority 50 \
    --Description  \
    --Detail {"TicketValidTime":1,"AutoLoginSwitch":2} \
    --ExpireTime 0 \
    --PolicyType 2 \
    --PolicyId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "ad159b64-de34-43ca-9556-559ef483ac47"
    }
}
```

