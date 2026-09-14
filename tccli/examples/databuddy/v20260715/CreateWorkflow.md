**Example 1: 创建携带python任务的工作流**

创建携带python任务的工作流

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --BaseInfo.WorkflowName *n**g*****n*pr** \
    --AdvanceConfig.QueuingMode OFF \
    --AdvanceConfig.MaxConcurrentNum 1 \
    --TaskList.0.TaskName py_0807 \
    --TaskList.0.TaskType.TaskTypeName PYTHON \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --TaskList.0.TaskType.RuntimePropertyList.0.PropertyKey ResourceMode \
    --TaskList.0.TaskType.RuntimePropertyList.0.PropertyValue 1 \
    --TaskList.0.ResourceGroupId res-ea***8f8 \
    --TaskList.0.DependOnRunCondition ALL_SUCCESS \
    --TaskList.0.LeftCoordinate 50 \
    --TaskList.0.TopCoordinate 50
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowId": "9a1670f3-14df-4869-9f38-ec31a4c4aac9"
        },
        "RequestId": "81772cad-5e71-4a7c-b063-a7b5db0d929a"
    }
}
```

