**Example 1: DescribeApplication**



Input: 

```
tccli tcmpp DescribeApplication --cli-unfold-argument  \
    --ApplicationId app-cc6g35711m \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "AndroidAppKey": "com.tencent.tcmpp.demo",
            "AppIdentityId": 100097611,
            "ApplicationId": "app-cc6g35711m",
            "ApplicationName": "autotest_app",
            "ApplicationType": 2,
            "CreateTime": "1721010944",
            "CreateUser": "autotest_op",
            "Intro": "modify application0802112440",
            "IosAppKey": "com.tencent.tcmpp.demo",
            "Logo": "http://127.0.0.1/T04257DS9431720WTAG/console/20240802112441-cf9ba6bd4c.png",
            "Remark": "",
            "SensitiveApiCount": 19,
            "TeamId": "3686677859",
            "TeamName": "autotest_app_team",
            "UpdateTime": "1724019292",
            "UpdateUser": "autotest_op"
        },
        "RequestId": "57c3656b-71bb-49a4-b6f7-8c467917d964"
    }
}
```

