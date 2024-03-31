**Example 1: 更新数据集成节点**

更新数据集成节点

Input: 

```
tccli wedata ModifyIntegrationNode --cli-unfold-argument  \
    --NodeInfo.Id abc \
    --NodeInfo.TaskId abc \
    --NodeInfo.Name abc \
    --NodeInfo.NodeType abc \
    --NodeInfo.DataSourceType abc \
    --NodeInfo.Description abc \
    --NodeInfo.DatasourceId abc \
    --NodeInfo.Config.0.Name abc \
    --NodeInfo.Config.0.Value abc \
    --NodeInfo.ExtConfig.0.Name abc \
    --NodeInfo.ExtConfig.0.Value abc \
    --NodeInfo.Schema.0.Id abc \
    --NodeInfo.Schema.0.Name abc \
    --NodeInfo.Schema.0.Value abc \
    --NodeInfo.Schema.0.Type abc \
    --NodeInfo.Schema.0.Properties.0.Name abc \
    --NodeInfo.Schema.0.Properties.0.Value abc \
    --NodeInfo.Schema.0.Alias abc \
    --NodeInfo.Schema.0.Comment abc \
    --NodeInfo.NodeMapping.SourceId abc \
    --NodeInfo.NodeMapping.SinkId abc \
    --NodeInfo.NodeMapping.SourceSchema.0.Id abc \
    --NodeInfo.NodeMapping.SourceSchema.0.Name abc \
    --NodeInfo.NodeMapping.SourceSchema.0.Value abc \
    --NodeInfo.NodeMapping.SourceSchema.0.Type abc \
    --NodeInfo.NodeMapping.SourceSchema.0.Alias abc \
    --NodeInfo.NodeMapping.SourceSchema.0.Comment abc \
    --NodeInfo.NodeMapping.SchemaMappings.0.SourceSchemaId abc \
    --NodeInfo.NodeMapping.SchemaMappings.0.SinkSchemaId abc \
    --NodeInfo.AppId abc \
    --NodeInfo.ProjectId abc \
    --NodeInfo.CreatorUin abc \
    --NodeInfo.OperatorUin abc \
    --NodeInfo.OwnerUin abc \
    --NodeInfo.CreateTime abc \
    --NodeInfo.UpdateTime abc \
    --ProjectId abc \
    --TaskType 1 \
    --TaskMode 1
```

Output: 
```
{
    "Response": {
        "Id": "abc",
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

