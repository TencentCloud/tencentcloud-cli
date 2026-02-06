**Example 1: 更新工作流调度任务**

更新工作流调度任务

Input: 

```
tccli wedata UpdateTriggerTask --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251124113217312 \
    --Task.TriggerTaskBaseAttribute.TaskName gallop_workflow_task_test_down \
    --Task.TriggerTaskBaseAttribute.OwnerUin 100028597773 \
    --Task.TriggerTaskBaseAttribute.TaskDescription update_desc \
    --Task.TriggerTaskConfiguration.CodeContent IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKaGVsbG93b3JsZAo= \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.0.ParamKey bucket \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.0.ParamValue wedata-fusion-dev-1257305158 \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.1.ParamKey specLabelConfItems \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.1.ParamValue eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ== \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.2.ParamKey ftp.file.name \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.2.ParamValue /datastudio/project/1460947878944567296/默认文件夹/gallopcai_workflow/gallop_workflow_task_test_down.sh \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.3.ParamKey tenantId \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.3.ParamValue 1257305158 \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.4.ParamKey calendar_open \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.4.ParamValue 0 \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.5.ParamKey region \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.5.ParamValue ap-nanjing \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.6.ParamKey waitExecutionTotalTTL \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.6.ParamValue 43100 \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.7.ParamKey enableKerberosLogin \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.7.ParamValue false \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.8.ParamKey extraInfo \
    --Task.TriggerTaskConfiguration.TaskExtConfigurationList.8.ParamValue {"fromMapping":false} \
    --Task.TriggerTaskConfiguration.DataCluster  \
    --Task.TriggerTaskConfiguration.BrokerIp any \
    --Task.TriggerTaskConfiguration.ResourceGroup 20240222212719833743 \
    --Task.TriggerTaskSchedulerConfiguration.UpstreamDependencyConfigList.0.TaskId 20251121175713839 \
    --Task.TriggerTaskSchedulerConfiguration.RunPriorityType 5 \
    --Task.TriggerTaskSchedulerConfiguration.RetryWaitMinute 4 \
    --Task.TriggerTaskSchedulerConfiguration.MaxRetryNumber 3 \
    --Task.TriggerTaskSchedulerConfiguration.ExecutionTTLMinute 10 \
    --Task.TriggerTaskSchedulerConfiguration.WaitExecutionTotalTTLMinute 15 \
    --Task.TriggerTaskSchedulerConfiguration.AllowRedoType ALL \
    --Task.TriggerTaskSchedulerConfiguration.ParamTaskOutList.0.ParamKey asadad \
    --Task.TriggerTaskSchedulerConfiguration.ParamTaskOutList.0.ParamValue 1 \
    --Task.TriggerTaskSchedulerConfiguration.ParamTaskOutList.1.ParamKey update_param_out \
    --Task.TriggerTaskSchedulerConfiguration.ParamTaskOutList.1.ParamValue 222_out
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "d66d48cf-1a68-4cae-a342-9e702df541b7"
    }
}
```

