**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeSensitiveApiApplyDetail --cli-unfold-argument  \
    --AuditNo abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "APIId": "abc",
            "APIMethod": "abc",
            "ApplyReason": "abc",
            "RejectReason": "abc",
            "AuditStatus": 0,
            "APIDesc": "111",
            "APIType": 1
        },
        "RequestId": "abc"
    }
}
```

