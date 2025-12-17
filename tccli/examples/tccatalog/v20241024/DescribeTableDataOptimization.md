**Example 1: 示例一**

示例一

Input: 

```
tccli tccatalog DescribeTableDataOptimization --cli-unfold-argument  \
    --CatalogName wd_lakehouse \
    --SchemaName mydb01 \
    --TableName mytb08 \
    --StartTime 2025-09-29 14:28:21 \
    --EndTime 2025-09-30 14:28:21 \
    --Status success \
    --Limit 3 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "AfterAverageFileSize": 0,
        "BeforeAverageFileSize": 0,
        "DataCount": 0,
        "DataList": [],
        "FileCount": 0,
        "TaskCount": 0,
        "RequestId": "f6acb12d-e45e-4655-abfd-3e56d156ad0d"
    }
}
```

