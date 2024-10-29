**Example 1: 新建文件导出用户任务**



Input: 

```
tccli ciam CreateFileExportUserJob --cli-unfold-argument  \
    --UserStoreId 2c3aca3b****************a7efe88e \
    --Format NDJSON \
    --Filters.0.Key local \
    --Filters.0.Values beijing \
    --Filters.0.Logic True \
    --ExportPropertyMaps.0.UserPropertyCode nickname \
    --ExportPropertyMaps.0.ColumnName 昵称
```

Output: 
```
{
    "Response": {
        "Job": {
            "Id": "c29f2c0f****************405ec698",
            "Status": "PENDING",
            "Type": "IMPORT_USER",
            "CreatedDate": 1715156770024,
            "Format": "NDJSON",
            "Location": "http://aa.com/bb.csv",
            "ErrorDetails": [
                {
                    "UserId": "53e25c3****************e4eb5bd1",
                    "Error": "error message"
                }
            ],
            "FailedUsers": [
                {
                    "FailedUserIdentification": "53e25c3****************e4eb5bd1",
                    "FailedReason": "error reason"
                }
            ]
        },
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

