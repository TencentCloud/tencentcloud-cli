**Example 1: 成功响应**



Input: 

```
tccli wedata RollbackCodeFileVersion --cli-unfold-argument  \
    --CodeFileId 74a0cab9-ed79-4432-8c79-e8e6ed623861 \
    --WorkspaceId worksapceId_test \
    --TargetVersion 1 \
    --ExtensionType ide
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "309aa76e-b75c-485a-9d73-79fb4af2a517"
    }
}
```

