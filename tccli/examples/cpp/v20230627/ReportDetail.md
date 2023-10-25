**Example 1:  ReportDetail 明细上报**



Input: 

```
tccli cpp ReportDetail --cli-unfold-argument  \
    --TaskId abc \
    --UserId abc \
    --Message abc \
    --CreatedTime 0 \
    --BillingItem abc \
    --Count 0
```

Output: 
```
{
    "Response": {
        "Code": 1,
        "Message": "abc",
        "RequestId": "abc"
    }
}
```

