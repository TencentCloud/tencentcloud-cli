**Example 1: 创建项目**



Input: 

```
tccli makers CreateProject --cli-unfold-argument  \
    --ZoneId zone-************ \
    --Name ************* \
    --Channel Custom \
    --Provider Upload \
    --Source capi-selftest \
    --Area overseas \
    --NodeJsVersion 20.18.0 \
    --RootDir / \
    --OutputDir dist \
    --BuildCmd npm run build \
    --InstallCmd npm install \
    --Framework Other \
    --TemplateId tpl-demo \
    --RepoUrl https://*********************** \
    --RepoOwner example \
    --RepoName demo \
    --RepoBranch main \
    --Namespace demo \
    --CodingProjectId 1
```

Output: 
```
{
    "Response": {
        "ProjectId": "makers-************",
        "RequestId": "c8ce425a-6e77-485f-b56d-c538a2ea28b5"
    }
}
```

