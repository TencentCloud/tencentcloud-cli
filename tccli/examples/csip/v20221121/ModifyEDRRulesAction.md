**Example 1: 批量修改策略动作**



Input: 

```
tccli csip ModifyEDRRulesAction --cli-unfold-argument  \
    --RuleIDs 35f27052-c64e-48b3-8de3-f38c6fdb7bcd \
    --AlertAction 0 \
    --TargetAppIDs 260082268
```

Output: 
```
{
    "Response": {
        "RequestId": "502cfa8c-1a71-4085-8df1-9b5494a84e36"
    }
}
```

