**Example 1: 成功**

成功

Input: 

```
tccli wedata ModifyTaskScriptDs --cli-unfold-argument  \
    --ProjectId abc \
    --TaskId abc \
    --ScriptContent abc \
    --IntegrationNodeDetails.0.Name abc \
    --IntegrationNodeDetails.0.NodeType abc \
    --IntegrationNodeDetails.0.DataSourceType abc \
    --IntegrationNodeDetails.0.Description abc \
    --IntegrationNodeDetails.0.DatasourceId abc \
    --IntegrationNodeDetails.0.Config.0.Name abc \
    --IntegrationNodeDetails.0.Config.0.Value abc \
    --IntegrationNodeDetails.0.ExtConfig.0.Name abc \
    --IntegrationNodeDetails.0.ExtConfig.0.Value abc \
    --IntegrationNodeDetails.0.Schema.0.Id abc \
    --IntegrationNodeDetails.0.Schema.0.Name abc \
    --IntegrationNodeDetails.0.Schema.0.Value abc \
    --IntegrationNodeDetails.0.Schema.0.Type abc \
    --IntegrationNodeDetails.0.Schema.0.Properties.0.Name abc \
    --IntegrationNodeDetails.0.Schema.0.Properties.0.Value abc \
    --IntegrationNodeDetails.0.Schema.0.Alias abc \
    --IntegrationNodeDetails.0.NodeMapping.SourceId abc \
    --IntegrationNodeDetails.0.NodeMapping.SinkId abc \
    --IntegrationNodeDetails.0.NodeMapping.SourceSchema.0.Id abc \
    --IntegrationNodeDetails.0.NodeMapping.SourceSchema.0.Name abc \
    --IntegrationNodeDetails.0.NodeMapping.SourceSchema.0.Value abc \
    --IntegrationNodeDetails.0.NodeMapping.SourceSchema.0.Type abc \
    --IntegrationNodeDetails.0.NodeMapping.SourceSchema.0.Alias abc \
    --IntegrationNodeDetails.0.NodeMapping.SchemaMappings.0.SourceSchemaId abc \
    --IntegrationNodeDetails.0.NodeMapping.SchemaMappings.0.SinkSchemaId abc \
    --IntegrationNodeDetails.0.OwnerUin abc
```

Output: 
```
{
    "Response": {
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

