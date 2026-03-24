**Example 1: 查询修正记录**



Input: 

```
tccli config ListRemediationExecutions --cli-unfold-argument  \
    --RuleId cr-RhUgJXUIOisba3r8uEqf \
    --Limit 10 \
    --Offset 1 \
    --ExecutionStatus 1
```

Output: 
```
{
    "Response": {
        "RemediationExecutions": [],
        "Total": 0,
        "RequestId": "62f735cf-3135-4cd7-8349-f0c2fd09f11e"
    }
}
```

