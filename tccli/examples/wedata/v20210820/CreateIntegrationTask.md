**Example 1: 创建集成任务**

创建集成任务

Input: 

```
tccli wedata CreateIntegrationTask --cli-unfold-argument  \
    --ProjectId 17865298918277529 \
    --TaskInfo.TaskGroupId i06c73547-eca5-4bc9-849d-b4bfaaf279 \
    --TaskInfo.Status 0 \
    --TaskInfo.WorkflowId 12345(仅离线任务填写) \
    --TaskInfo.Description 关于任务的自定义描述 \
    --TaskInfo.CreatorUin 100006386216 \
    --TaskInfo.SyncType 0 \
    --TaskInfo.ProjectId 17865298918277529 \
    --TaskInfo.OwnerUin 100006386216 \
    --TaskInfo.ExecuteContext.0.Name - \
    --TaskInfo.ExecuteContext.0.Value - \
    --TaskInfo.ScheduleTaskId 12345678 \
    --TaskInfo.TaskType 0 \
    --TaskInfo.AppId 57234323 \
    --TaskInfo.ExecutorId 1347534 \
    --TaskInfo.TaskId 015235-2adc2d-372dasd-5273 \
    --TaskInfo.OperatorUin 100006386235 \
    --TaskInfo.Nodes.0.NodeType INPUT \
    --TaskInfo.Nodes.0.Description test \
    --TaskInfo.Nodes.0.CreatorUin 100006386235 \
    --TaskInfo.Nodes.0.DataSourceType MYSQL \
    --TaskInfo.Nodes.0.ProjectId 17865298918277529 \
    --TaskInfo.Nodes.0.OwnerUin 100006386235 \
    --TaskInfo.Nodes.0.ExtConfig.0.Name test-name \
    --TaskInfo.Nodes.0.ExtConfig.0.Value test-value \
    --TaskInfo.Nodes.0.DatasourceId 1237582840 \
    --TaskInfo.Nodes.0.NodeMapping.SourceId 1 \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SinkSchemaId 2 \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SourceSchemaId 3 \
    --TaskInfo.Nodes.0.NodeMapping.SinkId 2 \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Type String \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Id 123 \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Value test \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Name name \
    --TaskInfo.Nodes.0.TaskId 015235-2adc2d-372dasd-5274 \
    --TaskInfo.Nodes.0.AppId 57234323 \
    --TaskInfo.Nodes.0.Schema.0.Type String \
    --TaskInfo.Nodes.0.Schema.0.Id 134 \
    --TaskInfo.Nodes.0.Schema.0.Value test2 \
    --TaskInfo.Nodes.0.Schema.0.Name name2 \
    --TaskInfo.Nodes.0.Config.0.Name config0 \
    --TaskInfo.Nodes.0.Config.0.Value value0 \
    --TaskInfo.Nodes.0.Id 123456 \
    --TaskInfo.Nodes.0.OperatorUin 100006386235 \
    --TaskInfo.Nodes.0.Name name \
    --TaskInfo.ExtConfig.0.Name name0 \
    --TaskInfo.ExtConfig.0.Value value0 \
    --TaskInfo.Config.0.Name config-name-0 \
    --TaskInfo.Config.0.Value config-value-09 \
    --TaskInfo.TaskName task-2 \
    --TaskInfo.Mappings.0.SourceId 1 \
    --TaskInfo.Mappings.0.SchemaMappings.0.SinkSchemaId 2 \
    --TaskInfo.Mappings.0.SchemaMappings.0.SourceSchemaId 3 \
    --TaskInfo.Mappings.0.SinkId 2 \
    --TaskInfo.Mappings.0.SourceSchema.0.Type String \
    --TaskInfo.Mappings.0.SourceSchema.0.Id 123 \
    --TaskInfo.Mappings.0.SourceSchema.0.Value test \
    --TaskInfo.Mappings.0.SourceSchema.0.Name name
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdefg-1234-32415-asd23f",
        "TaskId": "015235-2adc2d-372dasd-5274"
    }
}
```

