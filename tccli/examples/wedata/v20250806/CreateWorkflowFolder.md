**Example 1: 创建工作流文件夹**



Input: 

```
tccli wedata CreateWorkflowFolder --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --ParentFolderPath /0_only/0_sub \
    --FolderName child
```

Output: 
```
{
    "Response": {
        "Data": {
            "FolderId": "11b50a0d-8254-11f0-9366-7c8c09fca71c"
        },
        "RequestId": "f87fc425-1798-499e-a6be-dcffd15864fa"
    }
}
```

