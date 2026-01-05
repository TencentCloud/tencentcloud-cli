**Example 1: 更新调度工作流任务部分属性**

更新调度工作流任务部分属性

Input: 

```
tccli wedata UpdateTriggerTaskPartially --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251124113217312 \
    --NewSetting.TriggerTaskBaseAttribute.TaskName gallop_workflow_task_test_down_part \
    --NewSetting.TriggerTaskBaseAttribute.TaskDescription update_desc_re \
    --NewSetting.TriggerTaskConfiguration.CodeContent IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKaGVsbG93b3JsZAo= \
    --NewSetting.TriggerTaskConfiguration.ResourceGroup 20240222212719833743 \
    --FieldToRemoveList TaskSchedulerConfiguration/UpstreamDependencyConfigList:20251121175713839
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "2826b14b-3a7a-43d5-aff2-5489928216b5"
    }
}
```

