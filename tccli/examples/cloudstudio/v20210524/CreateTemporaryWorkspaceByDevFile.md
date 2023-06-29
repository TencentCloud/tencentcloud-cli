**Example 1: 通过 devfile 查询或创建临时工作空间**

通过 devfile 查询或创建临时工作空间

Input: 

```
tccli cloudstudio CreateTemporaryWorkspaceByDevFile --cli-unfold-argument  \
    --Name test-x2 \
    --Tags Node.js \
    --Image cloudstudio-devops-docker.pkg.coding.net/artifacts/standard.container/workspace-ubuntu-focal-amd64:20221124.1 \
    --LifeCycle.Init.0.Name init \
    --LifeCycle.Init.0.Command echo 'init workspace' \
    --LifeCycle.Start.0.Name start \
    --LifeCycle.Start.0.Command echo 'start workspace' \
    --LifeCycle.Destroy.0.Name stop \
    --LifeCycle.Destroy.0.Command echo 'stop workspace' \
    --Repository  \
    --Ref main
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateDate": "2023-03-07T04:15:49.732+00:00",
            "SpaceKey": "mfhiaj",
            "WorkspaceId": 924
        },
        "RequestId": "4dceb4f5-11b8-4234-8dec-76d4da0857a3"
    }
}
```

