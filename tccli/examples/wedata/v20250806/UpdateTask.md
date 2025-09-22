**Example 1: 更新任务**

更新任务

Input: 

```
tccli wedata UpdateTask --cli-unfold-argument  \
    --ProjectId 2417334454903762944 \
    --TaskId 20250908225847483 \
    --Task.TaskBaseAttribute.TaskName sh_241204_111248_copy \
    --Task.TaskBaseAttribute.OwnerUin 100028579801 \
    --Task.TaskBaseAttribute.TaskDescription  \
    --Task.TaskConfiguration.CodeContent IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK \
    --Task.TaskConfiguration.TaskExtConfigurationList.0.ParamKey calendar_id \
    --Task.TaskConfiguration.TaskExtConfigurationList.0.ParamValue  \
    --Task.TaskConfiguration.TaskExtConfigurationList.1.ParamKey python_type \
    --Task.TaskConfiguration.TaskExtConfigurationList.1.ParamValue python3 \
    --Task.TaskConfiguration.TaskExtConfigurationList.2.ParamKey data_cluster \
    --Task.TaskConfiguration.TaskExtConfigurationList.2.ParamValue  \
    --Task.TaskConfiguration.TaskExtConfigurationList.3.ParamKey calendar_open \
    --Task.TaskConfiguration.TaskExtConfigurationList.3.ParamValue 0 \
    --Task.TaskConfiguration.TaskExtConfigurationList.4.ParamKey calendar_name \
    --Task.TaskConfiguration.TaskExtConfigurationList.4.ParamValue  \
    --Task.TaskConfiguration.TaskExtConfigurationList.5.ParamKey waitExecutionTotalTTL \
    --Task.TaskConfiguration.TaskExtConfigurationList.5.ParamValue -1 \
    --Task.TaskConfiguration.TaskExtConfigurationList.6.ParamKey executionTTLStrategy \
    --Task.TaskConfiguration.TaskExtConfigurationList.6.ParamValue fail \
    --Task.TaskConfiguration.TaskExtConfigurationList.7.ParamKey bucket \
    --Task.TaskConfiguration.TaskExtConfigurationList.7.ParamValue wedata-fusion-dev-1257305158 \
    --Task.TaskConfiguration.TaskExtConfigurationList.8.ParamKey specLabelConfItems \
    --Task.TaskConfiguration.TaskExtConfigurationList.8.ParamValue eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ== \
    --Task.TaskConfiguration.TaskExtConfigurationList.9.ParamKey waitExecutionTotalTTLStrategy \
    --Task.TaskConfiguration.TaskExtConfigurationList.9.ParamValue fail \
    --Task.TaskConfiguration.TaskExtConfigurationList.10.ParamKey python_sub_version \
    --Task.TaskConfiguration.TaskExtConfigurationList.10.ParamValue python3 \
    --Task.TaskConfiguration.TaskExtConfigurationList.11.ParamKey ftp.file.name \
    --Task.TaskConfiguration.TaskExtConfigurationList.11.ParamValue https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com/datastudio/project/2417334454903762944/case_ssh/wf_ssh_test_01/sh_241204_111248_20250908225847483.sh \
    --Task.TaskConfiguration.TaskExtConfigurationList.12.ParamKey tenantId \
    --Task.TaskConfiguration.TaskExtConfigurationList.12.ParamValue 1257305158 \
    --Task.TaskConfiguration.TaskExtConfigurationList.13.ParamKey region \
    --Task.TaskConfiguration.TaskExtConfigurationList.13.ParamValue ap-nanjing \
    --Task.TaskConfiguration.TaskExtConfigurationList.14.ParamKey enableKerberosLogin \
    --Task.TaskConfiguration.TaskExtConfigurationList.14.ParamValue false \
    --Task.TaskConfiguration.TaskExtConfigurationList.15.ParamKey extraInfo \
    --Task.TaskConfiguration.TaskExtConfigurationList.15.ParamValue {"fromMapping":false} \
    --Task.TaskConfiguration.DataCluster  \
    --Task.TaskConfiguration.BrokerIp any \
    --Task.TaskConfiguration.ResourceGroup 20240416215649571819 \
    --Task.TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --Task.TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --Task.TaskSchedulerConfiguration.StartTime 2024-12-04 00:00:00 \
    --Task.TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --Task.TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --Task.TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --Task.TaskSchedulerConfiguration.ScheduleRunType 0 \
    --Task.TaskSchedulerConfiguration.CalendarOpen 0 \
    --Task.TaskSchedulerConfiguration.CalendarId  \
    --Task.TaskSchedulerConfiguration.CalendarName  \
    --Task.TaskSchedulerConfiguration.SelfDepend serial \
    --Task.TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.TaskId 20241204111252781 \
    --Task.TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.MainCyclicConfig DAY \
    --Task.TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.SubordinateCyclicConfig CURRENT_DAY \
    --Task.TaskSchedulerConfiguration.UpstreamDependencyConfigList.0.DependencyStrategy.PollingNullStrategy WAITING \
    --Task.TaskSchedulerConfiguration.EventListenerList.0.EventName event_241030 \
    --Task.TaskSchedulerConfiguration.EventListenerList.0.EventSubType DAY \
    --Task.TaskSchedulerConfiguration.EventListenerList.0.EventBroadcastType BROADCAST \
    --Task.TaskSchedulerConfiguration.RunPriority 6 \
    --Task.TaskSchedulerConfiguration.RetryWait 5 \
    --Task.TaskSchedulerConfiguration.MaxRetryAttempts 4 \
    --Task.TaskSchedulerConfiguration.ExecutionTTL -1 \
    --Task.TaskSchedulerConfiguration.WaitExecutionTotalTTL -1 \
    --Task.TaskSchedulerConfiguration.AllowRedoType ALL \
    --Task.TaskSchedulerConfiguration.ParamTaskOutList.0.ParamKey asadad \
    --Task.TaskSchedulerConfiguration.ParamTaskOutList.0.ParamValue 1 \
    --Task.TaskSchedulerConfiguration.ParamTaskInList.0.ParamKey intask_v \
    --Task.TaskSchedulerConfiguration.ParamTaskInList.0.ParamDesc DATA_DEV_SIM_PROJ_01.sh_241204_111248.taskout_v1 \
    --Task.TaskSchedulerConfiguration.ParamTaskInList.0.FromTaskId 20241204111252781 \
    --Task.TaskSchedulerConfiguration.ParamTaskInList.0.FromParamKey taskout_v1 \
    --Task.TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --Task.TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "93937196-c55c-4cad-b148-7af3cfb44c4d"
    }
}
```

