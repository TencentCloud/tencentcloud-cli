**Example 1: 更新文件夹**

编排空间-更新文件夹

Input: 

```
tccli wedata ModifyDsFolder --cli-unfold-argument  \
    --ProjectId abc \
    --ParentsFolderId abc \
    --FolderName abc \
    --FolderId abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

