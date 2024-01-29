**Example 1: 失败**

失败

Input: 

```
tccli wedata BatchCreateVirtualTaskDs --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --Tasks.0.TaskId 20230516193558842 \
    --Tasks.0.TaskName quinnzhu \
    --Tasks.0.WorkflowId e36dadbf-ebb3-11ed-8909-bc97e105ba60 \
    --Tasks.0.ProjectId 1470547050521227264 \
    --Tasks.0.LeftCoordinate 1 \
    --Tasks.0.TopCoordinate 1 \
    --WorkflowId e36dadbf-ebb3-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorDesc": "任务quinnzhu(20230516193558842)位于当前工作流e36dadbf-ebb3-11ed-8909-bc97e105ba60中",
            "ErrorId": "quinnzhu(20230516193558842)",
            "Result": false
        },
        "RequestId": "ca945e69-8d2a-47ec-889b-34584d901d65"
    }
}
```

**Example 2: 成功**

成功

Input: 

```
tccli wedata BatchCreateVirtualTaskDs --cli-unfold-argument  \
    --ProjectId abc \
    --Tasks.0.TaskId abc \
    --Tasks.0.TaskName abc \
    --Tasks.0.WorkflowId abc \
    --Tasks.0.ProjectId abc \
    --Tasks.0.LeftCoordinate 0 \
    --Tasks.0.TopCoordinate 0 \
    --WorkflowId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "ErrorId": "abc",
            "ErrorDesc": "abc"
        },
        "RequestId": "abc"
    }
}
```

