**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeApplicationList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --Keyword abc \
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
                    "CustomerID": "abc",
                    "ApplicationID": "abc",
                    "AppIdentityID": 0,
                    "ApplicationName": "abc",
                    "ApplicationEnglishName": "abc",
                    "Logo": "abc",
                    "Remark": "abc",
                    "AndroidAppKey": "abc",
                    "IosAppKey": "abc",
                    "CreateUser": "abc",
                    "CreateTime": "abc",
                    "UpdateUser": "abc",
                    "UpdateTime": "abc",
                    "Intro": "abc",
                    "IosAppUrl": "abc",
                    "AndroidAppUrl": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

