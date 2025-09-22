**Example 1: 创建任务**

创建任务

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2417334454903762944 \
    --TaskBaseAttribute.TaskName api_sh_250910_174514 \
    --TaskBaseAttribute.TaskTypeId 35 \
    --TaskBaseAttribute.WorkflowId a5acf635-a297-458d-a311-14745662dcae \
    --TaskBaseAttribute.OwnerUin 100028579801 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20240416215649571819 \
    --TaskConfiguration.CodeContent IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey enableKerberosLogin \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue false \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster  \
    --TaskConfiguration.BrokerIp any \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2024-12-04 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleRunType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.TaskId 20241204111252781 \
    --TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.MainCyclicConfig DAY \
    --TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.SubordinateCyclicConfig CURRENT_DAY \
    --TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.DependencyStrategy.PollingNullStrategy WAITING \
    --TaskSchedulerConfiguration.EventListenerList.0.EventName event_241030 \
    --TaskSchedulerConfiguration.EventListenerList.0.EventSubType DAY \
    --TaskSchedulerConfiguration.EventListenerList.0.EventBroadcastType BROADCAST \
    --TaskSchedulerConfiguration.RunPriority 6 \
    --TaskSchedulerConfiguration.RetryWait 5 \
    --TaskSchedulerConfiguration.MaxRetryAttempts 4 \
    --TaskSchedulerConfiguration.ExecutionTTL -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTL -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.ParamTaskOutList.0.ParamKey asadad \
    --TaskSchedulerConfiguration.ParamTaskOutList.0.ParamValue 1 \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174556035"
        },
        "RequestId": "933bd57d-a860-4b14-97d5-996d0c0bf10c"
    }
}
```

