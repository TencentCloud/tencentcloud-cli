**Example 1: 示例1**

查询数据库列表

Input: 

```
tccli dlc DescribeDatabases --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1068a137-ed80-4cbd-a7e6-1cd0341db332",
        "TotalCount": 1,
        "DatabaseList": [
            {
                "DatabaseName": "testdb",
                "Comment": "create by nick",
                "Properties": null,
                "CreateTime": "1630486408000",
                "ModifiedTime": "1630486408000"
            }
        ]
    }
}
```

