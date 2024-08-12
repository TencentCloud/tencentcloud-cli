**Example 1: demo**

demo

Input: 

```
tccli tcmpp ModifyPlatformAuditStatus --cli-unfold-argument  \
    --PlatformId T02245JR9111721GKOI \
    --AuditNo aud06ndxthykkw75l3 \
    --AuditNote  \
    --AuditResult 3 \
    --AuditItems.0.ApplicationId app-i8kxgprhks \
    --AuditItems.0.AuditStatus 3 \
    --AuditItems.0.AuditNote 
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "accd370371a14145bf44f269ec2fab03"
    }
}
```

