**Example 1: 空值返回**

空值返回

Input: 

```
tccli cfw ModifyBlockIgnoreRule --cli-unfold-argument  \
    --Rule.IP 1.1.1.1 \
    --Rule.Domain www.domain.com \
    --Rule.Direction 0 \
    --Rule.EndTime 2025-01-01 00:00:00 \
    --Rule.Comment 阻断访问 \
    --Rule.StartTime 2024-01-01 00:00:00 \
    --RuleType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3c442984-c832-43d0-b687-664845ee31b0"
    }
}
```

