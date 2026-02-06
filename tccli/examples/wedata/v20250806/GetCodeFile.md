**Example 1: GetCodeFile**



Input: 

```
tccli wedata GetCodeFile --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --CodeFileId c0e17cbc-7226-47d4-b9f2-f591705a9ffc \
    --IncludeContent False
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessScope": "SHARED",
            "CodeFileConfig": {
                "NotebookSessionInfo": {
                    "NotebookSessionId": "434343243",
                    "NotebookSessionName": "dsfdfsdf"
                },
                "Params": "sffdf"
            },
            "CodeFileContent": "sdsdsd",
            "CodeFileId": "c0e17cbc-7226-47d4-b9f2-f591705a9ffc",
            "CodeFileName": "test111",
            "CreateTime": "2025-08-27 21:40:26",
            "OwnerUin": "100028579606",
            "Path": "/test111",
            "ProjectId": "1470547050521227264",
            "UpdateTime": "2025-08-27 21:40:26",
            "UpdateUserUin": "100028579606"
        },
        "RequestId": "e5b6f458-b78f-4e87-87a5-9880f41313e8"
    }
}
```

