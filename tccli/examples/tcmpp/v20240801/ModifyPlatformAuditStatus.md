**Example 1: demo**

demo

Input: 

```
tccli tcmpp ModifyPlatformAuditStatus --cli-unfold-argument  \
    --AuditNo abc \
    --AuditResult 0 \
    --PlatformId abc \
    --AuditNote abc \
    --AuditItems.0.ApplicationId abc \
    --AuditItems.0.AuditStatus 0 \
    --AuditItems.0.AuditNote abc
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

