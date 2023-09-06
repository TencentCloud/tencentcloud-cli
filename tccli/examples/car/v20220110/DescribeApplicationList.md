**Example 1: 添加查询云应用列表请求**

查询应用列表

Input: 

```
tccli car DescribeApplicationList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name ApplicationId \
    --Filters.0.Values app-6get57ac
```

Output: 
```
{
    "Response": {
        "UserApplicationList": [
            {
                "ApplicationId": "app-6get57ac",
                "ApplicationName": "xxx",
                "ApplicationType": "Application3D",
                "ApplicationExePath": "xxx",
                "ApplicationInterList": "xxx",
                "ApplicationParams": "xxx",
                "ApplicationCreateTime": "2021-08-29T08:00:30Z",
                "ApplicationRunStatus": "xxx",
                "ApplicationUpdateStatus": "xxx",
                "ApplicationUpdateProgress": 100,
                "ApplicationVersions": [
                    {
                        "ApplicationVersionId": "ver-gq4c5eq",
                        "ApplicationVersionSize": 1024,
                        "ApplicationVersionStatus": "xxx",
                        "ApplicationVersionName": "xxx",
                        "CreateTime": "2021-08-29T08:00:30Z"
                    }
                ],
                "ApplicationBaseInfo": {
                    "WindowUseType": "xxx",
                    "WindowName": "xxx",
                    "WindowClassName": "xxx"
                },
                "ApplicationNature": "PUBLIC",
                "ApplicationStores": [
                    {
                        "CosBucket": "bucket-123456",
                        "CosRegion": "ap-guangzhou",
                        "StoreType": "LOG",
                        "StoreState": "ON",
                        "StorePath": "xxx"
                    },
                    {
                        "CosBucket": "bucket-123456",
                        "CosRegion": "ap-guangzhou",
                        "StoreType": "ARCHIVE",
                        "StoreState": "OFF",
                        "StorePath": "xxx"
                    }
                ]
            }
        ],
        "ApplicationTotal": 100,
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

