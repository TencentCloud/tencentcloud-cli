**Example 1: 成功**



Input: 

```
tccli wedata ExportEnvironment --cli-unfold-argument  \
    --WorkspaceId workspace_id_test \
    --KernelId 7e4c9d2b-6b8a-4f5e-9c3e-2a1f6b8d0c42 \
    --ParentFolderId 9d676e72-9b04-3e1f-8abd-4b5473c10a90 \
    --CodeFileName environment_2025-12-15_17-13-34.yaml
```

Output: 
```
{
    "Response": {
        "Data": {
            "FileId": "test_file_id",
            "FilePath": "test_file_path"
        },
        "RequestId": "58565e50-af12-4fa2-950e-1d47c6c4a571"
    }
}
```

