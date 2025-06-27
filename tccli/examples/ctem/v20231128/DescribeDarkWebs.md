**Example 1: 查看暗网数据**

查看暗网数据

Input: 

```
tccli ctem DescribeDarkWebs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Content": "test",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-07 11:32:09",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "dd5a495259147cfa1d9d4c4ab4414610",
                    "UpdateAt": "2024-06-07 11:32:09"
                },
                "Id": 30,
                "MatchedKeywords": "123",
                "Url": "http://a.cn"
            }
        ],
        "RequestId": "0dad3f27-bf93-4b11-bc20-acc6ae2a2932",
        "Total": 1
    }
}
```

