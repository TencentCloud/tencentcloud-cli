**Example 1: 查询仿冒应用**



Input: 

```
tccli ctem DescribeFakeApps --cli-unfold-argument  \
    --CustomerId 100279 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppName": "APP腾讯测试",
                "DisplayToolCommon": {
                    "CreateAt": "2025-06-09 11:25:54",
                    "CustomerId": 100279,
                    "CustomerName": "信息泄露测试",
                    "Detail": "",
                    "EnterpriseName": "分支机构",
                    "EnterpriseUid": "beea23ea16f0d399f33ab77b208c41f7",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Labels": "{}",
                    "Md5": "a73c252da5dff90d71bf093551d76982",
                    "UpdateAt": "2025-06-09 14:43:25"
                },
                "DownloadUrl": "https://xxxxqq.com/http-docker.arthin.net-80-Qndxn.png",
                "HandlingStatus": 1,
                "Id": 1,
                "PackageName": "com.xxx.test",
                "ShutdownStatus": 0,
                "ShutdownTime": ""
            }
        ],
        "Total": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

