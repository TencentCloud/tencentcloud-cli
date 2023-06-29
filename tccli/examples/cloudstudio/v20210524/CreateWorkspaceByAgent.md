**Example 1: CreateWorkspaceByAgent**



Input: 

```
tccli cloudstudio CreateWorkspaceByAgent --cli-unfold-argument  \
    --AgentSpaceDTO.RemotePort 22 \
    --AgentSpaceDTO.Name openapi_test_agent1 \
    --AgentSpaceDTO.RemoteUser root \
    --AgentSpaceDTO.RemoteHost 43.132.171.34 \
    --AgentSpaceDTO.ImageId 1 \
    --AgentSpaceDTO.ImageName Agent \
    --AgentSpaceDTO.WorkspaceVersion 2 \
    --AgentSpaceDTO.WorkspaceResourceDTO.NormalMemory 0 \
    --AgentSpaceDTO.WorkspaceResourceDTO.GpuNumber 0 \
    --AgentSpaceDTO.WorkspaceResourceDTO.SystemStorage 0 \
    --AgentSpaceDTO.WorkspaceResourceDTO.CpuCoreNumber 0 \
    --AgentSpaceDTO.WorkspaceResourceDTO.GpuMemory 0 \
    --AgentSpaceDTO.WorkspaceResourceDTO.UserStorage 0 \
    --AgentSpaceDTO.WorkspaceType NORMAL \
    --CloudStudioSessionTeam cloudstudio-devops
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateDate": "2022-06-15T11:39:49.087Z",
            "SpaceKey": "pmtoue",
            "WorkspaceId": 25
        },
        "RequestId": "2764d976-c5d5-482c-b22d-4f980b0dd980"
    }
}
```

