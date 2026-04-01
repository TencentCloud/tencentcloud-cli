**Example 1: 根据DDL创建表**



Input: 

```
tccli wedata CreateTableByDDL --cli-unfold-argument  \
    --Type TCLAKE \
    --DDLSql Q1JFQVRFIFRBQkxFIHRlc3RfY2F0YWxvZy50ZXN0X3NjaGVtYS50ZXN0X3RhYmxlIChpZCBJTlQgQ09NTUVOVCAnSUQnLCBuYW1lIFNUUklORyBDT01NRU5UICdOYW1lJywgYWdlIElOVCBDT01NRU5UICdBZ2UnKSBDT01NRU5UICdUZXN0IHRhYmxlJyBTVE9SRUQgQVMgUEFSUVVFVA== \
    --ComputeResourceId resource_1 \
    --WorkspaceId 17622177773248536 \
    --ConnectionId 1 \
    --Database test_db \
    --Catalog test_db \
    --Schema test_schema
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": "6820260205204135039",
            "Table": "test_table"
        },
        "RequestId": "2f25b7f4-d021-41bc-99ca-2707e257fb78"
    }
}
```

