**Example 1: DescribeApplicationList**



Input: 

```
tccli tcmpp DescribeApplicationList --cli-unfold-argument  \
    --TeamId  \
    --Limit 20 \
    --Offset 0 \
    --Keyword  \
    --PlatformId T04827BQ9761718REMX
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "ApplicationId": "abc",
                    "AppIdentityId": 0,
                    "ApplicationName": "abc",
                    "Logo": "abc",
                    "Remark": "abc",
                    "AndroidAppKey": "abc",
                    "IosAppKey": "abc",
                    "CreateUser": "abc",
                    "CreateTime": "abc",
                    "UpdateUser": "abc",
                    "UpdateTime": "abc",
                    "Intro": "abc",
                    "TeamId": "abc",
                    "TeamName": "abc",
                    "SensitiveApiCount": 0,
                    "ApplicationType": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

