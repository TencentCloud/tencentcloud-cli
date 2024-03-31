**Example 1: 更新集成任务**

更新集成任务

Input: 

```
tccli wedata ModifyIntegrationTask --cli-unfold-argument  \
    --TaskInfo.TaskName abc \
    --TaskInfo.Description abc \
    --TaskInfo.SyncType 0 \
    --TaskInfo.TaskType 0 \
    --TaskInfo.WorkflowId abc \
    --TaskInfo.TaskId abc \
    --TaskInfo.ScheduleTaskId abc \
    --TaskInfo.TaskGroupId abc \
    --TaskInfo.ProjectId abc \
    --TaskInfo.CreatorUin abc \
    --TaskInfo.OperatorUin abc \
    --TaskInfo.OwnerUin abc \
    --TaskInfo.AppId abc \
    --TaskInfo.Status 0 \
    --TaskInfo.Nodes.0.Id abc \
    --TaskInfo.Nodes.0.TaskId abc \
    --TaskInfo.Nodes.0.Name abc \
    --TaskInfo.Nodes.0.NodeType abc \
    --TaskInfo.Nodes.0.DataSourceType abc \
    --TaskInfo.Nodes.0.Description abc \
    --TaskInfo.Nodes.0.DatasourceId abc \
    --TaskInfo.Nodes.0.Config.0.Name abc \
    --TaskInfo.Nodes.0.Config.0.Value abc \
    --TaskInfo.Nodes.0.ExtConfig.0.Name abc \
    --TaskInfo.Nodes.0.ExtConfig.0.Value abc \
    --TaskInfo.Nodes.0.Schema.0.Id abc \
    --TaskInfo.Nodes.0.Schema.0.Name abc \
    --TaskInfo.Nodes.0.Schema.0.Value abc \
    --TaskInfo.Nodes.0.Schema.0.Type abc \
    --TaskInfo.Nodes.0.Schema.0.Properties.0.Name abc \
    --TaskInfo.Nodes.0.Schema.0.Properties.0.Value abc \
    --TaskInfo.Nodes.0.Schema.0.Alias abc \
    --TaskInfo.Nodes.0.Schema.0.Comment abc \
    --TaskInfo.Nodes.0.NodeMapping.SourceId abc \
    --TaskInfo.Nodes.0.NodeMapping.SinkId abc \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Id abc \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Name abc \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Value abc \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Type abc \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Alias abc \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Comment abc \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SourceSchemaId abc \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SinkSchemaId abc \
    --TaskInfo.Nodes.0.AppId abc \
    --TaskInfo.Nodes.0.ProjectId abc \
    --TaskInfo.Nodes.0.CreatorUin abc \
    --TaskInfo.Nodes.0.OperatorUin abc \
    --TaskInfo.Nodes.0.OwnerUin abc \
    --TaskInfo.Nodes.0.CreateTime abc \
    --TaskInfo.Nodes.0.UpdateTime abc \
    --TaskInfo.ExecutorId abc \
    --TaskInfo.Mappings.0.SourceId abc \
    --TaskInfo.Mappings.0.SinkId abc \
    --TaskInfo.Mappings.0.SourceSchema.0.Id abc \
    --TaskInfo.Mappings.0.SourceSchema.0.Name abc \
    --TaskInfo.Mappings.0.SourceSchema.0.Value abc \
    --TaskInfo.Mappings.0.SourceSchema.0.Type abc \
    --TaskInfo.Mappings.0.SourceSchema.0.Alias abc \
    --TaskInfo.Mappings.0.SourceSchema.0.Comment abc \
    --TaskInfo.Mappings.0.SchemaMappings.0.SourceSchemaId abc \
    --TaskInfo.Mappings.0.SchemaMappings.0.SinkSchemaId abc \
    --TaskInfo.TaskMode abc \
    --TaskInfo.Incharge abc \
    --TaskInfo.OfflineTaskAddEntity.WorkflowName abc \
    --TaskInfo.OfflineTaskAddEntity.DependencyWorkflow abc \
    --TaskInfo.OfflineTaskAddEntity.StartTime abc \
    --TaskInfo.OfflineTaskAddEntity.EndTime abc \
    --TaskInfo.OfflineTaskAddEntity.CycleType 1 \
    --TaskInfo.OfflineTaskAddEntity.CycleStep 1 \
    --TaskInfo.OfflineTaskAddEntity.DelayTime 1 \
    --TaskInfo.OfflineTaskAddEntity.CrontabExpression abc \
    --TaskInfo.OfflineTaskAddEntity.RetryWait 1 \
    --TaskInfo.OfflineTaskAddEntity.Retriable 1 \
    --TaskInfo.OfflineTaskAddEntity.TryLimit 1 \
    --TaskInfo.OfflineTaskAddEntity.RunPriority 1 \
    --TaskInfo.OfflineTaskAddEntity.ProductName abc \
    --TaskInfo.OfflineTaskAddEntity.SelfDepend 1 \
    --TaskInfo.OfflineTaskAddEntity.TaskAction abc \
    --TaskInfo.OfflineTaskAddEntity.ExecutionEndTime abc \
    --TaskInfo.OfflineTaskAddEntity.ExecutionStartTime abc \
    --TaskInfo.OfflineTaskAddEntity.TaskAutoSubmit True \
    --TaskInfo.OfflineTaskAddEntity.InstanceInitStrategy abc \
    --TaskInfo.ExecutorGroupName abc \
    --TaskInfo.InLongManagerUrl abc \
    --TaskInfo.InLongStreamId abc \
    --TaskInfo.InLongManagerVersion abc \
    --TaskInfo.DataProxyUrl abc \
    --TaskInfo.Submit True \
    --TaskInfo.InputDatasourceType abc \
    --TaskInfo.OutputDatasourceType abc \
    --TaskInfo.NumRecordsIn 0 \
    --TaskInfo.NumRecordsOut 0 \
    --TaskInfo.ReaderDelay 0 \
    --TaskInfo.NumRestarts 0 \
    --TaskInfo.CreateTime abc \
    --TaskInfo.UpdateTime abc \
    --TaskInfo.LastRunTime abc \
    --TaskInfo.StopTime abc \
    --TaskInfo.HasVersion True \
    --TaskInfo.Locked True \
    --TaskInfo.Locker abc \
    --TaskInfo.RunningCu 0 \
    --TaskInfo.TaskAlarmRegularList abc \
    --TaskInfo.SwitchResource 0 \
    --TaskInfo.ReadPhase 0 \
    --TaskInfo.InstanceVersion 0 \
    --TaskInfo.ArrangeSpaceTaskId abc \
    --TaskInfo.OfflineTaskStatus 0 \
    --ProjectId abc \
    --RollbackFlag True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "TaskId": "abc"
    }
}
```

