**Example 1: CreateIntegrationNode**

创建集成节点

Input: 

```
tccli wedata CreateIntegrationNode --cli-unfold-argument  \
    --NodeInfo.NodeType INPUT \
    --NodeInfo.Description test \
    --NodeInfo.CreatorUin 100006386216 \
    --NodeInfo.DataSourceType MYSQL \
    --NodeInfo.ProjectId 17865298918277529 \
    --NodeInfo.OwnerUin 100006386216 \
    --NodeInfo.ExtConfig.0.Name test-name \
    --NodeInfo.ExtConfig.0.Value test-value \
    --NodeInfo.DatasourceId 1 \
    --NodeInfo.NodeMapping.SourceId 1 \
    --NodeInfo.NodeMapping.SchemaMappings.0.SinkSchemaId 2 \
    --NodeInfo.NodeMapping.SchemaMappings.0.SourceSchemaId 3 \
    --NodeInfo.NodeMapping.SinkId 2 \
    --NodeInfo.NodeMapping.SourceSchema.0.Type String \
    --NodeInfo.NodeMapping.SourceSchema.0.Id 123 \
    --NodeInfo.NodeMapping.SourceSchema.0.Value test \
    --NodeInfo.NodeMapping.SourceSchema.0.Name name \
    --NodeInfo.TaskId 015235-2adc2d-372dasd-5274 \
    --NodeInfo.AppId 57234323 \
    --NodeInfo.Schema.0.Type String \
    --NodeInfo.Schema.0.Id 134 \
    --NodeInfo.Schema.0.Value test2 \
    --NodeInfo.Schema.0.Name name2 \
    --NodeInfo.Config.0.Name config0 \
    --NodeInfo.Config.0.Value value0 \
    --NodeInfo.Id 123456 \
    --NodeInfo.OperatorUin 100006386235 \
    --NodeInfo.Name name \
    --ProjectId 17865298918277529 \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "Id": "134",
        "TaskId": "015235-2adc2d-372dasd-5274",
        "RequestId": "1234-adfasd-2342-ssd"
    }
}
```

