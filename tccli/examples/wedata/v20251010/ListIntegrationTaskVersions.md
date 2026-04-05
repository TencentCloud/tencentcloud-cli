**Example 1: 查询集成任务版本列表**



Input: 

```
tccli wedata ListIntegrationTaskVersions --cli-unfold-argument  \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --WorkspaceId test-project-001 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed",
            "TotalCount": "1",
            "VersionInfoSet": [
                {
                    "CreateTime": "1766135530488",
                    "CreatorUin": "700002164618",
                    "Id": "5f451edd-546e-4ada-899f-69e02af3a5e2",
                    "IsProd": "0",
                    "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed",
                    "TaskVersion": "20251219171210",
                    "UpdateTime": "1766135530488",
                    "UpdaterUin": "700002164618"
                }
            ]
        },
        "RequestId": "713af3e6-dc8d-4b44-8eaa-319ceec15fa7"
    }
}
```

