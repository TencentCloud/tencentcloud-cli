**Example 1: 更新工作流文件夹名称**

更新工作流文件夹名称

Input: 

```
tccli wedata UpdateWorkflowFolder --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --FolderId f526424c-81b8-11f0-9366-7c8c09fca71c \
    --FolderName 0_new_folder
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "d56a3552-15c5-4372-a235-fd86166e57ef"
    }
}
```

