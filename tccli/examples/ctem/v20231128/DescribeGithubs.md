**Example 1: 查看github泄露数据**

查看github泄露数据

Input: 

```
tccli ctem DescribeGithubs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Content": "key=123",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-07 11:38:06",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "6b72273989650c06b3e3c7b48fdf724f",
                    "UpdateAt": "2024-06-07 11:38:06"
                },
                "Id": 15,
                "MatchedKeywords": "password",
                "Status": "泄露",
                "Url": "http://github.com/aaa"
            }
        ],
        "RequestId": "b3b19eca-1d28-4be9-9646-3740c7c84520",
        "Total": 1
    }
}
```

