**Example 1: 查询仿冒网站**



Input: 

```
tccli ctem DescribeFakeWebsites --cli-unfold-argument  \
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
                "DisplayToolCommon": {
                    "CreateAt": "2025-06-06 11:26:29",
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
                    "Md5": "a73c252da53b290d71bf093551d76982",
                    "UpdateAt": "2025-06-09 14:43:12"
                },
                "HandlingStatus": 0,
                "IPLocation": "中国 北京市",
                "Id": 1,
                "Screenshot": "https://xxxxxxxxx.com/http-docker.arthin.net-80-Qndxn.png",
                "ShutdownStatus": 0,
                "ShutdownTime": "",
                "Website": "test.qq.com"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Total": 1
    }
}
```

