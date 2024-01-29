**Example 1: 自动解析上游依赖**

自动解析上游依赖

Input: 

```
tccli wedata AnalyzeDependentTasks --cli-unfold-argument  \
    --ProjectId abc \
    --AnalyzeTasks.0.TaskId abc \
    --AnalyzeTasks.0.TaskName abc \
    --AnalyzeTasks.0.ProjectId abc \
    --AnalyzeTasks.0.DatasourceId abc \
    --AnalyzeTasks.0.DatabaseName abc \
    --AnalyzeTasks.0.TableName abc \
    --AnalyzeTasks.0.TableGuid abc \
    --AnalyzeTasks.0.PartitionName abc \
    --AnalyzeTasks.0.TablePhysicalId abc
```

Output: 
```
{
    "Response": {
        "Error": {
            "Message": "ce",
            "Code": "FailedOperation"
        },
        "RequestId": "eteter"
    }
}
```

