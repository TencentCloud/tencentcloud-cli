**Example 1: 获取用户项目列表**



Input: 

```
tccli makers DescribeProjects --cli-unfold-argument  \
    --ZoneId zone-3v5********* \
    --Offset 0 \
    --Limit 10 \
    --ProjectIds makers-yvl********* \
    --OrderBy CreatedOn \
    --OrderType DESC \
    --Source **** \
    --Query makers-functions-demo
```

Output: 
```
{
    "Response": {
        "Projects": [
            {
                "AgentFramework": null,
                "Area": "********",
                "BuildCmd": null,
                "CreatedOn": "2026-11-11T09:06:43.608Z",
                "CustomDomains": [],
                "Deployment": {
                    "BuildCost": "18275",
                    "CoverUrl": null,
                    "CreatedOn": "2026-11-11T09:06:45.114Z",
                    "DeploymentId": "dpdol*******",
                    "DplRepoUrl": null,
                    "Env": "Production",
                    "ModifiedOn": "2026-11-11T09:07:07.000Z",
                    "PreviewUrl": "https://************************************************************************",
                    "ProjectId": "makers-ji9*********",
                    "RepoBranch": null,
                    "RepoCommitHash": "",
                    "RepoCommitMsg": null,
                    "Status": "Success",
                    "ViaMeta": "Upload"
                },
                "EnvVars": [],
                "Framework": null,
                "InstallCmd": null,
                "IsAgent": 0,
                "IsTld": 0,
                "ModifiedOn": "2026-11-11T09:06:45.114Z",
                "Name": "makers*******************************",
                "NodejsVersion": "22.11.0",
                "OutputDir": null,
                "PresetDomain": "makers******************************************************************",
                "PresetDomainStatus": "",
                "ProjectId": "makers-ji9*********",
                "Provider": "Upload",
                "Regions": null,
                "RepoBranch": null,
                "RepoName": null,
                "RepoOwner": null,
                "RepoPreBranches": null,
                "RepoUrl": null,
                "RootDir": null,
                "Status": "Normal",
                "ZoneId": "zone-3v5*********"
            }
        ],
        "TotalCount": 3,
        "RequestId": "b3ed47d5-b660-4f6c-b670-c2edd41a9173"
    }
}
```

