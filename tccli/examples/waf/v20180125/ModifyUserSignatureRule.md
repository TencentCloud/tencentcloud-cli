**Example 1: 查询示例**



Input: 

```
tccli waf ModifyUserSignatureRule --cli-unfold-argument  \
    --Status 0 \
    --Domain www.test.com \
    --MainClassID xss \
    --RuleID.0.Status 0 \
    --RuleID.0.Reason 0 \
    --RuleID.0.Id 10000266
```

Output: 
```
{
    "Response": {
        "RequestId": "a4010dd1-d24b-43f5-bab4-8a6b204835b7"
    }
}
```

