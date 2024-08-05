**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeApplication --cli-unfold-argument  \
    --ApplicationId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
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
            "BindMNPCount": 0,
            "BindMNPList": [
                {
                    "MNPId": "abc",
                    "MNPName": "abc",
                    "MNPIcon": "abc",
                    "MNPType": "abc",
                    "MNPIntro": "abc",
                    "MNPDesc": "abc",
                    "EffectStatus": 0,
                    "EffectMNPVersion": "abc",
                    "MNPOnlineVersion": "abc",
                    "OnlineStatus": 0
                }
            ],
            "Intro": "abc",
            "AndroidAppUrl": "abc",
            "IosAppUrl": "abc"
        },
        "RequestId": "abc"
    }
}
```

