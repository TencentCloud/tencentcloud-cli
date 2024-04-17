**Example 1: 更新数据集成节点**

更新数据集成节点

Input: 

```
tccli wedata ModifyIntegrationNode --cli-unfold-argument  \
    --NodeInfo.Id 3039 \
    --NodeInfo.TaskId 20220331184313320 \
    --NodeInfo.Name mysql \
    --NodeInfo.NodeType OUTPUT \
    --NodeInfo.DataSourceType MYSQL \
    --NodeInfo.Description 描述 \
    --NodeInfo.DatasourceId 913032 \
    --NodeInfo.Config.0.Name isClean \
    --NodeInfo.Config.0.Value 0 \
    --NodeInfo.ExtConfig.0.Name x \
    --NodeInfo.ExtConfig.0.Value 269 \
    --NodeInfo.Schema.0.Id 913935552 \
    --NodeInfo.Schema.0.Name id \
    --NodeInfo.Schema.0.Value null \
    --NodeInfo.Schema.0.Type int \
    --NodeInfo.Schema.0.Properties.0.Name 111 \
    --NodeInfo.Schema.0.Properties.0.Value 1 \
    --NodeInfo.Schema.0.Alias id \
    --NodeInfo.Schema.0.Comment 主键ID \
    --NodeInfo.NodeMapping.SourceId 130973 \
    --NodeInfo.NodeMapping.SinkId 130972 \
    --NodeInfo.NodeMapping.SourceSchema.0.Id 517902752 \
    --NodeInfo.NodeMapping.SourceSchema.0.Name col1 \
    --NodeInfo.NodeMapping.SourceSchema.0.Value null \
    --NodeInfo.NodeMapping.SourceSchema.0.Type int(11) \
    --NodeInfo.NodeMapping.SourceSchema.0.Alias col1 \
    --NodeInfo.NodeMapping.SourceSchema.0.Comment 列名 \
    --NodeInfo.NodeMapping.SchemaMappings.0.SourceSchemaId 517902752 \
    --NodeInfo.NodeMapping.SchemaMappings.0.SinkSchemaId 756243136 \
    --NodeInfo.AppId 1257305158 \
    --NodeInfo.ProjectId 11022568003970304 \
    --NodeInfo.CreatorUin 100022744352 \
    --NodeInfo.OperatorUin 100022744352 \
    --NodeInfo.OwnerUin 100006908545 \
    --NodeInfo.CreateTime 2022-03-31 18:43:24 \
    --NodeInfo.UpdateTime 2022-03-31 18:43:24 \
    --ProjectId 11022568003970304 \
    --TaskType 202 \
    --TaskMode 2
```

Output: 
```
{
    "Response": {
        "Id": "1",
        "TaskId": "20230112170349643",
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

