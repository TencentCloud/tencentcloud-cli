**Example 1: 提交CodeFileJob**

提交CodeFileJob

Input: 

```
tccli wedata SubmitCodeFileJob --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --CodeFileId 794235159865778176 \
    --CodeFileName test-1.sql \
    --CodeFileContent c2VsZWN0IDE= \
    --CodeFileConfig.ResourceId res-c267d284 \
    --CodeFileConfig.DefaultCatalog default \
    --CodeFileConfig.DefaultSchema default \
    --ExtensionType SQL_FILE \
    --RunMode RUN_ALL
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeFileContent": "",
            "CodeFileId": "",
            "EndTime": "0",
            "JobExecution": [],
            "JobId": "6820260106175314006",
            "JobName": "20260106-1753",
            "ScriptContentTruncate": false,
            "StartTime": "0",
            "Status": "QUEUED",
            "TimeCost": "0"
        },
        "RequestId": "add7da99-957b-401e-92b2-75c665662c81"
    }
}
```

