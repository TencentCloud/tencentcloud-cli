**Example 1: 修改集成节点**



Input: 

```
tccli wedata UpdateIntegrationNode --cli-unfold-argument  \
    --NodeInfo.Id 1 \
    --NodeInfo.TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --NodeInfo.Name MySQL \
    --NodeInfo.NodeType INPUT \
    --NodeInfo.Description 读取 \
    --NodeInfo.ConnectionId 62274 \
    --NodeInfo.AppId 251436191 \
    --NodeInfo.WorkspaceId test-project-001 \
    --NodeInfo.OperatorUin 100028596846 \
    --NodeInfo.OwnerUin 100028596846 \
    --NodeInfo.Schema.0.Id 1 \
    --NodeInfo.Schema.0.Name id \
    --NodeInfo.Schema.0.Type int \
    --NodeInfo.Schema.0.Alias id \
    --WorkspaceId test-project-001
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": "1",
            "TaskId": ""
        },
        "RequestId": "16512914-7660-4a34-add6-ee2cfc71e8f7"
    }
}
```

