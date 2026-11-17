**Example 1: 查询环境列表**



Input: 

```
tccli makers DescribeEnvironments --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************
```

Output: 
```
{
    "Response": {
        "Environments": [
            {
                "AutoDeploy": true,
                "Branches": [
                    "main"
                ],
                "CreatedOn": "2026-11-16T11:38:00.000Z",
                "CustomDomains": [],
                "EnvVars": [],
                "ModifiedOn": "2026-11-16T11:38:00.000Z",
                "Name": "生产",
                "Slug": "Production",
                "Type": "Production"
            }
        ],
        "TotalCount": 2,
        "RequestId": "d3ce7714-ef4c-4a84-a466-557253ce750f"
    }
}
```

