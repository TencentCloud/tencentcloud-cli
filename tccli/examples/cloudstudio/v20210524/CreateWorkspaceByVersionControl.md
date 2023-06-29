**Example 1: CreateWorkspaceByVersionControl**



Input: 

```
tccli cloudstudio CreateWorkspaceByVersionControl --cli-unfold-argument  \
    --CloudStudioSessionTeam xx \
    --WorkspaceDTO.VersionControlType xx \
    --WorkspaceDTO.Name xx \
    --WorkspaceDTO.VersionControlRefType xx \
    --WorkspaceDTO.InitializeStatus 0 \
    --WorkspaceDTO.VersionControlUrl xx \
    --WorkspaceDTO.ImageId 46749 \
    --WorkspaceDTO.SnapshotUid xx \
    --WorkspaceDTO.ImageName All in One \
    --WorkspaceDTO.WorkspaceVersion 0 \
    --WorkspaceDTO.WorkspaceResourceDTO.NormalMemory 0 \
    --WorkspaceDTO.WorkspaceResourceDTO.GpuNumber 0 \
    --WorkspaceDTO.WorkspaceResourceDTO.SystemStorage 0 \
    --WorkspaceDTO.WorkspaceResourceDTO.CpuCoreNumber 0 \
    --WorkspaceDTO.WorkspaceResourceDTO.GpuMemory 0 \
    --WorkspaceDTO.WorkspaceResourceDTO.UserStorage 0 \
    --WorkspaceDTO.TemplateId 0 \
    --WorkspaceDTO.VersionControlRef xx \
    --WorkspaceDTO.PriceId 0 \
    --WorkspaceDTO.Description xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateDate": "2020-09-22T00:00:00+00:00",
            "WorkspaceId": 0,
            "SpaceKey": "xx"
        },
        "RequestId": "xx"
    }
}
```

