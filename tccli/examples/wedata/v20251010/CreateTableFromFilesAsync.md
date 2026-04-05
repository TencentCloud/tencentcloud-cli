**Example 1: 从文件创建表（异步）**



Input: 

```
tccli wedata CreateTableFromFilesAsync --cli-unfold-argument  \
    --WorkspaceId 1 \
    --Operation CREATE_TABLE \
    --FilePaths cosn://bucket/path/to/file.csv \
    --Catalog  \
    --Schema  \
    --Table employees \
    --ResourceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20251017177920000001",
            "Status": "SUBMITTED",
            "Progress": 10
        },
        "RequestId": "419bf816-cf61-42b1-9273-75459b655c04"
    }
}
```

