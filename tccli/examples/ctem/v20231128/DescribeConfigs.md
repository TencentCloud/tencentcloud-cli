**Example 1: 查看目录爆破数据**

查看目录爆破数据

Input: 

```
tccli ctem DescribeConfigs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Code": 200,
                "ContentLength": 0,
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-07 11:26:14",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "3c7bc55dc38c9c9e4b554f06b169fa7f",
                    "UpdateAt": "2024-06-07 11:27:15"
                },
                "Id": 41,
                "Ip": "",
                "Title": "test",
                "Url": "http://a.cn"
            }
        ],
        "RequestId": "15eb13bd-0a0e-4a3d-9a32-ef6db4186d41",
        "Total": 1,
        "AllConfigNum": 1,
        "HighRiskConfigNum": 1
    }
}
```

