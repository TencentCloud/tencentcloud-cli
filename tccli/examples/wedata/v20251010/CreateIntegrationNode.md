**Example 1: 创建集成节点**



Input: 

```
tccli wedata CreateIntegrationNode --cli-unfold-argument  \
    --NodeInfo.Id 12323456 \
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
            "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed"
        },
        "RequestId": "75f7e8fd-9110-4e28-88d8-e801336d5de7"
    }
}
```

