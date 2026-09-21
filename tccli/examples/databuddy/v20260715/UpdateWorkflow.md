**Example 1: 修改工作流Git信息**

修改工作流Git信息

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 8f760036-a086-49cd-9d20-7aa25c8a76be \
    --NewSetting.GitConfigId 1785920869632**** \
    --NewSetting.GitBranch main
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "bddfebb1-6ad0-482f-b21c-94bd5f2e7010"
    }
}
```

**Example 2: 更新工作流**



Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowId 8e0e3485-2736-4530-92ed-932e019898f1 \
    --NewSetting.TaskList.0.TaskName py_0807 \
    --NewSetting.TaskList.0.TaskType.TaskTypeName PYTHON \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyKey ResourceMode \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyValue 1 \
    --NewSetting.TaskList.0.ResourceGroupId res******8f8 \
    --NewSetting.TaskList.0.DependOnRunCondition ALL_SUCCESS \
    --NewSetting.TaskList.0.LeftCoordinate 50 \
    --NewSetting.TaskList.0.TopCoordinate 50
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "516da81c-51c7-4f90-9cad-8545fb200113"
    }
}
```

