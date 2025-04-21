**Example 1: 示例1**



Input: 

```
tccli ioa ModifyAccountSecurityPolicy --cli-unfold-argument  \
    --Status 1 \
    --PolicyName  \
    --ScopeItems.0.List.0.Name  \
    --ScopeItems.0.List.0.IdPathArr 0 \
    --ScopeItems.0.List.0.Id 0 \
    --ScopeItems.0.ScopeType 0 \
    --PolicyPriority 1 \
    --Description  \
    --Detail  \
    --ExpireTime 1 \
    --PolicyType 1 \
    --PolicyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "81d13817-209e-4237-978e-71ec82fe2c77"
    }
}
```

