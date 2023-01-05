**Example 1: 编辑自动化规则状态**

编辑自动化规则状态

Input: 

```
tccli hasim ModifyRuleStatus --cli-unfold-argument  \
    --RuleID 10001 \
    --IsActive True
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 2: modifystatus**



Input: 

```
tccli hasim ModifyRuleStatus --cli-unfold-argument  \
    --IsActive true \
    --RuleID 10027
```

Output: 
```
{
    "Response": {
        "RequestId": "0aabacc0-ca02-487d-a795-9376739257fd"
    }
}
```

