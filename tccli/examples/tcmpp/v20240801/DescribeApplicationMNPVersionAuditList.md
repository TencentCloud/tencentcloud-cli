**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeApplicationMNPVersionAuditList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --AuditStatusList 0 \
    --Keyword abc \
    --ApplicationId abc \
    --TeamId abc
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
                    "ApplicationId": "abc",
                    "AuditStatus": 0,
                    "MNPId": "abc",
                    "MNPVersion": "abc",
                    "MNPVersionId": 0,
                    "ApplyUser": "abc",
                    "ApplyTime": "abc",
                    "MNPName": "abc",
                    "MNPIcon": "abc",
                    "ApplicationName": "abc",
                    "ApplicationLogo": "abc",
                    "TeamId": "abc",
                    "TeamName": "abc",
                    "ApplicationAndUrl": "abc",
                    "ApplicationIOSUrl": "abc",
                    "MNPQrCodeUrl": "abc",
                    "MNPType": "abc",
                    "AuditUser": "abc",
                    "AuditTime": "abc",
                    "AuditNote": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

