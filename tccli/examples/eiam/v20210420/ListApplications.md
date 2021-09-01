**Example 1: 请求示例**



Input: 

```
tccli eiam ListApplications --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "xxx",
        "ApplicationInfoList": [
            {
                "ApplicationType": "API",
                "LastModifiedDate": "2021-07-07T16:05:47.964+0800",
                "AppStatus": true,
                "CreatedDate": "2021-07-07T16:05:47.964+0800",
                "DisplayName": "112",
                "ClientId": null,
                "Icon": null,
                "ApplicationId": "xxx"
            },
            {
                "ApplicationType": "API",
                "LastModifiedDate": "2021-07-07T16:04:34.529+0800",
                "AppStatus": true,
                "CreatedDate": "2021-07-07T16:04:34.529+0800",
                "DisplayName": "字符串",
                "ClientId": null,
                "Icon": null,
                "ApplicationId": "xxx"
            }
        ]
    }
}
```

