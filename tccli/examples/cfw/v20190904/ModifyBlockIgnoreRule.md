**Example 1: 空值返回**

空值返回

Input: 

```
tccli cfw ModifyBlockIgnoreRule --cli-unfold-argument  \
    --Rule.IP abc \
    --Rule.Domain abc \
    --Rule.Direction 0 \
    --Rule.EndTime abc \
    --Rule.Comment abc \
    --Rule.StartTime abc \
    --RuleType 0
```

Output: 
```
{
    "Response": {
        "RequestId": ""
    }
}
```

