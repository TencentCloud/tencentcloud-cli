**Example 1: demo**

demo

Input: 

```
tccli tcmpp ModifySensitiveAPIAuditStatus --cli-unfold-argument  \
    --AuditNo abc \
    --AuditStatus 0 \
    --AuditNote abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "abc"
    }
}
```

