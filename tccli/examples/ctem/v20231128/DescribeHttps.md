**Example 1: 查看http数据**

查看http数据

Input: 

```
tccli ctem DescribeHttps --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Api": "",
                "Code": 200,
                "Content": "",
                "ContentLength": 0,
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 17:15:10",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "1879dc192f156097b5511fbf9b1bd145",
                    "UpdateAt": "2024-06-06 17:15:10"
                },
                "Id": 3248,
                "Ip": "1.1.1.1",
                "ScreenshotThumbUrl": "",
                "ScreenshotUrl": "",
                "Ssl": "",
                "SslExpiredTime": "",
                "Title": "test",
                "Url": "a.test.com"
            }
        ],
        "RequestId": "f1935acd-4fcf-4972-9b9c-82d4661c2347",
        "Total": 1
    }
}
```

