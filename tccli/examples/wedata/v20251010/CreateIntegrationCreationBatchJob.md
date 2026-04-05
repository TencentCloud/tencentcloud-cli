**Example 1: 批量创建离线集成作业**



Input: 

```
tccli wedata CreateIntegrationCreationBatchJob --cli-unfold-argument  \
    --WorkspaceId test_project_batch_002 \
    --BatchJobInfo.BatchJobName 测试批量作业-包含任务 \
    --BatchJobInfo.Description 批量创建任务-包含2个同步任务 \
    --BatchJobInfo.SourceType MYSQL \
    --BatchJobInfo.SourceInstanceId source_instance_002 \
    --BatchJobInfo.SinkType TCLAKE \
    --BatchJobInfo.SinkInstanceId sink_instance_002 \
    --BatchJobInfo.TaskInfos.0.SourceDatabase source_db1 \
    --BatchJobInfo.TaskInfos.0.SourceTableName table1 \
    --BatchJobInfo.TaskInfos.0.SourceColumn.0.Id 1 \
    --BatchJobInfo.TaskInfos.0.SourceColumn.0.Name id \
    --BatchJobInfo.TaskInfos.0.SourceColumn.0.Type int \
    --BatchJobInfo.TaskInfos.0.SinkDatabase sink_db1 \
    --BatchJobInfo.TaskInfos.0.SinkTableName table1 \
    --BatchJobInfo.TaskInfos.0.SinkColumn.0.Id 1 \
    --BatchJobInfo.TaskInfos.0.SinkColumn.0.Name id \
    --BatchJobInfo.TaskInfos.0.SinkColumn.0.Type int \
    --BatchJobInfo.TaskInfos.0.ColumnMappingType 2 \
    --BatchJobInfo.TaskInfos.0.SchemaMappings.0.SourceSchemaId 1 \
    --BatchJobInfo.TaskInfos.0.SchemaMappings.0.SinkSchemaId 1 \
    --BatchJobInfo.TaskInfos.0.ExecutorGroupId executor_group_id \
    --BatchJobInfo.UserUinInCharge 700002164618
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": "beb23b934-4c76-4c21-81aa-e9841236c38e"
        },
        "RequestId": "c6a1f428-348c-415e-86c4-f5a5b76ed0e2"
    }
}
```

