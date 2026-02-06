**Example 1: CreateCodeFile**



Input: 

```
tccli wedata CreateCodeFile --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --CodeFileName testFile-0917-1.ipynb \
    --ParentFolderPath / \
    --CodeFileConfig.Params p1 \
    --CodeFileConfig.NotebookSessionInfo.NotebookSessionId dfdfds-3343gdfs-454 \
    --CodeFileConfig.NotebookSessionInfo.NotebookSessionName session1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessScope": "SHARED",
            "CodeFileConfig": {
                "NotebookSessionInfo": {
                    "NotebookSessionId": "dfdfds-3343gdfs-454",
                    "NotebookSessionName": "session1"
                },
                "Params": "p1"
            },
            "CodeFileContent": "",
            "CodeFileId": "2bfa8813-344f-4858-a2cc-7a07bd10ac1d",
            "CodeFileName": "testFile-0917-1.ipynb",
            "CreateTime": "2025-09-17 18:51:32",
            "OwnerUin": "100028579606",
            "Path": "/testFile-0917-1.ipynb",
            "ProjectId": "1470547050521227264",
            "UpdateTime": "2025-09-17 18:51:32",
            "UpdateUserUin": "100028579606"
        },
        "RequestId": "a54aa353-e71f-4507-9c72-80cdbe8dbb78"
    }
}
```

