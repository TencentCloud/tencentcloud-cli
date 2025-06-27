**Example 1: 查看网盘泄露数据**

查看网盘泄露数据

Input: 

```
tccli ctem DescribeNetDisks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Content": "test",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-07 11:43:18",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "fbecc76ff52943c9bff65515521dc0de",
                    "UpdateAt": "2024-06-07 11:43:18"
                },
                "Id": 32,
                "MatchedKeywords": "123",
                "Platform": "baidu.com",
                "Status": "",
                "Url": "http://a.cn"
            }
        ],
        "RequestId": "b440b23c-5f8f-4150-b806-07d7a57ade2a",
        "Total": 1
    }
}
```

