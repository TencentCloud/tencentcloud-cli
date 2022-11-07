**Example 1: CreateIntegrationNode**

创建集成节点

Input: 

```
tccli wedata CreateIntegrationNode --cli-unfold-argument  \
    --NodeInfo.NodeType xx \
    --NodeInfo.Description xx \
    --NodeInfo.CreatorUin xx \
    --NodeInfo.DataSourceType xx \
    --NodeInfo.ProjectId xx \
    --NodeInfo.OwnerUin xx \
    --NodeInfo.ExtConfig.0.Name xx \
    --NodeInfo.ExtConfig.0.Value xx \
    --NodeInfo.DatasourceId xx \
    --NodeInfo.NodeMapping.SourceId xx \
    --NodeInfo.NodeMapping.SchemaMappings.0.SinkSchemaId xx \
    --NodeInfo.NodeMapping.SchemaMappings.0.SourceSchemaId xx \
    --NodeInfo.NodeMapping.SinkId xx \
    --NodeInfo.NodeMapping.SourceSchema.0.Type xx \
    --NodeInfo.NodeMapping.SourceSchema.0.Id xx \
    --NodeInfo.NodeMapping.SourceSchema.0.Value xx \
    --NodeInfo.NodeMapping.SourceSchema.0.Name xx \
    --NodeInfo.TaskId xx \
    --NodeInfo.AppId xx \
    --NodeInfo.Schema.0.Type xx \
    --NodeInfo.Schema.0.Id xx \
    --NodeInfo.Schema.0.Value xx \
    --NodeInfo.Schema.0.Name xx \
    --NodeInfo.Config.0.Name xx \
    --NodeInfo.Config.0.Value xx \
    --NodeInfo.Id xx \
    --NodeInfo.OperatorUin xx \
    --NodeInfo.Name xx \
    --ProjectId xx \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "Id": "xx",
        "TaskId": "xx",
        "RequestId": "xx"
    }
}
```

