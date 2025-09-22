**Example 1: 更新sql文件夹示例**



Input: 

```
tccli wedata UpdateSQLFolder --cli-unfold-argument  \
    --FolderId b757d015-da6c-41ba-8f5b-50f6da8f5a2d \
    --FolderName data2 \
    --ProjectId 2917455276892352512 \
    --AccessScope SHARED
```

Output: 
```
{
    "Response": {
        "Data": {
            "FolderId": "b757d015-da6c-41ba-8f5b-50f6da8f5a2d",
            "Status": true
        },
        "RequestId": "8d12692c-97b5-4310-9d07-446bcc1865d5"
    }
}
```

