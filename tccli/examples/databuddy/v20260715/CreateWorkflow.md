**Example 1: 创建Cron定时调度的工作流（含参数/标签/监控告警/Git/排队并发，不含任务）**

创建不含任务的工作流，配置 Cron 表达式定时调度（每天 0 点、Asia/Shanghai、含起止有效期）、工作流参数与标签、运行时长监控指标与告警、Git 仓库关联及排队模式（最大并发 2）

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --BaseInfo.WorkflowName test_workflow_1030 \
    --Trigger.0.StartTime 1793203200000 \
    --Trigger.0.EndTime 1824815014000 \
    --Trigger.0.TriggerMode TIME_TRIGGER \
    --Trigger.0.ConfigMode CRON_EXPRESSION \
    --Trigger.0.SchedulerStatus ACTIVE \
    --Trigger.0.CrontabExpression 0 0 0 * * ? * \
    --Trigger.0.SchedulerTimeZone Asia/Shanghai \
    --Trigger.0.CycleType CRONTAB_CYCLE \
    --ParamList.0.ParamKey wp1 \
    --ParamList.0.ParamValue wpv1 \
    --ParamList.1.ParamKey wp2 \
    --ParamList.1.ParamValue wpv2 \
    --LabelList.0.LabelKey lb_test1 \
    --LabelList.0.LabelValue lbv1 \
    --LabelList.1.LabelKey lb_test2 \
    --LabelList.1.LabelValue lbv2 \
    --MonitorMetric.Metrics.0.MetricType RUN_DURATION \
    --MonitorMetric.Metrics.0.WarningThreshold 3600000 \
    --MonitorMetric.Metrics.0.TimeoutThreshold 5400000 \
    --MonitorMetric.AlarmMonitorType WORKFLOW \
    --Alarm.AlarmGroups.0.ChannelId  \
    --Alarm.AlarmGroups.0.ChannelName xxx@yyy.com \
    --Alarm.AlarmGroups.0.IsEmailChannel True \
    --Alarm.AlarmGroups.0.ChannelType 1 \
    --Alarm.AlarmGroups.0.AlarmConditions FAILURE MONITOR_INDICATOR_ALARM \
    --Alarm.AlarmMonitorType WORKFLOW \
    --Alarm.DoNotDisturbWhenSkipped False \
    --Alarm.DoNotDisturbWhenManuallyTerminated False \
    --Alarm.DoNotDisturbUntilTheLastRetry False \
    --GitConfigId 17879110044139837 \
    --GitBranch main \
    --AdvanceConfig.QueuingMode ON \
    --AdvanceConfig.MaxConcurrentNum 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowId": "2b938d4c-2493-4676-ba1a-91d4e60a739a"
        },
        "RequestId": "185e832a-49cd-400e-8366-a9f2eb6e72b4"
    }
}
```

**Example 2: 创建完整配置的工作流（参数/标签/告警/监控/排队）**

创建包含工作流参数、标签、邮件告警、监控指标、排队模式等完整配置的工作流

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --BaseInfo.WorkflowName dwd_full_config_workflow \
    --BaseInfo.OwnerUserName tom \
    --ParamList.0.ParamKey ds \
    --ParamList.0.ParamValue ${yyyy-MM-dd} \
    --LabelList.0.LabelKey department \
    --LabelList.0.LabelValue sales \
    --Alarm.AlarmMonitorType WORKFLOW \
    --Alarm.AlarmGroups.0.ChannelId f4ec3e79-7368-44c9-8b04-031fad7f1a76 \
    --Alarm.AlarmGroups.0.ChannelName alarm@example.com \
    --Alarm.AlarmGroups.0.IsEmailChannel True \
    --Alarm.AlarmGroups.0.AlarmConditions START FAILURE \
    --Alarm.AlarmGroups.0.ChannelType 1 \
    --Alarm.DoNotDisturbWhenSkipped False \
    --Alarm.DoNotDisturbWhenManuallyTerminated False \
    --Alarm.DoNotDisturbUntilTheLastRetry False \
    --MonitorMetric.AlarmMonitorType WORKFLOW \
    --MonitorMetric.Metrics.0.MetricType RUN_DURATION \
    --MonitorMetric.Metrics.0.WarningThreshold 3600 \
    --MonitorMetric.Metrics.0.TimeoutThreshold 7200 \
    --AdvanceConfig.QueuingMode OFF \
    --AdvanceConfig.MaxConcurrentNum 1 \
    --TaskList.0.TaskName sql_0807 \
    --TaskList.0.TaskType.TaskTypeName SQL \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyKey CodeFileId \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyValue file-9a1670f314df \
    --TaskList.0.TaskType.TaskTypePropertyList.2.PropertyKey SqlPath \
    --TaskList.0.TaskType.TaskTypePropertyList.2.PropertyValue /Workspace/sql/dwd_daily_sales.sql \
    --TaskList.0.ResourceGroupId res-ea1234568f8 \
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

**Example 3: 创建定时调度且多任务依赖的工作流**

创建定时调度（每日 2 点）且三任务依赖串联（含高级依赖：上游失败也继续）的工作流

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --BaseInfo.WorkflowName dwd_sales_etl \
    --Trigger.0.SchedulerStatus START \
    --Trigger.0.TriggerMode TIME_TRIGGER \
    --Trigger.0.SchedulerTimeZone Asia/Shanghai \
    --Trigger.0.StartTime 1769740800000 \
    --Trigger.0.EndTime 1798761600000 \
    --Trigger.0.ConfigMode COMMON \
    --Trigger.0.CycleType DAY \
    --Trigger.0.CrontabExpression 0 0 2 * * * \
    --Trigger.0.AdvancedConfig.TaskRetryMode onFailure \
    --TaskList.0.TaskName sql_extract \
    --TaskList.0.TaskType.TaskTypeName SQL \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyKey CodeFileId \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyValue file-9a1670f314df \
    --TaskList.0.TaskType.TaskTypePropertyList.2.PropertyKey SqlPath \
    --TaskList.0.TaskType.TaskTypePropertyList.2.PropertyValue /Workspace/sql/dwd_daily_sales.sql \
    --TaskList.0.ResourceGroupId res-ea1234568f8 \
    --TaskList.0.DependOnRunCondition ALL_SUCCESS \
    --TaskList.0.LeftCoordinate 50 \
    --TaskList.0.TopCoordinate 50 \
    --TaskList.1.TaskName sql_transform \
    --TaskList.1.DependOnList.0.TaskId 000001 \
    --TaskList.1.DependOnList.0.TaskName sql_extract \
    --TaskList.1.TaskType.TaskTypeName SQL \
    --TaskList.1.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.1.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --TaskList.1.TaskType.TaskTypePropertyList.1.PropertyKey CodeFileId \
    --TaskList.1.TaskType.TaskTypePropertyList.1.PropertyValue file-9a1670f314df \
    --TaskList.1.TaskType.TaskTypePropertyList.2.PropertyKey SqlPath \
    --TaskList.1.TaskType.TaskTypePropertyList.2.PropertyValue /Workspace/sql/dwd_daily_sales.sql \
    --TaskList.1.ResourceGroupId res-ea1234568f8 \
    --TaskList.1.DependOnRunCondition ALL_SUCCESS \
    --TaskList.1.LeftCoordinate 50 \
    --TaskList.1.TopCoordinate 50 \
    --TaskList.1.AdvancedDependencyConfig.Operator OR \
    --TaskList.1.AdvancedDependencyConfig.Conditions.0.UpstreamTaskId 000001 \
    --TaskList.1.AdvancedDependencyConfig.Conditions.0.UpstreamTaskName sql_extract \
    --TaskList.1.AdvancedDependencyConfig.Conditions.0.AllowedStates SUCCESS FAILED \
    --TaskList.2.TaskName py_report \
    --TaskList.2.DependOnList.0.TaskId 000002 \
    --TaskList.2.DependOnList.0.TaskName sql_transform \
    --TaskList.2.TaskType.TaskTypeName PYTHON \
    --TaskList.2.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.2.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --TaskList.2.ResourceGroupId res-ea1234568f8 \
    --TaskList.2.TaskRetryStrategy.MaxRetryTimes 3 \
    --TaskList.2.TaskRetryStrategy.RetryBetweenWaitTime 5 \
    --TaskList.2.TaskRetryStrategy.RetryBetweenWaitTimeUnit MINUTE \
    --TaskList.2.TaskRetryStrategy.TaskRunFailureRetrySwitch true \
    --TaskList.2.TaskRetryStrategy.TaskRunTimeoutRetrySwitch false \
    --TaskList.2.DependOnRunCondition ALL_SUCCESS \
    --TaskList.2.LeftCoordinate 50 \
    --TaskList.2.TopCoordinate 50
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

**Example 4: 创建携带Notebook,SQL,离线数据同步任务，且有任务间高级依赖关系的工作流**

创建携带Notebook,SQL,离线数据同步任务，且有任务间高级依赖关系(Notebook任务依赖SQL和离线数据同步任务)的工作流

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --BaseInfo.WorkflowName test_workflow_1028 \
    --TaskList.0.TaskName test_notebook_1028 \
    --TaskList.0.ResourceGroupId res-c07a503e \
    --TaskList.0.DependOnList.0.TaskName test_integration_1028_left \
    --TaskList.0.DependOnList.1.TaskName test_sql_1028_right \
    --TaskList.0.DependOnRunCondition ADVANCED \
    --TaskList.0.AdvancedDependencyConfig.Operator OR \
    --TaskList.0.AdvancedDependencyConfig.Conditions.0.AllowedStates SUCCESS \
    --TaskList.0.AdvancedDependencyConfig.Conditions.0.UpstreamTaskName test_integration_1028_left \
    --TaskList.0.AdvancedDependencyConfig.Conditions.1.AllowedStates FAILED \
    --TaskList.0.AdvancedDependencyConfig.Conditions.1.UpstreamTaskName test_sql_1028_right \
    --TaskList.0.TaskType.TaskTypeName NOTEBOOK \
    --TaskList.0.TaskType.RuntimePropertyList.0.PropertyKey ResourceMode \
    --TaskList.0.TaskType.RuntimePropertyList.0.PropertyValue 1 \
    --TaskList.0.TaskType.RuntimePropertyList.1.PropertyKey ConfigType \
    --TaskList.0.TaskType.RuntimePropertyList.1.PropertyValue CUSTOM \
    --TaskList.0.TaskType.RuntimePropertyList.2.PropertyKey ExecutorAllocation \
    --TaskList.0.TaskType.RuntimePropertyList.2.PropertyValue DYNAMIC \
    --TaskList.0.TaskType.RuntimePropertyList.3.PropertyKey ExecutorCU \
    --TaskList.0.TaskType.RuntimePropertyList.3.PropertyValue small \
    --TaskList.0.TaskType.RuntimePropertyList.4.PropertyKey ExecutorMinNum \
    --TaskList.0.TaskType.RuntimePropertyList.4.PropertyValue 1 \
    --TaskList.0.TaskType.RuntimePropertyList.5.PropertyKey ExecutorMaxNum \
    --TaskList.0.TaskType.RuntimePropertyList.5.PropertyValue 15 \
    --TaskList.0.TaskType.RuntimePropertyList.6.PropertyKey DriverCU \
    --TaskList.0.TaskType.RuntimePropertyList.6.PropertyValue small \
    --TaskList.0.TaskType.RuntimePropertyList.7.PropertyKey Style \
    --TaskList.0.TaskType.RuntimePropertyList.7.PropertyValue UI \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyKey NotebookPath \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyValue /Workspace/notebook_task.ipynb \
    --TaskList.1.TaskName test_integration_1028_left \
    --TaskList.1.ResourceGroupId res-00b25e3a \
    --TaskList.1.TaskType.TaskTypeName DATA_INTEGRATION \
    --TaskList.1.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.1.TaskType.TaskTypePropertyList.0.PropertyValue 4 \
    --TaskList.1.TaskType.TaskTypePropertyList.1.PropertyKey DataIntegrationTaskId \
    --TaskList.1.TaskType.TaskTypePropertyList.1.PropertyValue b4c20ebe-dd13-4875-8ab1-e645d9ca3910 \
    --TaskList.2.TaskName test_sql_1028_right \
    --TaskList.2.ResourceGroupId res-c07a503e \
    --TaskList.2.TaskType.TaskTypeName SQL \
    --TaskList.2.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.2.TaskType.TaskTypePropertyList.0.PropertyValue 5 \
    --TaskList.2.TaskType.TaskTypePropertyList.1.PropertyKey CodeFileId \
    --TaskList.2.TaskType.TaskTypePropertyList.1.PropertyValue 798545986376953856 \
    --TaskList.2.TaskType.TaskTypePropertyList.2.PropertyKey CodeFileVersion \
    --TaskList.2.TaskType.TaskTypePropertyList.2.PropertyValue 871098798448340992
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowId": "d0fb9645-f362-43b8-85bc-07a8cbddd2b9"
        },
        "RequestId": "fbe445ce-0ba0-4cdf-b417-aeac83ec1979"
    }
}
```

**Example 5: 创建携带Ray作业（配置了任务监控指标、告警和重试策略）,质量监控,嵌套工作流任务，且有上游全部成功的任务间简单依赖关系的工作流**

创建携带Ray作业（配置了任务监控指标、告警和重试策略）,质量监控,嵌套工作流任务，且有上游全部成功的任务间简单依赖关系的工作流

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --BaseInfo.WorkflowName test_workflow_1029 \
    --TaskList.0.TaskName test_ray_1028 \
    --TaskList.0.ResourceGroupId res-raydev01 \
    --TaskList.0.DependOnList.0.TaskName test_dq_1028_left \
    --TaskList.0.DependOnList.1.TaskName test_run_workflow_1028_right \
    --TaskList.0.DependOnRunCondition ALL_SUCCESS \
    --TaskList.0.TaskType.TaskTypeName RAY_JOB \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Entrypoint \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue cHl0aG9uIHNpbXBsZV90ZXN0LnB5 \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyKey JobConfig \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyValue eyJSZXNvdXJjZUNvbmZpZyI6IntcIkhlYWRcIjp7XCJOYW1lXCI6XCJIZWFkXCIsXCJSZXNvdXJjZVR5cGVcIjpcIkNQVVwiLFwiQmlsbGluZ0l0ZW1cIjpcInN2X2RsY19zdGFuZGFyZF9jdV9zdGFuZGFyZF9jdVwiLFwiU3BlY1wiOjEsXCJFbnZzXCI6W10sXCJMYWJlbHNcIjpbXSxcIkhpZ2hBdmFpbGFiaWxpdHlcIjpmYWxzZSxcIlBvZE51bVwiOjF9LFwiV29ya2VyXCI6W3tcIk5hbWVcIjpcIldvcmtlckdyb3VwMDFcIixcIlJlc291cmNlVHlwZVwiOlwiQ1BVXCIsXCJCaWxsaW5nSXRlbVwiOlwic3ZfZGxjX3N0YW5kYXJkX2N1X3N0YW5kYXJkX2N1XCIsXCJTcGVjXCI6MSxcIkVudnNcIjpbXSxcIkxhYmVsc1wiOltdLFwiTWluUG9kTnVtXCI6MSxcIk1heFBvZE51bVwiOjF9XX0iLCJJbWFnZSI6ImNjci5jY3MudGVuY2VudHl1bi5jb20vZW1yLWltYWdlL3RjcmF5OnRjcmF5Mi41Ny4wLXB5MzExLWNwdSIsIkltYWdlUHVsbFR5cGUiOiJCdWlsdGluIn0= \
    --TaskList.0.TaskType.TaskTypePropertyList.2.PropertyKey Source \
    --TaskList.0.TaskType.TaskTypePropertyList.2.PropertyValue 5 \
    --TaskList.0.TaskType.TaskTypePropertyList.3.PropertyKey JobPackage \
    --TaskList.0.TaskType.TaskTypePropertyList.3.PropertyValue /Workspace/jonsljiang/simple_test 2.py \
    --TaskList.0.TaskType.TaskTypePropertyList.4.PropertyKey WorkspaceEntryType \
    --TaskList.0.TaskType.TaskTypePropertyList.4.PropertyValue FILE \
    --TaskList.0.TaskType.TaskTypePropertyList.5.PropertyKey RunMode \
    --TaskList.0.TaskType.TaskTypePropertyList.5.PropertyValue SERVERLESS \
    --TaskList.0.TaskRetryStrategy.RetryBetweenWaitTimeUnit MINUTE \
    --TaskList.0.TaskRetryStrategy.RetryBetweenWaitTime 5 \
    --TaskList.0.TaskRetryStrategy.MaxRetryTimes 2 \
    --TaskList.0.TaskRetryStrategy.TaskRunTimeoutRetrySwitch False \
    --TaskList.0.TaskRetryStrategy.TaskRunFailureRetrySwitch True \
    --TaskList.0.Alarm.AlarmMonitorType TASK \
    --TaskList.0.Alarm.AlarmGroups.0.ChannelId  \
    --TaskList.0.Alarm.AlarmGroups.0.ChannelName test_user@xxx.com \
    --TaskList.0.Alarm.AlarmGroups.0.ChannelType 1 \
    --TaskList.0.Alarm.AlarmGroups.0.IsEmailChannel True \
    --TaskList.0.Alarm.AlarmGroups.0.AlarmConditions FAILURE MONITOR_INDICATOR_ALARM \
    --TaskList.0.Alarm.DoNotDisturbWhenSkipped False \
    --TaskList.0.Alarm.DoNotDisturbWhenManuallyTerminated False \
    --TaskList.0.Alarm.DoNotDisturbUntilTheLastRetry False \
    --TaskList.0.MonitorMetric.AlarmMonitorType TASK \
    --TaskList.0.MonitorMetric.Metrics.0.MetricType RUN_DURATION \
    --TaskList.0.MonitorMetric.Metrics.0.WarningThreshold 60000 \
    --TaskList.0.MonitorMetric.Metrics.0.TimeoutThreshold 120000 \
    --TaskList.1.TaskName test_dq_1028_left \
    --TaskList.1.ResourceGroupId res-c07a503e \
    --TaskList.1.TaskType.TaskTypeName DATA_QUALITY \
    --TaskList.1.TaskType.TaskTypePropertyList.0.PropertyKey SourceUniqueId \
    --TaskList.1.TaskType.TaskTypePropertyList.0.PropertyValue dd6c42d1-d36d-4f7f-905b-4db4a83ce6c9 \
    --TaskList.1.TaskType.TaskTypePropertyList.1.PropertyKey Source \
    --TaskList.1.TaskType.TaskTypePropertyList.1.PropertyValue 4 \
    --TaskList.1.TaskType.TaskTypePropertyList.2.PropertyKey TemplatePath \
    --TaskList.1.TaskType.TaskTypePropertyList.2.PropertyValue quality/tasks/17678671667189298/dd6c42d1-d36d-4f7f-905b-4db4a83ce6c9/published/templates.json \
    --TaskList.2.TaskName test_run_workflow_1028_right \
    --TaskList.2.TaskType.TaskTypeName RUN_WORKFLOW \
    --TaskList.2.TaskType.TaskTypePropertyList.0.PropertyKey WorkflowId \
    --TaskList.2.TaskType.TaskTypePropertyList.0.PropertyValue 27a49f96-004c-4438-bded-d21cb6892c8c
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowId": "958dfa6f-a6e6-41fa-bdb7-97a5a923f40c"
        },
        "RequestId": "16b27bd7-9e0a-440a-bee2-82866561e5f0"
    }
}
```

**Example 6: 创建携带嵌套工作流任务的工作流**

创建携带嵌套工作流（RUN_WORKFLOW）任务的工作流，通过 WorkflowId 属性指定目标工作流

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --BaseInfo.WorkflowName sub_wf_caller_workflow \
    --TaskList.0.TaskName sub_wf_caller \
    --TaskList.0.TaskType.TaskTypeName RUN_WORKFLOW \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey WorkflowId \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 9a1670f3-14df-4869-9f38-ec31a4c4aac9 \
    --TaskList.0.ResourceGroupId res-ea1234568f8 \
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

**Example 7: 创建携带数据质量任务的工作流**

创建携带数据质量（DATA_QUALITY）任务的工作流，属性列表参考 ListWorkflowTaskTypeProperties 接口

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --BaseInfo.WorkflowName dq_check_workflow \
    --TaskList.0.TaskName dq_0807 \
    --TaskList.0.TaskType.TaskTypeName DATA_QUALITY \
    --TaskList.0.ResourceGroupId res-ea1234568f8 \
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

**Example 8: 创建一个携带Python任务的工作流**

创建一个携带Python任务的工作流，任务来源为git，资源模式为单节点，资源配置small(1CU)。

Input: 

```
tccli databuddy CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --BaseInfo.WorkflowName test_workflow_1031 \
    --GitBranch main \
    --GitConfigId 17879110044139837 \
    --TaskList.0.TaskName py_0807 \
    --TaskList.0.ResourceGroupId res-46e4a9a0 \
    --TaskList.0.TaskType.TaskTypeName PYTHON \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyKey Source \
    --TaskList.0.TaskType.TaskTypePropertyList.0.PropertyValue 2 \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyKey SourcePath \
    --TaskList.0.TaskType.TaskTypePropertyList.1.PropertyValue 1234.py \
    --TaskList.0.TaskType.RuntimePropertyList.0.PropertyKey ResourceMode \
    --TaskList.0.TaskType.RuntimePropertyList.0.PropertyValue 2 \
    --TaskList.0.TaskType.RuntimePropertyList.1.PropertyKey DriverCU \
    --TaskList.0.TaskType.RuntimePropertyList.1.PropertyValue small
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowId": "d940c85b-d5d0-4c26-96b2-eefe43e614cd"
        },
        "RequestId": "6843c1e7-ddfd-433c-90b6-634371a40750"
    }
}
```

