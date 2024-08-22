**Example 1: DescribeMNPSensitiveAPIPermissionList**



Input: 

```
tccli tcmpp DescribeMNPSensitiveAPIPermissionList --cli-unfold-argument  \
    --MNPId mpg9yjc0qbpkelik \
    --Limit 10 \
    --Offset 0 \
    --Keyword testState \
    --ApplicationId  \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "DataList": [
                {
                    "APIId": "api-x9se3c7kg5xjwlvl",
                    "APIName": "testState",
                    "APIMethod": "testState",
                    "APIDesc": "testState",
                    "APIType": 2,
                    "APIStatus": 1,
                    "APIApplyStatus": 30,
                    "RejectReason": "",
                    "ApprovalNo": "20240821ejhfcfnmoq",
                    "ApplicationId": "app-cc6g35711m",
                    "ApplicationIcon": "http://127.0.0.1/T04257DS9431720WTAG/console/20240802112441-cf9ba6bd4c.png",
                    "ApplicationName": "autotest_app"
                }
            ]
        },
        "RequestId": "df5abf55-63fd-4e94-ad8d-423b02e3cb68"
    }
}
```

