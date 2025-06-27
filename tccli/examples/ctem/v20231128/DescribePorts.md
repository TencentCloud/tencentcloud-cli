**Example 1: 查看端口数据**

查看端口数据

Input: 

```
tccli ctem DescribePorts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "App": "mysql",
                "Asset": "db.test.com",
                "Banner": "",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 16:34:35",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "36f9f9e1a49bc000f5bf46e0390b3be5",
                    "UpdateAt": "2024-06-06 16:34:35"
                },
                "Id": 24838,
                "Ip": "1.1.1.1",
                "IsHighRisk": true,
                "Port": 3306,
                "Service": "mysql"
            }
        ],
        "RequestId": "060f8b23-15a0-46ea-9ff8-806729094e98",
        "Total": 1
    }
}
```

