**Example 1: CreateWorkspaceByTemplate**

通过模板 ID 创建工作空间

Input: 

```
tccli cloudstudio CreateWorkspaceByTemplate --cli-unfold-argument  \
    --CloudStudioSessionTeam cloudstudio-devops \
    --TemplateId 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkspaceId": 26,
            "SpaceKey": "tfyiyw"
        },
        "RequestId": "26881c75-375d-48ad-9a24-7270176e4fab"
    }
}
```

