**Example 1: 创建构建**



Input: 

```
tccli makers CreateDeployment --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --ViaMeta Upload \
    --Env Production \
    --Provider Upload \
    --DistType Folder \
    --TempBucketPath *************************************** \
    --RepoBranch main \
    --RepoCommitHash abc1234 \
    --RepoCommitMsg docs example \
    --BuildFrom Upload \
    --TemplateId tpl-demo \
    --CiSpec default
```

Output: 
```
{
    "Response": {
        "DeploymentId": "************",
        "RequestId": "7f059411-b286-47bf-a306-d18c2bea4034"
    }
}
```

