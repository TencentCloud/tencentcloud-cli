**Example 1: 添加一个没有上游的工作流调度任务**

添加一个没有上游的工作流调度任务

Input: 

```
tccli wedata CreateTriggerTask --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TriggerTaskBaseAttribute.TaskName gallop_workflow_task_test_2_1222 \
    --TriggerTaskBaseAttribute.TaskTypeId 35 \
    --TriggerTaskBaseAttribute.WorkflowId d3e40dcc-bf42-4fb9-b081-b00408d478ec \
    --TriggerTaskBaseAttribute.OwnerUin 100028579801 \
    --TriggerTaskBaseAttribute.TaskDescription  \
    --TriggerTaskConfiguration.ResourceGroup 20240222212719833743 \
    --TriggerTaskConfiguration.CodeContent IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK \
    --TriggerTaskConfiguration.TaskExtConfigurationList.0.ParamKey enableKerberosLogin \
    --TriggerTaskConfiguration.TaskExtConfigurationList.0.ParamValue false \
    --TriggerTaskConfiguration.TaskExtConfigurationList.1.ParamKey extraInfo \
    --TriggerTaskConfiguration.TaskExtConfigurationList.1.ParamValue {"fromMapping":false} \
    --TriggerTaskConfiguration.DataCluster  \
    --TriggerTaskConfiguration.BrokerIp any \
    --TriggerTaskSchedulerConfiguration.RunPriorityType 6 \
    --TriggerTaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TriggerTaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TriggerTaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TriggerTaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TriggerTaskSchedulerConfiguration.AllowRedoType ALL \
    --TriggerTaskSchedulerConfiguration.ParamTaskOutList.0.ParamKey asadad \
    --TriggerTaskSchedulerConfiguration.ParamTaskOutList.0.ParamValue 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20251222225827398"
        },
        "RequestId": "a72bf5c4-2398-4081-84d0-967e1391a325"
    }
}
```

