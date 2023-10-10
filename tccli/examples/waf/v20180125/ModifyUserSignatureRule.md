**Example 1: 查询示例**



Input: 

```
tccli waf ModifyUserSignatureRule --cli-unfold-argument  \
    --Status 0 \
    --Domain xx \
    --MainClassID xx \
    --RuleID.0.Status 0 \
    --RuleID.0.Reason 0 \
    --RuleID.0.Id xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

