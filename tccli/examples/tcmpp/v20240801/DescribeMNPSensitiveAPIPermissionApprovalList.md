**Example 1: DescribeMNPSensitiveAPIPermissionApprovalList**



Input: 

```
tccli tcmpp DescribeMNPSensitiveAPIPermissionApprovalList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --PlatformId T04257DS9431720WTAG \
    --ApprovalStatusList 30 \
    --Keyword 
```

Output: 
```
{
    "Response": {
        "Data": {
            "DataList": [
                {
                    "APIDesc": "test",
                    "APIId": "api-bmorxwbint70oqno",
                    "APIMethod": "base64ToArrayBuffer",
                    "APIName": "base64ToArrayBuffer",
                    "APIType": 1,
                    "ApplicationId": "app-cc6g35711m",
                    "ApplicationLogo": "http://127.0.0.1/T04257DS9431720WTAG/console/20240802112441-cf9ba6bd4c.png",
                    "ApplicationName": "autotest_app",
                    "ApplyNote": "eee",
                    "ApplyTime": "1722580644",
                    "ApplyUser": "autotest_op",
                    "ApprovalNo": "20240802wfhikl2dzp",
                    "ApprovalNote": "test",
                    "ApprovalStatus": 30,
                    "ApprovalTime": "1722580698",
                    "ApprovalUser": "admin",
                    "MNPId": "mpg9yjc0qbpkelik",
                    "MNPName": "autotest_miniapp"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "01237c35-abfd-44b5-a814-ab4722b293d2"
    }
}
```

