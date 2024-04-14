**Example 1: 更新集成任务**

更新集成任务

Input: 

```
tccli wedata ModifyIntegrationTask --cli-unfold-argument  \
    --TaskInfo.TaskName testtaskname \
    --TaskInfo.Description testdesc \
    --TaskInfo.SyncType 2 \
    --TaskInfo.TaskType 202 \
    --TaskInfo.WorkflowId  \
    --TaskInfo.TaskId n11a6d01c-0ec6-4efc-bd14-97a921d01d3f \
    --TaskInfo.ScheduleTaskId cql-hjlx38yl \
    --TaskInfo.TaskGroupId a5d814828-452c-46f6-b128-19c1a3249bf0 \
    --TaskInfo.ProjectId 1486446569620893696 \
    --TaskInfo.CreatorUin 100022187073 \
    --TaskInfo.OperatorUin 100022187073 \
    --TaskInfo.OwnerUin 100022187073 \
    --TaskInfo.AppId 1257305888 \
    --TaskInfo.Status 3 \
    --TaskInfo.Nodes.0.Id 130973 \
    --TaskInfo.Nodes.0.TaskId n11a6d01c-0ec6-4efc-bd14-97a921d01d3f \
    --TaskInfo.Nodes.0.Name nodeTestName \
    --TaskInfo.Nodes.0.NodeType INPUT \
    --TaskInfo.Nodes.0.DataSourceType MYSQL \
    --TaskInfo.Nodes.0.Description testdesc \
    --TaskInfo.Nodes.0.DatasourceId 914840 \
    --TaskInfo.Nodes.0.Config.0.Name Type \
    --TaskInfo.Nodes.0.Config.0.Value MYSQL \
    --TaskInfo.Nodes.0.Config.1.Name splitPk \
    --TaskInfo.Nodes.0.Config.1.Value id \
    --TaskInfo.Nodes.0.Config.2.Name Database \
    --TaskInfo.Nodes.0.Config.2.Value databasetestname \
    --TaskInfo.Nodes.0.Config.3.Name TableNames \
    --TaskInfo.Nodes.0.Config.3.Value tabletestname \
    --TaskInfo.Nodes.0.Config.4.Name PrimaryKey \
    --TaskInfo.Nodes.0.Config.4.Value id \
    --TaskInfo.Nodes.0.Config.5.Name isNew \
    --TaskInfo.Nodes.0.Config.5.Value true \
    --TaskInfo.Nodes.0.Config.6.Name PrimaryKey_INPUT_SYMBOL \
    --TaskInfo.Nodes.0.Config.6.Value input \
    --TaskInfo.Nodes.0.Config.7.Name splitPk_INPUT_SYMBOL \
    --TaskInfo.Nodes.0.Config.7.Value input \
    --TaskInfo.Nodes.0.Config.8.Name isClean \
    --TaskInfo.Nodes.0.Config.8.Value 0 \
    --TaskInfo.Nodes.0.Config.9.Name encoding \
    --TaskInfo.Nodes.0.Config.9.Value utf-8 \
    --TaskInfo.Nodes.0.ExtConfig.0.Name x \
    --TaskInfo.Nodes.0.ExtConfig.0.Value 300 \
    --TaskInfo.Nodes.0.ExtConfig.1.Name y \
    --TaskInfo.Nodes.0.ExtConfig.1.Value 260 \
    --TaskInfo.Nodes.0.ExtConfig.2.Name iconPosition \
    --TaskInfo.Nodes.0.ExtConfig.2.Value left \
    --TaskInfo.Nodes.0.ExtConfig.3.Name size \
    --TaskInfo.Nodes.0.ExtConfig.3.Value m \
    --TaskInfo.Nodes.0.Schema.0.Type String \
    --TaskInfo.Nodes.0.Schema.0.Alias name \
    --TaskInfo.Nodes.0.Schema.0.Comment 名字 \
    --TaskInfo.Nodes.0.Schema.0.Id 616042880 \
    --TaskInfo.Nodes.0.Schema.0.Name name \
    --TaskInfo.Nodes.0.Schema.0.Properties.0.Name exttestname \
    --TaskInfo.Nodes.0.Schema.0.Properties.0.Value exttestvalue \
    --TaskInfo.Nodes.0.NodeMapping.SourceId 130973 \
    --TaskInfo.Nodes.0.NodeMapping.SinkId 130972 \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Id 597853056 \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Name name \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Value test \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Type String \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Alias name \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Comment 名称 \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Properties.0.Name exttestname \
    --TaskInfo.Nodes.0.NodeMapping.SourceSchema.0.Properties.0.Value exttestvalue \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SourceSchemaId 597853056 \
    --TaskInfo.Nodes.0.NodeMapping.SchemaMappings.0.SinkSchemaId 616042880 \
    --TaskInfo.Nodes.0.AppId 1315051999 \
    --TaskInfo.Nodes.0.ProjectId 1486446569620893696 \
    --TaskInfo.Nodes.0.CreatorUin 100028644005 \
    --TaskInfo.Nodes.0.OperatorUin 100028644005 \
    --TaskInfo.Nodes.0.OwnerUin 100028644005 \
    --TaskInfo.Nodes.0.CreateTime 2022-05-07 10:13:21 \
    --TaskInfo.Nodes.0.UpdateTime 2022-05-07 10:13:21 \
    --TaskInfo.ExecutorId 20220331190555092303 \
    --TaskInfo.Mappings.0.SourceId 130973 \
    --TaskInfo.Mappings.0.SinkId 130972 \
    --TaskInfo.Mappings.0.SourceSchema.0.Id 597853056 \
    --TaskInfo.Mappings.0.SourceSchema.0.Name name \
    --TaskInfo.Mappings.0.SourceSchema.0.Value test \
    --TaskInfo.Mappings.0.SourceSchema.0.Type String \
    --TaskInfo.Mappings.0.SourceSchema.0.Alias name \
    --TaskInfo.Mappings.0.SourceSchema.0.Comment 名称 \
    --TaskInfo.Mappings.0.SourceSchema.0.Properties.0.Name exttestname \
    --TaskInfo.Mappings.0.SourceSchema.0.Properties.0.Value exttestvalue \
    --TaskInfo.Mappings.0.SchemaMappings.0.SourceSchemaId 597853056 \
    --TaskInfo.Mappings.0.SchemaMappings.0.SinkSchemaId 616042880 \
    --TaskInfo.TaskMode 1 \
    --TaskInfo.Incharge 100028625403 \
    --TaskInfo.OfflineTaskAddEntity.WorkflowName  \
    --TaskInfo.OfflineTaskAddEntity.DependencyWorkflow  \
    --TaskInfo.OfflineTaskAddEntity.StartTime 2024-04-10 00:00:00 \
    --TaskInfo.OfflineTaskAddEntity.EndTime 2099-12-31 00:00:00 \
    --TaskInfo.OfflineTaskAddEntity.CycleType 1 \
    --TaskInfo.OfflineTaskAddEntity.CycleStep 5 \
    --TaskInfo.OfflineTaskAddEntity.DelayTime 0 \
    --TaskInfo.OfflineTaskAddEntity.CrontabExpression  \
    --TaskInfo.OfflineTaskAddEntity.RetryWait 3 \
    --TaskInfo.OfflineTaskAddEntity.Retriable 1 \
    --TaskInfo.OfflineTaskAddEntity.TryLimit 3 \
    --TaskInfo.OfflineTaskAddEntity.RunPriority 6 \
    --TaskInfo.OfflineTaskAddEntity.ProductName DATA_INTEGRATION \
    --TaskInfo.OfflineTaskAddEntity.SelfDepend 3 \
    --TaskInfo.OfflineTaskAddEntity.TaskAction  \
    --TaskInfo.OfflineTaskAddEntity.ExecutionEndTime 23:59 \
    --TaskInfo.OfflineTaskAddEntity.ExecutionStartTime 00:00 \
    --TaskInfo.OfflineTaskAddEntity.TaskAutoSubmit True \
    --TaskInfo.OfflineTaskAddEntity.InstanceInitStrategy T+0 \
    --TaskInfo.ExecutorGroupName 资源组01 \
    --TaskInfo.InLongManagerUrl 172.16.64.68:8083 \
    --TaskInfo.InLongStreamId f8317843e-68f9-4373-914f-241d7200a9a4 \
    --TaskInfo.InLongManagerVersion v17 \
    --TaskInfo.DataProxyUrl 172.16.64.68:8086 \
    --TaskInfo.Submit True \
    --TaskInfo.InputDatasourceType MYSQL \
    --TaskInfo.OutputDatasourceType DLC \
    --TaskInfo.NumRecordsIn 1000 \
    --TaskInfo.NumRecordsOut 1000 \
    --TaskInfo.ReaderDelay 5.0 \
    --TaskInfo.NumRestarts 2 \
    --TaskInfo.CreateTime 2022-05-07 10:13:21 \
    --TaskInfo.UpdateTime 2022-05-07 10:13:21 \
    --TaskInfo.LastRunTime 2022-05-07 10:13:21 \
    --TaskInfo.StopTime 2022-05-07 10:13:21 \
    --TaskInfo.HasVersion True \
    --TaskInfo.Locked True \
    --TaskInfo.Locker 100022187073 \
    --TaskInfo.RunningCu 2.0 \
    --TaskInfo.TaskAlarmRegularList 1769,1768 \
    --TaskInfo.SwitchResource 1 \
    --TaskInfo.ReadPhase 0 \
    --TaskInfo.InstanceVersion 12 \
    --TaskInfo.ArrangeSpaceTaskId 20230112170349643 \
    --TaskInfo.OfflineTaskStatus 1 \
    --ProjectId 1486446569620893696 \
    --RollbackFlag False
```

Output: 
```
{
    "Response": {
        "RequestId": "3508f999-0ee0-43b9-9ee3-542bfbf6559a",
        "TaskId": "n11a6d01c-0ec6-4efc-bd14-97a921d01d3f"
    }
}
```

