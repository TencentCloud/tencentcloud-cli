**Example 1: 查看漏洞数据**

查看漏洞数据

Input: 

```
tccli ctem DescribeVuls --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DiscoverTime": "2024-06-07 10:59:23",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-07 10:59:23",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "847604bc4c5622c19116008cc8454e33",
                    "UpdateAt": "2024-06-07 10:59:23"
                },
                "Id": 168,
                "Ip": "1.1.1.1",
                "Level": 0,
                "Name": "test",
                "Port": 80,
                "RepairStatus": 0,
                "Suggestion": "",
                "Url": "http://a.cn"
            }
        ],
        "RequestId": "0eb8c233-c47f-4a80-97c3-7a551f1178cc",
        "Total": 1
    }
}
```

