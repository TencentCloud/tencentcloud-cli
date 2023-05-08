**Example 1: 更新集成任务**

更新集成任务

Input: 

```
tccli wedata ModifyIntegrationTask --cli-unfold-argument  \
    --ProjectId xx \
    --TaskInfo.TaskGroupId xx \
    --TaskInfo.Status 0 \
    --TaskInfo.WorkflowId xx \
    --TaskInfo.Description xx \
    --TaskInfo.CreatorUin xx \
    --TaskInfo.SyncType 0 \
    --TaskInfo.ProjectId xx \
    --TaskInfo.OwnerUin xx \
    --TaskInfo.ExecuteContext.0.Name xx \
    --TaskInfo.ExecuteContext.0.Value xx \
    --TaskInfo.ScheduleTaskId xx \
    --TaskInfo.TaskType 0 \
    --TaskInfo.AppId xx \
    --TaskInfo.ExecutorId xx \
    --TaskInfo.TaskId xx \
    --TaskInfo.OperatorUin xx \
    --TaskInfo.Nodes.0.NodeType xx \
    --TaskInfo.Nodes.0.Description xx \
    --TaskInfo.Nodes.0.CreatorUin xx \
    --TaskInfo.Nodes.0.DataSourceType xx \
    --TaskInfo.Nodes.0.ProjectId xx \
    --TaskInfo.Nodes.0.OwnerUin xx \
    --TaskInfo.Nodes.0.ExtConfig.0.Name xx \
    --TaskInfo.Nodes.0.ExtConfig.0.Value xx \
    --TaskInfo.Nodes.0.DatasourceId xx \
    --TaskInfo.Nodes.0.NodeMapping.SourceId xx \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SinkSchemaId xx \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SourceSchemaId xx \
    --TaskInfo.Nodes.0.NodeMapping.SinkId xx \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Type xx \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Id xx \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Value xx \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Name xx \
    --TaskInfo.Nodes.0.TaskId xx \
    --TaskInfo.Nodes.0.AppId xx \
    --TaskInfo.Nodes.0.Schema.0.Type xx \
    --TaskInfo.Nodes.0.Schema.0.Id xx \
    --TaskInfo.Nodes.0.Schema.0.Value xx \
    --TaskInfo.Nodes.0.Schema.0.Name xx \
    --TaskInfo.Nodes.0.Config.0.Name xx \
    --TaskInfo.Nodes.0.Config.0.Value xx \
    --TaskInfo.Nodes.0.Id xx \
    --TaskInfo.Nodes.0.OperatorUin xx \
    --TaskInfo.Nodes.0.Name xx \
    --TaskInfo.ExtConfig.0.Name xx \
    --TaskInfo.ExtConfig.0.Value xx \
    --TaskInfo.Config.0.Name xx \
    --TaskInfo.Config.0.Value xx \
    --TaskInfo.TaskName xx \
    --TaskInfo.Mappings.0.SourceId xx \
    --TaskInfo.Mappings.0.SchemaMappings.0.SinkSchemaId xx \
    --TaskInfo.Mappings.0.SchemaMappings.0.SourceSchemaId xx \
    --TaskInfo.Mappings.0.SinkId xx \
    --TaskInfo.Mappings.0.SourceSchema.0.Type xx \
    --TaskInfo.Mappings.0.SourceSchema.0.Id xx \
    --TaskInfo.Mappings.0.SourceSchema.0.Value xx \
    --TaskInfo.Mappings.0.SourceSchema.0.Name xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

