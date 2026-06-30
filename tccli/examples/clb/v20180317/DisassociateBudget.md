**Example 1: 解除Key的Budget关联**



Input: 

```
tccli clb DisassociateBudget --cli-unfold-argument  \
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

