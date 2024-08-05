**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeSensitiveAPIAuditList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --AuditStatusList 0 \
    --Keyword abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "AuditNo": "abc",
                    "ApiId": "abc",
                    "ApiName": "abc",
                    "ApiMethod": "abc",
                    "MNPId": "abc",
                    "MNPName": "abc",
                    "ApplyUser": "abc",
                    "ApplyTime": "abc",
                    "ApplyNote": "abc",
                    "AuditStatus": 0,
                    "AuditUser": "abc",
                    "AuditTime": "abc",
                    "AuditNote": "abc",
                    "ApiType": 1,
                    "ApiDesc": "desc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

