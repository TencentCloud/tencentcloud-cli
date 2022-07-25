**Example 1: 作业列表新建文件夹**



Input: 

```
tccli oceanus CreateFolder --cli-unfold-argument  \
    --FolderName joylyu-test \
    --ParentId folder-xxxxxxxx \
    --FolderType 0
```

Output: 
```
{
    "Response": {
        "FolderId": "folder-cccccccc",
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccca348a"
    }
}
```

**Example 2: 测试**



Input: 

```
tccli oceanus CreateFolder --cli-unfold-argument  \
    --FolderName test1 \
    --WorkSpaceId space-1257058945ap-guangzho \
    --FolderType 0 \
    --ParentId root
```

Output: 
```
{
    "Response": {
        "FolderId": "folder-qy7n62qr",
        "RequestId": "eb7bbe76-77b3-444d-8554-4dd14394a008"
    }
}
```

**Example 3: 2**



Input: 

```
tccli oceanus CreateFolder --cli-unfold-argument  \
    --FolderName test2 \
    --WorkSpaceId space-1257058945ap-guangzho \
    --FolderType 0 \
    --ParentId root
```

Output: 
```
{
    "Response": {
        "FolderId": "folder-dhq5omrl",
        "RequestId": "a6030a9d-d791-4e7f-8f2c-7d908b6449a0"
    }
}
```

