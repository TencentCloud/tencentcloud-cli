**Example 1: 获取构建记录列表**



Input: 

```
tccli makers DescribeDeployments --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --DeploymentIds ************ \
    --Offset 0 \
    --Limit 10 \
    --OrderBy CreatedOn \
    --OrderType DESC \
    --StartTime 2026-11-16 00:00:00 \
    --EndTime 2026-11-17 00:00:00
```

Output: 
```
{
    "Response": {
        "Deployments": [
            {
                "BuildCost": "10917",
                "Code": 18,
                "CoverUrl": null,
                "CreatedOn": "2026-11-16T11:43:15.067Z",
                "DeploymentId": "************",
                "DplRepoUrl": "https://***********************",
                "Env": "Production",
                "MetaData": null,
                "ModifiedOn": "2026-11-16T11:43:30.000Z",
                "OriginalStatus": "Failed",
                "PreviewUrl": "https://*****************************************************",
                "ProjectId": "makers-************",
                "ProjectUrl": "https://************************************************",
                "RepoBranch": "main",
                "RepoCommitHash": "abc1234",
                "RepoCommitMsg": "docs example",
                "Status": "Failed",
                "UsedInProd": true,
                "ViaMeta": "Upload"
            }
        ],
        "TotalCount": 1,
        "RequestId": "48ec6c28-cc3a-4b08-9b09-43b15a5af85b"
    }
}
```

