**Example 1: 查询仿冒小程序**



Input: 

```
tccli ctem DescribeFakeMiniPrograms --cli-unfold-argument  \
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
                "Category": "安全",
                "DisplayToolCommon": {
                    "CreateAt": "2025-06-09 11:32:25",
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
                    "Md5": "a734442da5dff90d71bf093551d76982",
                    "UpdateAt": "2025-06-09 14:40:28"
                },
                "HandlingStatus": 2,
                "Id": 1,
                "ProgramId": "wx_sdfsdfasdf",
                "ProgramName": "情报",
                "QrCode": "https://pcmsdfses.com/applet-code.jpg",
                "ShutdownStatus": 0,
                "ShutdownTime": ""
            }
        ],
        "Total": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

