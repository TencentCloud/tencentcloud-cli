**Example 1: 创建文件夹**

编排空间-创建文件夹

Input: 

```
tccli wedata CreateDsFolder --cli-unfold-argument  \
    --ProjectId 1485413914375667712 \
    --ParentsFolderId 860a23d6-ea4a-11ed-8909-bc97e105ba60 \
    --FolderName gallop
```

Output: 
```
{
    "Response": {
        "Data": "gallop",
        "RequestId": "d398e684-f7d7-40d3-b6ec-9441eb6c5328"
    }
}
```

