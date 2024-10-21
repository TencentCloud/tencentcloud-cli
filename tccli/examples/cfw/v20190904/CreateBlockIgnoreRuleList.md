**Example 1: 空值返回**

空值返回

Input: 

```
tccli cfw CreateBlockIgnoreRuleList --cli-unfold-argument  \
    --Rules.0.IP 1.1.1.1 \
    --Rules.0.Domain  \
    --Rules.0.Direction 1 \
    --Rules.0.EndTime 2025-01-01 00:00:00 \
    --Rules.0.Comment 阻断访问 \
    --Rules.0.StartTime 2024-10-10 00:00:00 \
    --RuleType 1
```

Output: 
```
{
    "Response": {
        "RequestId": ""
    }
}
```

