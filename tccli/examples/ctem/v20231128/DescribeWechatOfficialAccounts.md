**Example 1: 查看微信公众号**

查看微信公众号

Input: 

```
tccli ctem DescribeWechatOfficialAccounts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AccountId": "wx123",
                "Description": "",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 19:05:56",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "e8e66edcf875f380cb03930e6d7e8b59",
                    "UpdateAt": "2024-06-06 19:05:56"
                },
                "Id": 12,
                "Logo": "",
                "Name": "com.qq.test测试",
                "QrCode": ""
            }
        ],
        "RequestId": "ca3fbaae-4f42-4382-a01c-e19c7d62364e",
        "Total": 1
    }
}
```

