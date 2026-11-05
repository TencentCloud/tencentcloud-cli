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

**Example 2: 利用FieldToRemoveList来删除工作流绑定的指定标签**

通过 FieldToRemoveList 删除本工作流绑定的指定标签，标签编号为通过GetWorkflow接口返回的Data.LabelList.LabelKeyId字段，值为6263的标签

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 27a49f96-004c-4438-bded-d21cb6892c8c \
    --FieldToRemoveList /LabelList:[6263]
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "ff01e545-dc82-4dc1-bedc-1244fbc8ff0d"
    }
}
```

**Example 3: 更新任务上游依赖（高级模式：任一条件满足）**

更新任务上游依赖，运行条件为高级模式（ADVANCED）：Operator=OR 表示配置的多个条件任一满足即触发；每个条件通过 UpstreamTaskId 指定上游任务、AllowedStates 指定其允许状态

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 562e7847-0499-4e61-89dd-085c9d7bfc2a \
    --NewSetting.TaskList.0.TaskId b8fa8f30-eee5-4c13-8577-99cad9d8c4f7 \
    --NewSetting.TaskList.0.DependOnList.0.TaskId 198ee412-8c01-4c4a-a65f-1348010691d0 \
    --NewSetting.TaskList.0.DependOnList.1.TaskId 3a6ff797-3d9c-4fa8-8fbd-2b5718e5fb94 \
    --NewSetting.TaskList.0.DependOnList.2.TaskId b4d825c4-15a7-484f-a783-a8f56697790f \
    --NewSetting.TaskList.0.DependOnRunCondition ADVANCED \
    --NewSetting.TaskList.0.AdvancedDependencyConfig.Operator OR \
    --NewSetting.TaskList.0.AdvancedDependencyConfig.Conditions.0.AllowedStates SUCCESS \
    --NewSetting.TaskList.0.AdvancedDependencyConfig.Conditions.0.UpstreamTaskId 198ee412-8c01-4c4a-a65f-1348010691d0 \
    --NewSetting.TaskList.0.AdvancedDependencyConfig.Conditions.1.AllowedStates SUCCESS \
    --NewSetting.TaskList.0.AdvancedDependencyConfig.Conditions.1.UpstreamTaskId 3a6ff797-3d9c-4fa8-8fbd-2b5718e5fb94 \
    --NewSetting.TaskList.0.AdvancedDependencyConfig.Conditions.2.AllowedStates FAILED \
    --NewSetting.TaskList.0.AdvancedDependencyConfig.Conditions.2.UpstreamTaskId b4d825c4-15a7-484f-a783-a8f56697790f
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "ffed021a-dbaf-4467-ac91-61d9bf16d3a0"
    }
}
```

**Example 4: 更新任务上游依赖，运行条件为简单模式：多个上游必须全部成功**

更新任务列表：通过 DependOnList 为指定任务设置多个上游依赖，并以 DependOnRunCondition 指定依赖运行条件为全部成功

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 562e7847-0499-4e61-89dd-085c9d7bfc2a \
    --NewSetting.TaskList.0.TaskId b8fa8f30-eee5-4c13-8577-99cad9d8c4f7 \
    --NewSetting.TaskList.0.DependOnList.0.TaskId 198ee412-8c01-4c4a-a65f-1348010691d0 \
    --NewSetting.TaskList.0.DependOnList.1.TaskId 3a6ff797-3d9c-4fa8-8fbd-2b5718e5fb94 \
    --NewSetting.TaskList.0.DependOnRunCondition ALL_SUCCESS
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "8d925c00-9612-4893-93ac-7603129c49db"
    }
}
```

**Example 5: 更新任务重试配置**

更新任务重试配置，开启任务失败重试、任务超时重试，最大重试2次，重试间隔5分钟

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 562e7847-0499-4e61-89dd-085c9d7bfc2a \
    --NewSetting.TaskList.0.TaskId 3a6ff797-3d9c-4fa8-8fbd-2b5718e5fb94 \
    --NewSetting.TaskList.0.TaskRetryStrategy.MaxRetryTimes 2 \
    --NewSetting.TaskList.0.TaskRetryStrategy.RetryBetweenWaitTime 5 \
    --NewSetting.TaskList.0.TaskRetryStrategy.RetryBetweenWaitTimeUnit MINUTE \
    --NewSetting.TaskList.0.TaskRetryStrategy.TaskRunFailureRetrySwitch True \
    --NewSetting.TaskList.0.TaskRetryStrategy.TaskRunTimeoutRetrySwitch True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "aa247320-7975-4bc2-bc38-19f7f61269ac"
    }
}
```

**Example 6: 更新工作流和任务告警与监控指标**

更新工作流和任务告警与监控指标，工作流设为监控指标告警，任务设为监控指标告警和失败告警

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 27a49f96-004c-4438-bded-d21cb6892c8c \
    --NewSetting.MonitorMetric.Metrics.0.MetricType RUN_DURATION \
    --NewSetting.MonitorMetric.Metrics.0.WarningThreshold 3600000 \
    --NewSetting.MonitorMetric.Metrics.0.TimeoutThreshold 7200000 \
    --NewSetting.MonitorMetric.AlarmMonitorType WORKFLOW \
    --NewSetting.Alarm.DoNotDisturbWhenSkipped False \
    --NewSetting.Alarm.AlarmMonitorType WORKFLOW \
    --NewSetting.Alarm.DoNotDisturbWhenManuallyTerminated False \
    --NewSetting.Alarm.DoNotDisturbUntilTheLastRetry False \
    --NewSetting.Alarm.AlarmGroups.0.ChannelId  \
    --NewSetting.Alarm.AlarmGroups.0.IsEmailChannel True \
    --NewSetting.Alarm.AlarmGroups.0.AlarmConditions MONITOR_INDICATOR_ALARM \
    --NewSetting.Alarm.AlarmGroups.0.ChannelName test_user@tencent.com \
    --NewSetting.Alarm.AlarmGroups.0.ChannelType 1 \
    --NewSetting.TaskList.0.Alarm.AlarmId 5e609d06-0dae-4358-9323-c8df6e0d51c2 \
    --NewSetting.TaskList.0.Alarm.DoNotDisturbWhenSkipped False \
    --NewSetting.TaskList.0.Alarm.AlarmMonitorType TASK \
    --NewSetting.TaskList.0.Alarm.DoNotDisturbWhenManuallyTerminated False \
    --NewSetting.TaskList.0.Alarm.DoNotDisturbUntilTheLastRetry False \
    --NewSetting.TaskList.0.Alarm.AlarmGroups.0.ChannelId  \
    --NewSetting.TaskList.0.Alarm.AlarmGroups.0.IsEmailChannel True \
    --NewSetting.TaskList.0.Alarm.AlarmGroups.0.AlarmConditions FAILURE MONITOR_INDICATOR_ALARM \
    --NewSetting.TaskList.0.Alarm.AlarmGroups.0.ChannelName test_user@tencent.com \
    --NewSetting.TaskList.0.Alarm.AlarmGroups.0.ChannelType 1 \
    --NewSetting.TaskList.0.TaskId 27c91337-cc90-468c-b014-5bfb694c21f8 \
    --NewSetting.TaskList.0.MonitorMetric.MonitorMetricId 1fab2ae1-d989-4202-9d3e-82a5387f83a4 \
    --NewSetting.TaskList.0.MonitorMetric.Metrics.0.MetricType RUN_DURATION \
    --NewSetting.TaskList.0.MonitorMetric.Metrics.0.WarningThreshold 600000 \
    --NewSetting.TaskList.0.MonitorMetric.Metrics.0.TimeoutThreshold 900000 \
    --NewSetting.TaskList.0.MonitorMetric.AlarmMonitorType TASK
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "7ee75c0d-8d2f-4d1a-a645-fd56a3b3d305"
    }
}
```

**Example 7: 更新工作流的调度配置：根据Cron表达式定时触发，并设定了有效期限**

更新工作流的调度配置：根据Cron表达式定时触发，并设定了有效期限。如果已经配置过调度，就需要从GetWorkflow接口返回的Data.Trigger.TriggerId进更新；否则无需传TriggerId

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 27a49f96-004c-4438-bded-d21cb6892c8c \
    --NewSetting.Trigger.0.TriggerId 410bc8b5-e3b6-4632-a0ba-5dae970c198a \
    --NewSetting.Trigger.0.SchedulerStatus ACTIVE \
    --NewSetting.Trigger.0.TriggerMode TIME_TRIGGER \
    --NewSetting.Trigger.0.SchedulerTimeZone Asia/Shanghai \
    --NewSetting.Trigger.0.StartTime 1793030400000 \
    --NewSetting.Trigger.0.EndTime 1824652799000 \
    --NewSetting.Trigger.0.ConfigMode CRON_EXPRESSION \
    --NewSetting.Trigger.0.CycleType CRONTAB_CYCLE \
    --NewSetting.Trigger.0.CrontabExpression 0 22 1,5 * * ?
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "46908688-b5bb-4950-91ae-fda715f886e0"
    }
}
```

**Example 8: 更新工作流的调度配置：根据日期时间定时触发，并设定了有效期限**

更新工作流的调度配置：每天 1 点执行定时触发，并设定了有效期限。如果已经配置过调度，就需要从GetWorkflow接口返回的Data.Trigger.TriggerId进更新；否则无需传TriggerId

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 27a49f96-004c-4438-bded-d21cb6892c8c \
    --NewSetting.Trigger.0.TriggerId 9acef20c-60dc-400b-a1bc-655a4a6afb45 \
    --NewSetting.Trigger.0.SchedulerStatus ACTIVE \
    --NewSetting.Trigger.0.TriggerMode TIME_TRIGGER \
    --NewSetting.Trigger.0.SchedulerTimeZone Asia/Shanghai \
    --NewSetting.Trigger.0.StartTime 1793030400000 \
    --NewSetting.Trigger.0.EndTime 1824652799000 \
    --NewSetting.Trigger.0.ConfigMode COMMON \
    --NewSetting.Trigger.0.CycleType DAY_CYCLE \
    --NewSetting.Trigger.0.CrontabExpression 0 0 1 * * ? *
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "14333b14-abfe-4914-b763-bff9fdcd35ca"
    }
}
```

**Example 9: 更新工作流，增加或修改一个标签**

更新工作流，增加或修改一个标签

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 27a49f96-004c-4438-bded-d21cb6892c8c \
    --NewSetting.LabelList.0.LabelKey label_test \
    --NewSetting.LabelList.0.LabelValue lv
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "dab4f7cc-9f26-4be4-b512-7ea2c57dfa5f"
    }
}
```

**Example 10: 更新工作流，增加或修改工作流参数**

更新工作流，增加或修改工作流参数

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 27a49f96-004c-4438-bded-d21cb6892c8c \
    --NewSetting.ParamList.0.ParamKey wp_1 \
    --NewSetting.ParamList.0.ParamValue wpv_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "3f767675-ba88-4338-9a9d-7d1470a5c351"
    }
}
```

**Example 11: 更新已存在JAR任务**

更新已存在JAR任务

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 37a8f5e9-abc9-4fdd-9ee7-26583df366a1 \
    --NewSetting.TaskList.0.DependOnList.0.TaskId 60e85209-3364-49ca-b46a-8d36b4a630ed \
    --NewSetting.TaskList.0.TaskId 5a60f483-fde8-4df3-8750-30ac09787a0d \
    --NewSetting.TaskList.0.TaskName test-11 \
    --NewSetting.TaskList.0.TaskType.TaskTypeName JAR \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyKey ResourceMode \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyValue 1 \
    --NewSetting.TaskList.0.ResourceGroupId res-c07a503e \
    --NewSetting.TaskList.0.Description  \
    --NewSetting.TaskList.0.TaskRetryStrategy.MaxRetryTimes 3 \
    --NewSetting.TaskList.0.TaskRetryStrategy.RetryBetweenWaitTime 5 \
    --NewSetting.TaskList.0.TaskRetryStrategy.RetryBetweenWaitTimeUnit MINUTE \
    --NewSetting.TaskList.0.TaskRetryStrategy.TaskRunFailureRetrySwitch True \
    --NewSetting.TaskList.0.TaskRetryStrategy.TaskRunTimeoutRetrySwitch False \
    --NewSetting.TaskList.0.DependOnRunCondition ALL_SUCCESS \
    --NewSetting.TaskList.0.LeftCoordinate 70 \
    --NewSetting.TaskList.0.TopCoordinate 182
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "ca485d4a-bfcb-45d2-8525-0f445c48311a"
    }
}
```

**Example 12: 更新已存在的Notebook任务**

更新已存在的Notebook任务（来源文件在工作空间），资源模式为单节点，Driver资源规格配置为small(1CU)

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 27a49f96-004c-4438-bded-d21cb6892c8c \
    --NewSetting.TaskList.0.TaskId 27c91337-cc90-468c-b014-5bfb694c21f8 \
    --NewSetting.TaskList.0.TaskType.TaskTypeName NOTEBOOK \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyKey ResourceMode \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyValue 2 \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.1.PropertyKey DriverCU \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.1.PropertyValue small
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "9a4d0cff-35d8-491d-9104-ee3bf0441db1"
    }
}
```

**Example 13: 更新已存在的Python任务的资源配置（来源文件在GIT）**

更新已存在的Python任务的资源配置（来源文件在GIT），资源模式单节点，资源配置改为medium(2CU)。

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId d940c85b-d5d0-4c26-96b2-eefe43e614cd \
    --NewSetting.TaskList.0.TaskId f3e88300-5cf5-4ec7-b3ef-4805b2650d94 \
    --NewSetting.TaskList.0.TaskType.TaskTypeName PYTHON \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyKey ResourceMode \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.0.PropertyValue 2 \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.1.PropertyKey DriverCU \
    --NewSetting.TaskList.0.TaskType.RuntimePropertyList.1.PropertyValue medium
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "13b44681-ecb0-48fb-b95e-e4b53aab9193"
    }
}
```

**Example 14: 更新已存在的Ray作业任务的来源文件（来源文件在工作空间）**

更新已存在的Ray作业任务的来源文件（来源文件在工作空间）

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 14ed60bb-0f1c-46ab-9d51-8cf6b17cfc73 \
    --NewSetting.TaskList.0.TaskId cab6b8e5-6e05-4304-b2b0-a5246ef38176 \
    --NewSetting.TaskList.0.TaskType.TaskTypeName RAY_JOB \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Entrypoint \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue cHl0aG9uIHNpbXBsZV90ZXN0LnB5 \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.1.PropertyKey JobConfig \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.1.PropertyValue eyJSZXNvdXJjZUNvbmZpZyI6IntcIkhlYWRcIjp7XCJOYW1lXCI6XCJIZWFkXCIsXCJSZXNvdXJjZVR5cGVcIjpcIkNQVVwiLFwiQmlsbGluZ0l0ZW1cIjpcInN2X2RsY19zdGFuZGFyZF9jdV9zdGFuZGFyZF9jdVwiLFwiU3BlY1wiOjEsXCJFbnZzXCI6W10sXCJMYWJlbHNcIjpbXSxcIkhpZ2hBdmFpbGFiaWxpdHlcIjpmYWxzZSxcIlBvZE51bVwiOjF9LFwiV29ya2VyXCI6W3tcIk5hbWVcIjpcIldvcmtlckdyb3VwMDFcIixcIlJlc291cmNlVHlwZVwiOlwiQ1BVXCIsXCJCaWxsaW5nSXRlbVwiOlwic3ZfZGxjX3N0YW5kYXJkX2N1X3N0YW5kYXJkX2N1XCIsXCJTcGVjXCI6MSxcIkVudnNcIjpbXSxcIkxhYmVsc1wiOltdLFwiTWluUG9kTnVtXCI6MSxcIk1heFBvZE51bVwiOjF9XX0iLCJJbWFnZSI6ImNjci5jY3MudGVuY2VudHl1bi5jb20vZW1yLWltYWdlL3RjcmF5OnRjcmF5Mi41Ny4wLXB5MzExLWNwdSIsIkltYWdlUHVsbFR5cGUiOiJCdWlsdGluIn0= \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.2.PropertyKey Source \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.2.PropertyValue 5 \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.3.PropertyKey JobPackage \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.3.PropertyValue /Workspace/jonsljiang/simple_test 2.py \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.4.PropertyKey WorkspaceEntryType \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.4.PropertyValue FILE \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.5.PropertyKey RunMode \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.5.PropertyValue SERVERLESS
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "3729bcd8-6e3b-4b41-a49e-cdba3180a153"
    }
}
```

**Example 15: 更新已存在的SQL任务的来源文件（来源文件在工作空间）**

更新已存在的SQL任务的来源文件（来源文件在工作空间）

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 0612a7de-b5f1-4348-8f44-d090ae69df35 \
    --NewSetting.TaskList.0.TaskId f3be8a4a-ab45-4ee3-b981-a3eb399af042 \
    --NewSetting.TaskList.0.TaskType.TaskTypeName SQL \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.1.PropertyKey CodeFileId \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.1.PropertyValue 798545986376953856
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "35fb1b9c-4c2d-42c2-ab21-cb996c589b31"
    }
}
```

**Example 16: 更新排队模式+设置工作流运行最大并发数**

更新工作流排队模式：开启工作流排队且工作流最大并发设置为 5

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowId 9a1670f3-14df-4869-9f38-ec31a4c4aac9 \
    --NewSetting.AdvanceConfig.QueuingMode ON \
    --NewSetting.AdvanceConfig.MaxConcurrentNum 5
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "81772cad-5e71-4a7c-b063-a7b5db0d929a"
    }
}
```

**Example 17: 更新已存在的依赖检查节点任务**

更新已存在的依赖检查节点任务

Input: 

```
tccli databuddy UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 37a8f5e9-abc9-4fdd-9ee7-26583df366a1 \
    --FieldToRemoveList /TaskList:[d8bc6f84-bbd5-4e87-b80a-e9ab58975841]/MonitorMetric:[0f8c423b-0bb6-48d1-a95f-97c9147abea8]/Metrics \
    --NewSetting.TaskList.0.TaskId d8bc6f84-bbd5-4e87-b80a-e9ab58975841 \
    --NewSetting.TaskList.0.TaskName test-12 \
    --NewSetting.TaskList.0.TaskType.TaskTypeName DEPENDENCY_SENSOR \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey checkIntervalSeconds \
    --NewSetting.TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 10 \
    --NewSetting.TaskList.0.Description  \
    --NewSetting.TaskList.0.MonitorMetric.MonitorMetricId 0f8c423b-0bb6-48d1-a95f-97c9147abea8 \
    --NewSetting.TaskList.0.MonitorMetric.AlarmMonitorType TASK \
    --NewSetting.TaskList.0.MonitorMetric.Metrics.0.MetricType RUN_DURATION \
    --NewSetting.TaskList.0.MonitorMetric.Metrics.0.WarningThreshold 21600000 \
    --NewSetting.TaskList.0.MonitorMetric.Metrics.0.TimeoutThreshold 21600000 \
    --NewSetting.TaskList.0.TaskRetryStrategy.MaxRetryTimes 3 \
    --NewSetting.TaskList.0.TaskRetryStrategy.RetryBetweenWaitTime 5 \
    --NewSetting.TaskList.0.TaskRetryStrategy.RetryBetweenWaitTimeUnit MINUTE \
    --NewSetting.TaskList.0.TaskRetryStrategy.TaskRunFailureRetrySwitch True \
    --NewSetting.TaskList.0.TaskRetryStrategy.TaskRunTimeoutRetrySwitch False \
    --NewSetting.TaskList.0.DependOnRunCondition ALL_SUCCESS \
    --NewSetting.TaskList.0.LeftCoordinate 410 \
    --NewSetting.TaskList.0.TopCoordinate 32
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "fdc3beb7-ee94-47b8-a162-129d2388a0fc"
    }
}
```

