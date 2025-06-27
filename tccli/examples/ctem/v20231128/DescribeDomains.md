**Example 1: 查看主域名数据**

查看主域名数据

Input: 

```
tccli ctem DescribeDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Company": "",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 15:49:05",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "b0b91453d6733070139b6a2bd3ba1514",
                    "UpdateAt": "2024-06-06 15:49:05"
                },
                "Domain": "test.com",
                "ExpiredTime": "",
                "ICP": "",
                "Id": 4436,
                "RegisteredTime": ""
            }
        ],
        "RequestId": "c2a13b42-e53c-4b93-a290-a4cc61bae379",
        "Total": 1
    }
}
```

