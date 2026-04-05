**Example 1: 删除代码文件**

删除代码文件

Input: 

```
tccli wedata DeleteCodeFile --cli-unfold-argument  \
    --WorkspaceId workspaceId_test \
    --CodeFileId 1800f374-e469-4e39-86c9-521021c7df63 \
    --ExtensionType ide
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeFileId": "1800f374-e469-4e39-86c9-521021c7df63",
            "Status": true
        },
        "RequestId": "1c826fa4-edd0-4222-aa7b-ba9cede88e8c"
    }
}
```

