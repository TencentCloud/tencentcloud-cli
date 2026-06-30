**Example 1: 关联Key到Budget**



Input: 

```
tccli clb AssociateBudget --cli-unfold-argument  \
    --BudgetId budget-1a2b3c4d \
    --Resources.0.Type Key \
    --Resources.0.ModelRouterId cmr-abc12345 \
    --Resources.0.KeyId vkey-abc12345
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

