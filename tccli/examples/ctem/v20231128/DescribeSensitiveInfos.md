**Example 1: 查看敏感信息泄露数据**

查看敏感信息泄露数据

Input: 

```
tccli ctem DescribeSensitiveInfos --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-07 14:15:14",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "366ecd81e3353e615b1e7dd13e5bf7fa",
                    "UpdateAt": "2024-06-07 14:15:30"
                },
                "Id": 10,
                "Source": "baidu.com",
                "Type": "敏感信息",
                "Value": "key=123"
            }
        ],
        "RequestId": "dc218a31-31be-45d7-94d0-8565c9fb9f89",
        "Total": 1
    }
}
```

