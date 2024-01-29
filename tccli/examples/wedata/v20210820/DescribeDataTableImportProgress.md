**Example 1: 示例1**

数据导入中

Input: 

```
tccli wedata DescribeDataTableImportProgress --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --Id 23
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "2023-06-02 14:22:42",
            "DatabaseName": "ztt_test",
            "DatasourceId": "8444",
            "DatasourceType": "HIVE",
            "Id": 23,
            "ImportStatus": 5,
            "Message": "导入数据中",
            "OwnerUserId": 100028448903,
            "ProjectId": "1460947878944567296",
            "SourceDataPath": "cosn://jaydenjhu-1315051789/datastudio/data_manage/import/1460947878944567296/110101000000.csv",
            "TableName": "teq1",
            "TenantId": 1315051789,
            "UpdateTime": "2023-06-02 16:43:06",
            "UserId": 100028579606
        },
        "RequestId": "d48e04fb-cf2a-44b6-8004-521e267159f9"
    }
}
```

