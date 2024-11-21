**Example 1: 添加封禁**

添加封禁

Input: 

```
tccli cfw CreateBlockIgnoreRuleList --cli-unfold-argument  \
    --Rules.0.IP 1.1.1.1 \
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
        "List": [
            {
                "IP": "1.1.1.1",
                "Direction": 1
            }
        ],
        "RequestId": "e7c8de24-958f-4200-9d30-ddd186d6ee48"
    }
}
```

