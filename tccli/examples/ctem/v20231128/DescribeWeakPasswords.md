**Example 1: 查看弱口令数据**

查看弱口令数据

Input: 

```
tccli ctem DescribeWeakPasswords --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Account": "tester",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-07 11:18:56",
                    "CustomerId": 100081,
                    "CustomerName": "腾讯test",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "0647840402863130803dab85174b963f",
                    "UpdateAt": "2024-06-07 11:18:56"
                },
                "Id": 13,
                "Ip": "1.1.1.1",
                "IsHoneypot": true,
                "Password": "321#abc",
                "Port": 22,
                "Type": "",
                "Url": "http://a.cn"
            }
        ],
        "RequestId": "176ed921-d230-44d3-a9af-b431f2e86da7",
        "Total": 1
    }
}
```

