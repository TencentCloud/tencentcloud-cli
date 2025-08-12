**Example 1: 查看微信小程序数据**

查看微信小程序数据

Input: 

```
tccli ctem DescribeWechatApplets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AccountId": "tester",
                "Description": "",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 17:42:47",
                    "CustomerId": 100081,
                    "CustomerName": "腾讯test",
                    "Detail": "com.qq.test测试",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "a14874f9e36c3f04e0dfc3ab8967ef4c",
                    "UpdateAt": "2024-06-06 17:42:47"
                },
                "Id": 11,
                "Logo": "",
                "Name": "com.qq.test",
                "QrCode": ""
            }
        ],
        "RequestId": "055d7aa9-6cec-43e9-8f5f-27c3425d7b7c",
        "Total": 1
    }
}
```

