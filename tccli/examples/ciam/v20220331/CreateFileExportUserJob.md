**Example 1: 新建文件导出用户任务**



Input: 

```
tccli ciam CreateFileExportUserJob --cli-unfold-argument  \
    --UserStoreId xx \
    --ExportPropertyMaps.0.ColumnName xx \
    --ExportPropertyMaps.0.UserPropertyCode xx \
    --Filters.0.Values xx \
    --Filters.0.Key xx \
    --Filters.0.Logic True \
    --Format xx
```

Output: 
```
{
    "Response": {
        "Job": {
            "Status": "xx",
            "Format": "xx",
            "ErrorDetails": [
                {
                    "UserId": "xx",
                    "Error": "xx"
                }
            ],
            "Location": "xx",
            "CreatedDate": 0,
            "FailedUsers": [
                {
                    "FailedUserIdentification": "xx",
                    "FailedReason": "xx"
                }
            ],
            "Type": "xx",
            "Id": "xx"
        },
        "RequestId": "xx"
    }
}
```

