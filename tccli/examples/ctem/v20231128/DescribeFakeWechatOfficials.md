**Example 1: 查询仿冒公众号**



Input: 

```
tccli ctem DescribeFakeWechatOfficials --cli-unfold-argument  \
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
                "AccountName": "测试1",
                "Avatar": "https://screenoud.com/2025-05-26/http-docker.arthin.net-80-Qndxn.png",
                "DisplayToolCommon": {
                    "CreateAt": "2025-06-09 14:42:28",
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
                    "Md5": "",
                    "UpdateAt": "2025-06-09 14:43:42"
                },
                "HandlingStatus": 2,
                "Id": 2,
                "QrCode": "https://pcmgcloud.com/web-static/images/expert-code.svg",
                "ShutdownStatus": 5,
                "ShutdownTime": "",
                "WechatId": "wx_2222"
            },
            {
                "AccountName": "测试公众号",
                "Avatar": "https://screenssdfadfa.com/5-26/http-docker.arthin.net-80-Qndxn.png",
                "DisplayToolCommon": {
                    "CreateAt": "2025-06-09 11:26:59",
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
                    "Md5": "a73c252123dff90d71bf093551d76982",
                    "UpdateAt": "2025-06-09 14:43:51"
                },
                "HandlingStatus": 0,
                "Id": 1,
                "QrCode": "https://sdfasfaages.com/expert-code.svg",
                "ShutdownStatus": 0,
                "ShutdownTime": "",
                "WechatId": "wx_xxxxddfa"
            }
        ],
        "Total": 2,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

