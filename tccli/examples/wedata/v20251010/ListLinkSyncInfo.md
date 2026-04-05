**Example 1: 示例1**



Input: 

```
tccli wedata ListLinkSyncInfo --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --PageNumber 1 \
    --PageSize 10 \
    --TaskId 5d8d60ac-cfb7-437a-b6d8-40666a9c34a4
```

Output: 
```
{
    "Response": {
        "Data": {
            "LinkSyncInfos": [
                {
                    "DdlSql": "DdlSql",
                    "SourceDatabase": "SourceDatabase",
                    "SourceSchema": "SourceSchema",
                    "SourceTable": "SourceTable",
                    "SyncType": "SyncType",
                    "WriteRecordNum": "WriteRecordNum"
                }
            ],
            "TotalCount": "0"
        },
        "RequestId": "a7351f8f-0cee-40f7-9499-4fef39fbaa78"
    }
}
```

