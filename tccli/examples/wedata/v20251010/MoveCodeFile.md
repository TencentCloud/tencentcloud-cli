**Example 1: 移动代码文件到指定文件夹**

移动代码文件到指定文件夹

Input: 

```
tccli wedata MoveCodeFile --cli-unfold-argument  \
    --WorkspaceId workspaceId_test \
    --CodeFileId 1107a3f1-5592-46a1-bb9f-522a819b6a78 \
    --ExtensionType ide \
    --ParentFolderId 0be14a43-0be7-480f-8450-3bcbcc0dea48
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeFileId": "1107a3f1-5592-46a1-bb9f-522a819b6a78",
            "Status": true
        },
        "RequestId": "8341dd0d-35ab-4c3c-8728-5d87c8ceccca"
    }
}
```

