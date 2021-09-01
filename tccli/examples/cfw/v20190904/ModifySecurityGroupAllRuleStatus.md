**Example 1: 启用停用全部安全组规则**



Input: 

```
tccli cfw ModifySecurityGroupAllRuleStatus --cli-unfold-argument  \
    --EdgeId  \
    --Status 1 \
    --Direction 1 \
    --Area 
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "b21d7f7c-3191-41a2-bd13-9a5f6d86ab44"
    }
}
```

