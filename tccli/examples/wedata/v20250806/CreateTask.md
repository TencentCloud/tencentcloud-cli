**Example 2: 任务类型133：SSH**

任务类型133：SSH


Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 1869349306215632896 \
    --TaskBaseAttribute.TaskName test_ssh_openapi111111 \
    --TaskBaseAttribute.TaskTypeId 133 \
    --TaskBaseAttribute.WorkflowId ce95d416-c360-4c97-9d7e-1fb34a070a0b \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription test_ssh_openapi1 \
    --TaskConfiguration.CodeContent LS1UQ0hvdXNlLVggU1FMCi0tKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLS0KLS1hdXRob3I6IHNvbG9tb25kZW5nCi0tY3JlYXRlIHRpbWU6IDIwMjUtMDgtMjggMTk6NDE6NTEKLS0qKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiotLQotLeS9v+eUqFRDSG91c2UtWCBTUUznmoTnprvnur/mlbDmja7lpITnkIblvJXmk47vvIxTUUzmnIDliY3pnaLpnIDopoHmt7vliqAgLyorZW5naW5lPWJhdGNoKi8tLQpzaG93IHRhYmxlczs= \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 83112 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey specLabelConfItems \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ== \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey waitExecutionTotalTTL \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue -1 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20231124174433263533 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558006"
        },
        "RequestId": "c40e882d-5b8a-42f8-84ff-29c66e983137"
    }
}
```

**Example 3: 任务类型134：StarRocks**

任务类型134：StarRocks

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName test_st_openapi111111 \
    --TaskBaseAttribute.TaskTypeId 134 \
    --TaskBaseAttribute.WorkflowId c3152ead-bd27-4c07-afbc-2ae7b54347a4 \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription test_ssh_openapi1 \
    --TaskConfiguration.CodeContent c2VsZWN0IDE7 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 71512 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue emr-higbxfuq \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue emr-higbxfuq \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue default \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174559005"
        },
        "RequestId": "b8a6969d-c78e-4ec4-a817-ef6a0c8c909f"
    }
}
```

**Example 4: 任务类型138：Setats SQL**

任务类型138：Setats SQL

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917511217424453632 \
    --TaskBaseAttribute.TaskName test_setats_openapi111111wwwwwqqqq \
    --TaskBaseAttribute.TaskTypeId 138 \
    --TaskBaseAttribute.WorkflowId 2e773f88-9e7b-4cd2-b601-2e5cb545bd8c \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription test_ssh_openapi1 \
    --TaskConfiguration.CodeContent Q1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgZGF0YWdlbl9zb3VyY2VfdGFibGUgKCAKICAgIGlkIElOVCwgCiAgICBuYW1lIFNUUklORyAKKSBXSVRIICggCiAgICAnY29ubmVjdG9yJyA9ICdkYXRhZ2VuJywKICAgICdyb3dzLXBlci1zZWNvbmQnPScxJyAgLS0g5q+P56eS5Lqn55Sf55qE5pWw5o2u5p2h5pWwCik7CgpDUkVBVEUgVEFCTEUgSUYgTk9UIEVYSVNUUyBibGFja2hvbGVfc2luayAoIAogICAgaWQgSU5ULCAKICAgIG5hbWUgU1RSSU5HIAopIFdJVEggKCAKICAgICdjb25uZWN0b3InID0gJ2JsYWNraG9sZScKKTsKCmluc2VydCBpbnRvIGJsYWNraG9sZV9zaW5rIHNlbGVjdCAqIGZyb20gZGF0YWdlbl9zb3VyY2VfdGFibGUgbGltaXQgMTAgOw== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey engine.jobManagerSpec \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey engine.properties \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey engine.defaultParallelism \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey engine.taskManagerSpec \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 73171 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue cluster-muom2ct7 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue cluster-muom2ct7 \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey engine.runMode \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 1 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174559007"
        },
        "RequestId": "9df82dfe-4e01-4836-a513-b68ff930c80c"
    }
}
```

**Example 5: 任务类型21：JDBC-SQL任务**

任务类型21：JDBC-SQL任务

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName test110 \
    --TaskBaseAttribute.TaskTypeId 21 \
    --TaskBaseAttribute.WorkflowId a9ef8153-2291-4b60-8b57-3364a384df69 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription 251205_201200 \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskConfiguration.CodeContent LS1KREJDIFNRTAotLSoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi0tCi0tYXV0aG9yOiBzb2xvbW9uZGVuZwotLWNyZWF0ZSB0aW1lOiAyMDI1LTA4LTI5IDEwOjMzOjI4Ci0tKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLS0Kc2VsZWN0IDEzNDQyOw== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue f827b4ae-3500-4960-8a6b-d45054c65335 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 70604 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey service_type \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue sqlserver \
    --TaskConfiguration.DataCluster f827b4ae-3500-4960-8a6b-d45054c65335 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.YarnQueue None \
    --TaskConfiguration.SourceServiceId 70604 \
    --TaskConfiguration.TargetServiceId None \
    --TaskConfiguration.BundleId None \
    --TaskConfiguration.BundleInfo None \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174556001"
        },
        "RequestId": "0103e074-da92-4f46-9ec9-b262f5748ff5"
    }
}
```

**Example 6: 任务类型23：TDSQL-PostgreSQL**

任务类型23：TDSQL-PostgreSQL

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName test206 \
    --TaskBaseAttribute.TaskTypeId 23 \
    --TaskBaseAttribute.WorkflowId a9ef8153-2291-4b60-8b57-3364a384df69 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription 251205_204816 \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskConfiguration.CodeContent c2VsZWN0IDEzNDQyOw== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue 378334db-ab57-47d4-999c-cc458328f0b1 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 80933 \
    --TaskConfiguration.DataCluster 378334db-ab57-47d4-999c-cc458328f0b1 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId None \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174556003"
        },
        "RequestId": "641e9f83-de4a-47de-b804-0767342a651d"
    }
}
```

**Example 7: 任务类型26：OfflineSynchronization （集成任务） 表单模式**

任务类型26：OfflineSynchronization （集成任务） 表单模式

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskBaseAttribute.TaskName etl_1_api_250827_232828 \
    --TaskBaseAttribute.TaskTypeId 26 \
    --TaskBaseAttribute.WorkflowId 7feb253c-e734-4aa1-a466-c36eee16fa6b \
    --TaskBaseAttribute.OwnerUin 100028579801 \
    --TaskBaseAttribute.TaskDescription etl_1_api \
    --TaskConfiguration.CodeContent IFt7Ik5hbWUiOiJJTlBVVCIsIk5vZGVUeXBlIjoiSU5QVVQiLCJEYXRhU291cmNlVHlwZSI6Ik1ZU1FMIiwiRGVzY3JpcHRpb24iOm51bGwsIkRhdGFzb3VyY2VJZCI6IjYxOTM0IiwiUHJvamVjdElkIjoiMCIsIkNyZWF0b3JVaW4iOiIxMDAwMjg1Nzk4MDEiLCJPcGVyYXRvclVpbiI6IjEwMDAyODU3OTgwMSIsIk93bmVyVWluIjpudWxsLCJBcHBJZCI6IjEzMTUwNTE3ODkiLCJDb25maWciOlt7Ik5hbWUiOiJUeXBlIiwiVmFsdWUiOiJNWVNRTCJ9LHsiTmFtZSI6InNwbGl0UGsiLCJWYWx1ZSI6ImVtcGxveWVlX2lkIn0seyJOYW1lIjoiUHJpbWFyeUtleSIsIlZhbHVlIjoiZW1wbG95ZWVfaWQifSx7Ik5hbWUiOiJpc05ldyIsIlZhbHVlIjoidHJ1ZSJ9LHsiTmFtZSI6IlRhYmxlSWQiLCJWYWx1ZSI6ImFwY3NfZHVvemh1amlhbjEifSx7Ik5hbWUiOiJQcmltYXJ5S2V5X0lOUFVUX1NZTUJPTCIsIlZhbHVlIjoiaW5wdXQifSx7Ik5hbWUiOiJzcGxpdFBrX0lOUFVUX1NZTUJPTCIsIlZhbHVlIjoiaW5wdXQifSx7Ik5hbWUiOiJEYXRhYmFzZSIsIlZhbHVlIjoibWVuZ2h1aXl1In0seyJOYW1lIjoiVGFibGVOYW1lcyIsIlZhbHVlIjoiYXBjc19kdW96aHVqaWFuMSJ9LHsiTmFtZSI6InF1ZXJ5TW9kZSIsIlZhbHVlIjoidGFibGUifSx7Ik5hbWUiOiJ0YWJsZV9JTlBVVF9TWU1CT0wiLCJWYWx1ZSI6InNlbGVjdCJ9LHsiTmFtZSI6IlNpYmxpbmdOb2RlcyIsIlZhbHVlIjoiW10ifSx7Ik5hbWUiOiJjbHVzdGVyRGVwbG95VHlwZSIsIlZhbHVlIjoiIn0seyJOYW1lIjoiaXNDbGVhbiIsIlZhbHVlIjoiMCJ9LHsiTmFtZSI6ImVuY29kaW5nIiwiVmFsdWUiOiJ1dGYtOCJ9LHsiTmFtZSI6ImRhdGFzb3VyY2VEZXZEQiIsIlZhbHVlIjoid2VkYXRhREIifV0sIkV4dENvbmZpZyI6W3siTmFtZSI6IngiLCJWYWx1ZSI6IjI5MCJ9LHsiTmFtZSI6InkiLCJWYWx1ZSI6IjE2MCJ9LHsiTmFtZSI6Imljb25Qb3NpdGlvbiIsIlZhbHVlIjoibGVmdCJ9LHsiTmFtZSI6InNpemUiLCJWYWx1ZSI6Im0ifSx7Ik5hbWUiOiJkaXNUeXBlIiwiVmFsdWUiOiIifV0sIlNjaGVtYSI6W3siSWQiOiI4NTYzMjk1MzYiLCJOYW1lIjoiZW1wbG95ZWVfaWQiLCJWYWx1ZSI6bnVsbCwiVHlwZSI6ImludCIsIlByb3BlcnRpZXMiOltdLCJBbGlhcyI6ImVtcGxveWVlX2lkIiwiQ29tbWVudCI6IiIsIkNhdGVnb3J5IjpudWxsfSx7IklkIjoiODkyNDc0NzUyIiwiTmFtZSI6ImVtYWlsIiwiVmFsdWUiOm51bGwsIlR5cGUiOiJ2YXJjaGFyKDUwKSIsIlByb3BlcnRpZXMiOltdLCJBbGlhcyI6ImVtYWlsIiwiQ29tbWVudCI6IiIsIkNhdGVnb3J5IjpudWxsfSx7IklkIjoiNzI3ODI3NzYiLCJOYW1lIjoiZmlyc3RfbmFtZSIsIlZhbHVlIjpudWxsLCJUeXBlIjoidmFyY2hhcigyMCkiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJmaXJzdF9uYW1lIiwiQ29tbWVudCI6IiIsIkNhdGVnb3J5IjpudWxsfSx7IklkIjoiOTIzODMzMTUyIiwiTmFtZSI6Imxhc3RfbmFtZSIsIlZhbHVlIjpudWxsLCJUeXBlIjoidmFyY2hhcigyNSkiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJsYXN0X25hbWUiLCJDb21tZW50IjoiIiwiQ2F0ZWdvcnkiOm51bGx9LHsiSWQiOiIxMjU0NzM4NDAiLCJOYW1lIjoiaGlyZV9kYXRlIiwiVmFsdWUiOm51bGwsIlR5cGUiOiJkYXRldGltZSIsIlByb3BlcnRpZXMiOltdLCJBbGlhcyI6ImhpcmVfZGF0ZSIsIkNvbW1lbnQiOiIiLCJDYXRlZ29yeSI6bnVsbH0seyJJZCI6IjE3ODI2MjU3NiIsIk5hbWUiOiJuZXdfY29sIiwiVmFsdWUiOm51bGwsIlR5cGUiOiJ2YXJjaGFyKDEwMCkiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJuZXdfY29sIiwiQ29tbWVudCI6IiIsIkNhdGVnb3J5IjpudWxsfV0sIk5vZGVNYXBwaW5nIjpudWxsfSx7Ik5hbWUiOiJPVVRQVVQiLCJOb2RlVHlwZSI6Ik9VVFBVVCIsIkRhdGFTb3VyY2VUeXBlIjoiTVlTUUwiLCJEZXNjcmlwdGlvbiI6bnVsbCwiRGF0YXNvdXJjZUlkIjoiNjIxNzUiLCJQcm9qZWN0SWQiOiIwIiwiQ3JlYXRvclVpbiI6IjEwMDAyODU3OTgwMSIsIk9wZXJhdG9yVWluIjoiMTAwMDI4NTc5ODAxIiwiT3duZXJVaW4iOm51bGwsIkFwcElkIjoiMTMxNTA1MTc4OSIsIkNvbmZpZyI6W3siTmFtZSI6IlR5cGUiLCJWYWx1ZSI6Ik1ZU1FMIn0seyJOYW1lIjoiRGF0YWJhc2UiLCJWYWx1ZSI6Im1lbmdodWl5dSJ9LHsiTmFtZSI6IlRhYmxlTmFtZXMiLCJWYWx1ZSI6ImFwY3NfZmVpd2VpeWlzdW95aW4ifSx7Ik5hbWUiOiJpc0NsZWFuIiwiVmFsdWUiOiIwIn0seyJOYW1lIjoiZW5jb2RpbmciLCJWYWx1ZSI6InV0Zi04In0seyJOYW1lIjoid3JpdGVNb2RlIiwiVmFsdWUiOiJhcHBlbmQifSx7Ik5hbWUiOiJzeW5jVHlwZSIsIlZhbHVlIjoic2luZ2xlX3RhYmxlIn0seyJOYW1lIjoiVGFibGVJZCIsIlZhbHVlIjoiYXBjc19mZWl3ZWl5aXN1b3lpbiJ9LHsiTmFtZSI6ImluRmV0Y2hUeXBlIiwiVmFsdWUiOiJNWVNRTCJ9LHsiTmFtZSI6ImRhdGFzb3VyY2VSZWdpb24iLCJWYWx1ZSI6ImFwLWJlaWppbmcifSx7Ik5hbWUiOiJjbHVzdGVyRGVwbG95VHlwZSIsIlZhbHVlIjoiIn0seyJOYW1lIjoiZGF0YXNvdXJjZURldkRCIiwiVmFsdWUiOiJ3ZWRhdGFEQiJ9XSwiRXh0Q29uZmlnIjpbeyJOYW1lIjoieCIsIlZhbHVlIjoiMzAwIn0seyJOYW1lIjoieSIsIlZhbHVlIjoiMjYwIn0seyJOYW1lIjoiaWNvblBvc2l0aW9uIiwiVmFsdWUiOiJsZWZ0In0seyJOYW1lIjoic2l6ZSIsIlZhbHVlIjoibSJ9LHsiTmFtZSI6ImRpc1R5cGUiLCJWYWx1ZSI6IiJ9XSwiU2NoZW1hIjpbeyJJZCI6IjYzODIxMTA3MiIsIk5hbWUiOiJlbXBsb3llZV9pZCIsIlZhbHVlIjpudWxsLCJUeXBlIjoiaW50IiwiUHJvcGVydGllcyI6W10sIkFsaWFzIjoiZW1wbG95ZWVfaWQiLCJDb21tZW50IjoiIiwiQ2F0ZWdvcnkiOm51bGx9LHsiSWQiOiIzNTQwNzUwMDgiLCJOYW1lIjoiZmlyc3RfbmFtZSIsIlZhbHVlIjpudWxsLCJUeXBlIjoidmFyY2hhcigyMCkiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJmaXJzdF9uYW1lIiwiQ29tbWVudCI6IiIsIkNhdGVnb3J5IjpudWxsfSx7IklkIjoiMzMwNTg1NTY4IiwiTmFtZSI6Imxhc3RfbmFtZSIsIlZhbHVlIjpudWxsLCJUeXBlIjoidmFyY2hhcigyNSkiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJsYXN0X25hbWUiLCJDb21tZW50IjoiIiwiQ2F0ZWdvcnkiOm51bGx9LHsiSWQiOiI5MTUyNzY0MTYiLCJOYW1lIjoiZW1haWwiLCJWYWx1ZSI6bnVsbCwiVHlwZSI6InZhcmNoYXIoNTApIiwiUHJvcGVydGllcyI6W10sIkFsaWFzIjoiZW1haWwiLCJDb21tZW50IjoiIiwiQ2F0ZWdvcnkiOm51bGx9LHsiSWQiOiI4MjAyMzg5NzYiLCJOYW1lIjoiaGlyZV9kYXRlIiwiVmFsdWUiOm51bGwsIlR5cGUiOiJkYXRlIiwiUHJvcGVydGllcyI6W10sIkFsaWFzIjoiaGlyZV9kYXRlIiwiQ29tbWVudCI6IiIsIkNhdGVnb3J5IjpudWxsfV0sIk5vZGVNYXBwaW5nIjp7IlNvdXJjZUlkIjoiNTc3MSIsIlNpbmtJZCI6IjU3NzIiLCJTb3VyY2VTY2hlbWEiOlt7IklkIjoiODU2MzI5NTM2IiwiTmFtZSI6ImVtcGxveWVlX2lkIiwiVmFsdWUiOm51bGwsIlR5cGUiOiJpbnQiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJlbXBsb3llZV9pZCIsIkNvbW1lbnQiOiIiLCJDYXRlZ29yeSI6bnVsbH0seyJJZCI6Ijg5MjQ3NDc1MiIsIk5hbWUiOiJlbWFpbCIsIlZhbHVlIjpudWxsLCJUeXBlIjoidmFyY2hhcig1MCkiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJlbWFpbCIsIkNvbW1lbnQiOiIiLCJDYXRlZ29yeSI6bnVsbH0seyJJZCI6IjcyNzgyNzc2IiwiTmFtZSI6ImZpcnN0X25hbWUiLCJWYWx1ZSI6bnVsbCwiVHlwZSI6InZhcmNoYXIoMjApIiwiUHJvcGVydGllcyI6W10sIkFsaWFzIjoiZmlyc3RfbmFtZSIsIkNvbW1lbnQiOiIiLCJDYXRlZ29yeSI6bnVsbH0seyJJZCI6IjkyMzgzMzE1MiIsIk5hbWUiOiJsYXN0X25hbWUiLCJWYWx1ZSI6bnVsbCwiVHlwZSI6InZhcmNoYXIoMjUpIiwiUHJvcGVydGllcyI6W10sIkFsaWFzIjoibGFzdF9uYW1lIiwiQ29tbWVudCI6IiIsIkNhdGVnb3J5IjpudWxsfSx7IklkIjoiMTI1NDczODQwIiwiTmFtZSI6ImhpcmVfZGF0ZSIsIlZhbHVlIjpudWxsLCJUeXBlIjoiZGF0ZXRpbWUiLCJQcm9wZXJ0aWVzIjpbXSwiQWxpYXMiOiJoaXJlX2RhdGUiLCJDb21tZW50IjoiIiwiQ2F0ZWdvcnkiOm51bGx9LHsiSWQiOiIxNzgyNjI1NzYiLCJOYW1lIjoibmV3X2NvbCIsIlZhbHVlIjpudWxsLCJUeXBlIjoidmFyY2hhcigxMDApIiwiUHJvcGVydGllcyI6W10sIkFsaWFzIjoibmV3X2NvbCIsIkNvbW1lbnQiOiIiLCJDYXRlZ29yeSI6bnVsbH1dLCJFeHRDb25maWciOlt7Ik5hbWUiOiJmcm9tTm9kZSIsIlZhbHVlIjoibm9kZV81NzcxIn0seyJOYW1lIjoidG9Ob2RlIiwiVmFsdWUiOiJub2RlXzU3NzIifSx7Ik5hbWUiOiJmcm9tTm9kZUFuY2hvciIsIlZhbHVlIjoiYm90dG9tIn0seyJOYW1lIjoidG9Ob2RlQW5jaG9yIiwiVmFsdWUiOiJ0b3AifV0sIlNjaGVtYU1hcHBpbmdzIjpbeyJTb3VyY2VTY2hlbWFJZCI6Ijg1NjMyOTUzNiIsIlNpbmtTY2hlbWFJZCI6IjYzODIxMTA3MiJ9LHsiU291cmNlU2NoZW1hSWQiOiI4OTI0NzQ3NTIiLCJTaW5rU2NoZW1hSWQiOiI5MTUyNzY0MTYifSx7IlNvdXJjZVNjaGVtYUlkIjoiNzI3ODI3NzYiLCJTaW5rU2NoZW1hSWQiOiIzNTQwNzUwMDgifSx7IlNvdXJjZVNjaGVtYUlkIjoiOTIzODMzMTUyIiwiU2lua1NjaGVtYUlkIjoiMzMwNTg1NTY4In0seyJTb3VyY2VTY2hlbWFJZCI6IjEyNTQ3Mzg0MCIsIlNpbmtTY2hlbWFJZCI6IjgyMDIzODk3NiJ9XX19XQ== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey enableDataContrast \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue false \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey target_service_type \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue MYSQL \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey targetScope \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue ALL \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey waitExecutionTotalTTL \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue -1 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey target_service \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 62175 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey dirtyDataThresholdUnit \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey sourceIncrementCondition \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey syncRateLimitUnit \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue 61934 \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey calendar_id \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey syncRateLimit \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue -1 \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue 2568295b-56ac-4a74-8b37-4c8b17545353 \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey calendar_open \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey calendar_name \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamKey dataContrastRule \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamValue Cnt \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamKey dirtyDataThreshold \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamKey concurrency \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamKey service_type \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamValue MYSQL \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamKey tenantId \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamValue 1257305158 \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamKey sourceScope \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamValue ALL \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamValue 2568295b-56ac-4a74-8b37-4c8b17545353 \
    --TaskConfiguration.TaskExtConfigurationList.22.ParamKey target_server \
    --TaskConfiguration.TaskExtConfigurationList.22.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.23.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.23.ParamValue {"taskMode":"1","fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.24.ParamKey targetIncrementCondition \
    --TaskConfiguration.TaskExtConfigurationList.24.ParamValue  \
    --TaskConfiguration.DataCluster zaxa \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.YarnQueue default \
    --TaskConfiguration.SourceServiceId ;62175; \
    --TaskConfiguration.TargetServiceId ;61933; \
    --TaskConfiguration.ResourceGroup 20221219061532357712 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174556005"
        },
        "RequestId": "2f5b0f64-32cc-45c1-a63c-f25c630b32aa"
    }
}
```

**Example 8: 任务类型26：OfflineSynchronization （集成任务）代码模式**

任务类型26：OfflineSynchronization （集成任务）代码模式

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName api_etl_code_250829_094215 \
    --TaskBaseAttribute.TaskTypeId 26 \
    --TaskBaseAttribute.WorkflowId 8f9915b8-683c-4732-b0b2-b3a5ff0d90f1 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription 250829_093945 \
    --TaskConfiguration.ResourceGroup 20240927151912348498 \
    --TaskConfiguration.CodeContent eyJjb3JlIjp7InRyYW5zcG9ydCI6eyJjaGFubmVsIjp7InNwZWVkIjp7ImJ5dGUiOi0xfX19fSwiam9iIjp7ImNvbnRlbnQiOlt7InJlYWRlciI6eyJwYXJhbWV0ZXIiOnsicGFzc3dvcmQiOiIqKioqKioiLCJkYXRhc291cmNlIjoibXlzcWxfeXVuXzAzMDQiLCJjb2x1bW4iOlsiKiJdLCJjb25uZWN0aW9uIjpbeyJqZGJjVXJsIjpbImpkYmM6bXlzcWw6Ly8xNzIuMTYuMC43MDozMzA2L3dlZGF0YV90ZXN0P3Jld3JpdGVCYXRjaGVkU3RhdGVtZW50cz10cnVlJnRpbnlJbnQxaXNCaXQ9ZmFsc2Umc2VydmVyVGltZXpvbmU9VVRDJTJCNyZjaGFyYWN0ZXJFbmNvZGluZz11dGY4JmF1dG9SZWNvbm5lY3Q9dHJ1ZSJdLCJ0YWJsZSI6WyJiYXJyeXRlc3QiXX1dLCJ1c2VybmFtZSI6InJvb3QifSwibmFtZSI6Im15c3FscmVhZGVyIn0sInRyYW5zZm9ybWVyIjpbXSwid3JpdGVyIjp7InBhcmFtZXRlciI6eyJwYXNzd29yZCI6IioqKioqKiIsInNlc3Npb24iOlsic2V0IHNlc3Npb24gc3FsX21vZGU9J0FOU0knIl0sImRhdGFzb3VyY2UiOiJteXNxbF95dW5fMDMwNCIsImNvbHVtbiI6WyIqIl0sImNvbm5lY3Rpb24iOlt7ImpkYmNVcmwiOiJqZGJjOm15c3FsOi8vMTcyLjE2LjAuNzA6MzMwNi93ZWRhdGFfdGVzdD9yZXdyaXRlQmF0Y2hlZFN0YXRlbWVudHM9dHJ1ZSZ0aW55SW50MWlzQml0PWZhbHNlJnNlcnZlclRpbWV6b25lPVVUQyUyQjcmY2hhcmFjdGVyRW5jb2Rpbmc9dXRmOCZhdXRvUmVjb25uZWN0PXRydWUiLCJ0YWJsZSI6WyJsYXJnZV90YWJsZSJdfV0sImJhdGNoU2l6ZSI6MjA0OCwidXNlcm5hbWUiOiJyb290Iiwib24iOlsiaWQiXX0sIm5hbWUiOiJteXNxbHdyaXRlciJ9fV0sInNldHRpbmciOnsibWVtb3J5Ijp7InRhc2tMaW1pdCI6MzM1NTQ0MzIwLCJjaGFubmVsTGltaXQiOjY3MTA4ODY0LCJ3cml0ZXJMaW1pdCI6MTM0MjE3NzI4LCJqb2JMaW1pdCI6ODcyNDE1MjMyLCJyZWFkZXJMaW1pdCI6MTM0MjE3NzI4fSwiZXJyb3JMaW1pdCI6eyJyZWNvcmQiOjB9LCJzcGVlZCI6eyJieXRlIjotMSwiY2hhbm5lbCI6MX19fX0= \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey enableDataContrast \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue false \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey target_service_type \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue MYSQL \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey targetScope \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue ALL \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey waitExecutionTotalTTL \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue -1 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey executionTTLStrategy \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue fail \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey target_service \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue 81467 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey dirtyDataThresholdUnit \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue percentage \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey sourceIncrementCondition \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey syncRateLimitUnit \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 81467 \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey calendar_id \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey syncRateLimit \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue -1 \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue 107773e6-088b-45fb-8cbc-ba2bc0c5f906 \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey calendar_open \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamKey calendar_name \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamKey dataContrastRule \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamValue Cnt \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamKey dirtyDataThreshold \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamKey concurrency \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamKey service_type \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamValue MYSQL \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamKey waitExecutionTotalTTLStrategy \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamValue fail \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamKey tenantId \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamValue 1257305158 \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamKey sourceScope \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamValue ALL \
    --TaskConfiguration.TaskExtConfigurationList.22.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.22.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.23.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.23.ParamValue 107773e6-088b-45fb-8cbc-ba2bc0c5f906 \
    --TaskConfiguration.TaskExtConfigurationList.24.ParamKey target_server \
    --TaskConfiguration.TaskExtConfigurationList.24.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.25.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.25.ParamValue {"taskMode":"3","fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.26.ParamKey targetIncrementCondition \
    --TaskConfiguration.TaskExtConfigurationList.26.ParamValue  \
    --TaskConfiguration.DataCluster 107773e6-088b-45fb-8cbc-ba2bc0c5f906 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId ;81467; \
    --TaskConfiguration.TargetServiceId ;81467; \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174556007"
        },
        "RequestId": "31ce344f-2059-4e5e-a938-86c84c89abc3"
    }
}
```

**Example 9: 任务类型26：OfflineSynchronization （集成任务）画布模式**

任务类型26：OfflineSynchronization （集成任务）画布模式

注意：注意 TaskConfiguration.CodeContent 部分为 集成任务配置，传参时，使用Base64编码；


Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2624349095964852224 \
    --TaskBaseAttribute.TaskName api_etl_canvas_250902_122129 \
    --TaskBaseAttribute.TaskTypeId 26 \
    --TaskBaseAttribute.WorkflowId 7c2e7db0-61e1-4f6a-8fb4-0e4d54e206e1 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20230920200643704861 \
    --TaskConfiguration.CodeContent W3siTmFtZSI6ImNzZCIsIk5vZGVUeXBlIjoiT1VUUFVUIiwiRGF0YVNvdXJjZVR5cGUiOiJTRlRQIiwiRGVzY3JpcHRpb24iOm51bGwsIkRhdGFzb3VyY2VJZCI6Ijc5NjYxIiwiUHJvamVjdElkIjoiMCIsIkNyZWF0b3JVaW4iOiIxMDAwMjg1OTY4NDYiLCJPcGVyYXRvclVpbiI6IjEwMDAyODU5Njg0NiIsIk93bmVyVWluIjpudWxsLCJBcHBJZCI6IjEzMTUwNTE3ODkiLCJDb25maWciOlt7Ik5hbWUiOiJUeXBlIiwiVmFsdWUiOiJTRlRQIn0seyJOYW1lIjoiaXNDbGVhbiIsIlZhbHVlIjoiMCJ9LHsiTmFtZSI6IkZpbGVOYW1lIiwiVmFsdWUiOiJ0b0xvd2VyKCdBQiBjJHtmaWxldHJhbnNfZGlfc3JjfScpIn0seyJOYW1lIjoiRmlsZVBhdGgiLCJWYWx1ZSI6Ii9ob21lL2Z0cHVzZXIvdGVzdG1pMiJ9LHsiTmFtZSI6IlN5bmNUeXBlIiwiVmFsdWUiOiJGSUxFIn0seyJOYW1lIjoiZW5hYmxlZE9rRmlsZSIsIlZhbHVlIjoibm8ifSx7Ik5hbWUiOiJjbHVzdGVyRGVwbG95VHlwZSIsIlZhbHVlIjoiIn0seyJOYW1lIjoiZW5jb2RpbmciLCJWYWx1ZSI6InV0Zi04In0seyJOYW1lIjoiZGF0YXNvdXJjZURldkRCIiwiVmFsdWUiOiIifV0sIkV4dENvbmZpZyI6W3siTmFtZSI6IngiLCJWYWx1ZSI6IjMzNyJ9LHsiTmFtZSI6InkiLCJWYWx1ZSI6IjE4MCJ9LHsiTmFtZSI6Imljb25Qb3NpdGlvbiIsIlZhbHVlIjoibGVmdCJ9LHsiTmFtZSI6InNpemUiLCJWYWx1ZSI6Im0ifSx7Ik5hbWUiOiJkaXNUeXBlIiwiVmFsdWUiOiJTRlRQIn1dLCJTY2hlbWEiOm51bGwsIk5vZGVNYXBwaW5nIjp7IlNvdXJjZUlkIjoiMjQyNTY3IiwiU2lua0lkIjoiMjQyNTY2IiwiU291cmNlU2NoZW1hIjpbXSwiRXh0Q29uZmlnIjpbeyJOYW1lIjoiZnJvbU5vZGUiLCJWYWx1ZSI6Im5vZGVfMjQyNTY3In0seyJOYW1lIjoidG9Ob2RlIiwiVmFsdWUiOiJub2RlXzI0MjU2NiJ9LHsiTmFtZSI6ImZyb21Ob2RlQW5jaG9yIiwiVmFsdWUiOiJib3R0b20ifSx7Ik5hbWUiOiJ0b05vZGVBbmNob3IiLCJWYWx1ZSI6InRvcCJ9XSwiU2NoZW1hTWFwcGluZ3MiOltdfSwiQ3JlYXRlVGltZSI6IjIwMjUtMDktMDIgMTE6NDc6MjIiLCJVcGRhdGVUaW1lIjoiMjAyNS0wOS0wMiAxMTo0NzoyMiJ9LHsiTmFtZSI6ImRjc3MiLCJOb2RlVHlwZSI6IklOUFVUIiwiRGF0YVNvdXJjZVR5cGUiOiJTRlRQIiwiRGVzY3JpcHRpb24iOm51bGwsIkRhdGFzb3VyY2VJZCI6Ijc5NjYxIiwiUHJvamVjdElkIjoiMCIsIkNyZWF0b3JVaW4iOiIxMDAwMjg1OTY4NDYiLCJPcGVyYXRvclVpbiI6IjEwMDAyODU5Njg0NiIsIk93bmVyVWluIjpudWxsLCJBcHBJZCI6IjEzMTUwNTE3ODkiLCJDb25maWciOlt7Ik5hbWUiOiJUeXBlIiwiVmFsdWUiOiJTRlRQIn0seyJOYW1lIjoiaXNDbGVhbiIsIlZhbHVlIjoiMCJ9LHsiTmFtZSI6IkZpbGVOYW1lIiwiVmFsdWUiOiJbXCIvaG9tZS9mdHB1c2VyL3Rlc3RtaS8qXCJdIn0seyJOYW1lIjoiU3luY1R5cGUiLCJWYWx1ZSI6IkZJTEUifSx7Ik5hbWUiOiJDb21wcmVzc1R5cGUiLCJWYWx1ZSI6Im5vbmUifSx7Ik5hbWUiOiJza2lwSGVhZGVyIiwiVmFsdWUiOiIwIn0seyJOYW1lIjoiY2x1c3RlckRlcGxveVR5cGUiLCJWYWx1ZSI6IiJ9LHsiTmFtZSI6ImVuY29kaW5nIiwiVmFsdWUiOiJ1dGYtOCJ9LHsiTmFtZSI6ImRhdGFzb3VyY2VEZXZEQiIsIlZhbHVlIjoiIn1dLCJFeHRDb25maWciOlt7Ik5hbWUiOiJ4IiwiVmFsdWUiOiIzMzEifSx7Ik5hbWUiOiJ5IiwiVmFsdWUiOiI3NCJ9LHsiTmFtZSI6Imljb25Qb3NpdGlvbiIsIlZhbHVlIjoibGVmdCJ9LHsiTmFtZSI6InNpemUiLCJWYWx1ZSI6Im0ifSx7Ik5hbWUiOiJkaXNUeXBlIiwiVmFsdWUiOiJTRlRQIn1dLCJTY2hlbWEiOm51bGwsIk5vZGVNYXBwaW5nIjpudWxsLCJDcmVhdGVUaW1lIjoiMjAyNS0wOS0wMiAxMTo0NzoyMiIsIlVwZGF0ZVRpbWUiOiIyMDI1LTA5LTAyIDExOjQ3OjIyIn1d \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 79661 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey target_service_type \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue SFTP \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue a9bc5214-8632-494b-bd83-61c75d4eebac \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey dirtyDataThreshold \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey concurrency \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey service_type \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue SFTP \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey target_service \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue 79661 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue a9bc5214-8632-494b-bd83-61c75d4eebac \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey target_server \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey syncRateLimitUnit \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue {"taskMode":"0","fromMapping":false} \
    --TaskConfiguration.DataCluster a9bc5214-8632-494b-bd83-61c75d4eebac \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId ;79661; \
    --TaskConfiguration.TargetServiceId ;79661; \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.StartTime 2025-02-14 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2025-02-14 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 37 14 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174556004"
        },
        "RequestId": "3464d6c5-014f-43c2-9848-2a27e3f86347"
    }
}
```

**Example 10: 任务类型30：Python**

任务类型30：Python

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2417334454903762944 \
    --TaskBaseAttribute.TaskName py_api_250827_160130 \
    --TaskBaseAttribute.TaskTypeId 30 \
    --TaskBaseAttribute.WorkflowId 1f9e9b2b-5b71-45d3-b3d3-81baaae485dd \
    --TaskBaseAttribute.OwnerUin 100028579801 \
    --TaskBaseAttribute.TaskDescription py_api_250827_160130 \
    --TaskConfiguration.CodeContent cHJpbnQoJ2hlbGxvIHdvcmxkIScp \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey python_type \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey python_sub_version \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey ssmDynamicSkSwitch \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue off \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20240416215649571819 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174556008"
        },
        "RequestId": "109a5835-6798-4662-840d-2221e85e0ceb"
    }
}
```

**Example 11: 任务类型31：PySpark**

任务类型31：PySpark

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2840738091966353408 \
    --TaskBaseAttribute.TaskName api_pyspark_250902_123239 \
    --TaskBaseAttribute.TaskTypeId 31 \
    --TaskBaseAttribute.WorkflowId 5be0a485-63c5-47dc-a618-ddad5890cdb4 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskConfiguration.CodeContent IyBQeXNwYXJrCgpmcm9tIHB5c3Bhcmsuc3FsIGltcG9ydCBTcGFya1Nlc3Npb24KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIGRhdGUKZnJvbSBweXNwYXJrLnNxbCBpbXBvcnQgUm93CiAKc3BhcmsgPSBTcGFya1Nlc3Npb24uYnVpbGRlci5hcHBOYW1lKCdOT1RJQ0U6ZGVuZ2JveHVfaGFuZHNvbWUhISEnKS5nZXRPckNyZWF0ZSgpCiAKZGYgPSBzcGFyay5jcmVhdGVEYXRhRnJhbWUoWwogICAgUm93KGE9MSwgYj0yLiwgYz0nc3RyaW5nMScsIGQ9ZGF0ZSgyMDAwLCAxLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAxLCAxMiwgMCkpLAogICAgUm93KGE9MiwgYj0zLiwgYz0nc3RyaW5nMicsIGQ9ZGF0ZSgyMDAwLCAyLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAyLCAxMiwgMCkpLAogICAgUm93KGE9NCwgYj01LiwgYz0nc3RyaW5nMycsIGQ9ZGF0ZSgyMDAwLCAzLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAzLCAxMiwgMCkpCl0pCiAKcHJpbnQoJy0tLS0tcHlzcGFyayB0ZXN0IHN0YXJ0JykKIApkZi5maWx0ZXIoZGYuYSA9PSAxKS5zaG93KCkKZGYuY3JlYXRlT3JSZXBsYWNlVGVtcFZpZXcoJ3RhYmxlQScpCnNwYXJrLnNxbCgnU0VMRUNUIGNvdW50KCopIGZyb20gdGFibGVBJykuc2hvdygpCiAKcHJpbnQoJy0tLS0tcHlzcGFyayB0ZXN0IGVuZCcp \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey python_type \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey python_sub_version \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster emr-34r7poh0 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.YarnQueue root.default \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-09-02 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557001"
        },
        "RequestId": "635730ac-1c92-4083-80d2-0d66dcf86f4b"
    }
}
```

**Example 12: 任务类型32: DLCSQL**

任务类型32: DLCSQL；
引擎字段 dlcDataEngine 需要通过 https://cloud.tencent.com/document/product/1342/86308  获取;
注意，DLCSQL任务共支持5种引擎类型，对应参数设置不同，dlcEngineType、computeResourceType、IsInherit 三个属性的对应不同引擎类型需要对应设置：
- SuperSQL引擎-SparkSQL（SparkSQL）：SparkSQLTask、nonSparkJob、不用填；
- SuperSQL引擎-Presto（PrestoSQL）：SQLTask、nonSparkJob、不用填；
- SuperSQL引擎-Spark作业（SparkBatch）：sparkJob、sparkJob、1；
- 标准引擎-Spark（StandardSpark）：StandardSpark、nonSparkJob、2；
- 标准引擎-Presto（StandardPresto）：StandardPresto、nonSparkJob、不用填；


Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskBaseAttribute.TaskName api_DLCSQL_32_SparkSQL_250829_1756470787 \
    --TaskBaseAttribute.TaskTypeId 32 \
    --TaskBaseAttribute.WorkflowId 1adcdb07-77fe-4ee6-8d98-1cfcc2cdcfa9 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskConfiguration.CodeContent LS1ETEMgU1FMCi0tKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLS0KLS1hdXRob3I6IHRlc3Q1LWF1dG8tdGVzdDEKLS1jcmVhdGUgdGltZTogMjAyNS0wOC0yOSAxNzoxMDo0MgotLSoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi0tCnNlbGVjdCAxOw== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey dlcDataEngine \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue eyJBY2Nlc3NJbmZvcyI6W3siQWNjZXNzQ29ubmVjdGlvbkluZm9zIjpbImpkYmM6ZGxjOmRsYy50ZW5jZW50Y2xvdWRhcGkuY29tP3Rhc2tfdHlwZT1TcGFya1NRTFRhc2smZGF0YWJhc2VfbmFtZT17RGF0YWJhc2VOYW1lfSZkYXRhc291cmNlX2Nvbm5lY3Rpb25fbmFtZT1EYXRhTGFrZUNhdGFsb2cmcmVnaW9uPWFwLXNoYW5naGFpJmRhdGFfZW5naW5lX25hbWU9d2VkYXRhLWRpLWVuZ2luZSZyZXN1bHRfdHlwZT17UmVzdWx0VHlwZX0mcmVhZF90eXBlPXtSZWFkVHlwZX0iXSwiQWNjZXNzVHlwZSI6IkRMQ0pEQkMifV0sIkF1dG9BdXRob3JpemF0aW9uIjp0cnVlLCJBdXRvUmVzdW1lIjpmYWxzZSwiQXV0b1N1c3BlbmQiOmZhbHNlLCJBdXRvU3VzcGVuZFRpbWUiOjEwLCJDaGlsZEltYWdlVmVyc2lvbklkIjoiZGMwNDUyZTMtOTdkZi00ZDY4LTg2NmItZTMxY2U2NWEwYTMyIiwiQ2lkckJsb2NrIjoiMTAuMjU1LjAuMC8xNiIsIkNsdXN0ZXJUeXBlIjoic3BhcmtfY3UiLCJDcmVhdGVUaW1lIjoxNzQxMjQ5ODk3LCJDcm9udGFiUmVzdW1lU3VzcGVuZCI6MCwiQ3JvbnRhYlJlc3VtZVN1c3BlbmRTdHJhdGVneSI6eyJSZXN1bWVUaW1lIjoiIiwiU3VzcGVuZFN0cmF0ZWd5IjowLCJTdXNwZW5kVGltZSI6IiJ9LCJEYXRhRW5naW5lSWQiOiJEYXRhRW5naW5lLWJwaHNyNGhkIiwiRGF0YUVuZ2luZU5hbWUiOiJ3ZWRhdGEtZGktZW5naW5lIiwiRGVmYXVsdERhdGFFbmdpbmUiOmZhbHNlLCJEZWZhdWx0SG91c2UiOmZhbHNlLCJFbGFzdGljTGltaXQiOjAsIkVsYXN0aWNTd2l0Y2giOmZhbHNlLCJFbmdpbmVFeGVjVHlwZSI6IlNRTCIsIkVuZ2luZUdlbmVyYXRpb24iOiJTdXBlclNRTCIsIkVuZ2luZU5ldHdvcmtJZCI6IiIsIkVuZ2luZU5ldHdvcmtOYW1lIjoiIiwiRW5naW5lUmVzb3VyY2VHcm91cENvdW50IjowLCJFbmdpbmVSZXNvdXJjZVVzZWRDVSI6MCwiRW5naW5lVHlwZSI6InNwYXJrIiwiRW5naW5lVHlwZURldGFpbCI6IlNwYXJrU1FMIiwiRXhwaXJlVGltZSI6IjAiLCJHYXRld2F5SWQiOiIiLCJHYXRld2F5U3RhdGUiOjAsIklkIjowLCJJbWFnZVZlcnNpb25JZCI6IjdhYzljYzc4LWJjOTUtNDQwZi05NzY4LTRmNGE3OTA0ODc1NSIsIkltYWdlVmVyc2lvbk5hbWUiOiJTdXBlclNRTC1TIDEuMCIsIklzQUlFbmdpbmUiOjAsIklzQUlHYXRld2F5IjpmYWxzZSwiSXNQb29sTW9kZSI6bnVsbCwiSXNTdXBwb3J0QUkiOmZhbHNlLCJJc29sYXRlZFRpbWUiOiIwIiwiTWF4Q2x1c3RlcnMiOjIsIk1heENvbmN1cnJlbmN5Ijo1LCJNZXNzYWdlIjoiIiwiTWluQ2x1c3RlcnMiOjEsIk1vZGUiOjEsIk5ldHdvcmtDb25uZWN0aW9uU2V0IjpbXSwiUGVybWlzc2lvbnMiOlsiVVNFIiwiTU9ESUZZIiwiT1BFUkFURSIsIk1PTklUT1IiLCJERUxFVEUiXSwiUXVvdGFJZCI6IiIsIlJlbmV3RmxhZyI6MCwiUmVzb3VyY2VUeXBlIjoiU3RhbmRhcmRfQ1UiLCJSZXZlcnNhbFRpbWUiOiIwIiwiU2NoZWR1bGVFbGFzdGljaXR5Q29uZiI6eyJTY2hlZHVsZVR5cGUiOiIiLCJTY2hlZHVsZWRFbGFzdGljaXR5RW5hYmxlZCI6ZmFsc2UsIlRpbWVab25lIjoiIn0sIlNlcnZpY2VUeXBlIjoiRExDIiwiU2Vzc2lvblJlc291cmNlVGVtcGxhdGUiOnsiRHJpdmVyU2l6ZSI6InNtYWxsIiwiRXhlY3V0b3JNYXhOdW1iZXJzIjoxLCJFeGVjdXRvck51bXMiOjEsIkV4ZWN1dG9yU2l6ZSI6InNtYWxsIn0sIlNpemUiOjY0LCJTcGVuZEFmdGVyIjowLCJTdGFydFN0YW5kYnlDbHVzdGVyIjpmYWxzZSwiU3RhdGUiOjIsIlN1YkFjY291bnRVaW4iOiIxMDAwMjk0MTEwNTYiLCJUYWdMaXN0IjpbXSwiVG9sZXJhYmxlUXVldWVUaW1lIjowLCJVaVVSTCI6Ii0xIiwiVXBkYXRlVGltZSI6MTc1MTYyOTg0NiwiVXNlckFsaWFzIjoiQVVUT19URVNUIiwiVXNlckFwcElkIjoxMzE1MDUxNzg5LCJVc2VyVWluIjoiMTAwMDI4NDQ4OTAzIiwiVnBjSW5mbyI6IntcIlZwY0lkXCI6XCJ2cGMtcHIxcDk1dHlcIixcIlZwY0NpZHJCbG9ja1wiOlwiMTAuMjU1LjAuMC8xNlwiLFwiU3VibmV0SWRzXCI6W1wic3VibmV0LTdxZ3h4MGVwXCIsXCJzdWJuZXQtYTE1ajk3bGZcIixcInN1Ym5ldC1tMDFqbHB5elwiLFwic3VibmV0LTI2Z281Y3JqXCJdLFwiUHJpdmF0ZUxpbmtJbmZvXCI6e1wiVmlwXCI6XCIxMC4yNTUuMC4zXCIsXCJFbmRwb2ludElkXCI6XCJ2cGNlLTZlbm1saWYxXCJ9LFwiU2VjdXJpdHlHcm91cElkXCI6XCJzZy1jNzZ5andnMFwiLFwiVmlydHVhbFNlY3VyaXR5R3JvdXBJZFwiOlwiXCIsXCJFbmlTdWJuZXRJZHNcIjpudWxsLFwiRW50ZXJwcmlzZUdhdGV3YXlKbnNnd0NvbmZpZ1wiOm51bGx9IiwicmVnaW9uIjoiYXAtc2hhbmdoYWkifQ== \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey runConfParams \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey computeResourceType \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue nonSparkJob \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 73170 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey cmdargsEni \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey dlcEngineType \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue SparkSQLTask \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey computeResource \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue wedata-di-engine \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey dlc_region \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue ap-shanghai \
    --TaskConfiguration.DataCluster ff4fl7vc \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId ;73170; \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557004"
        },
        "RequestId": "c5379ad7-c098-4421-9f04-a77c59918195"
    }
}
```

**Example 13: 任务类型33：Impala**

任务类型33：Impala

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName test306 \
    --TaskBaseAttribute.TaskTypeId 33 \
    --TaskBaseAttribute.WorkflowId a9ef8153-2291-4b60-8b57-3364a384df69 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription 251206_152734 \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskConfiguration.CodeContent LS1KREJDIFNRTAotLSoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi0tCi0tYXV0aG9yOiBzb2xvbW9uZGVuZwotLWNyZWF0ZSB0aW1lOiAyMDI1LTA4LTI5IDEwOjMzOjI4Ci0tKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLS0Kc2VsZWN0IDEzNDQyOw== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 69049 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster emr-34r7poh0 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId 69049 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557003"
        },
        "RequestId": "0cb2f271-2ba8-48fd-8246-8f486af163fa"
    }
}
```

**Example 14: 任务类型34：Hive SQL**

任务类型34：Hive SQL

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName test510 \
    --TaskBaseAttribute.TaskTypeId 34 \
    --TaskBaseAttribute.WorkflowId a9ef8153-2291-4b60-8b57-3364a384df69 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription 251206_152846 \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskConfiguration.CodeContent LS1KREJDIFNRTAotLSoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi0tCi0tYXV0aG9yOiBzb2xvbW9uZGVuZwotLWNyZWF0ZSB0aW1lOiAyMDI1LTA4LTI5IDEwOjMzOjI4Ci0tKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLS0Kc2VsZWN0IDEzNDQyOw== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 73001 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey specLabelConfItems \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ== \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 97dabaad-83f4-40d2-9e94-bca95d5ca50b \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster 97dabaad-83f4-40d2-9e94-bca95d5ca50b \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId 73001 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557008"
        },
        "RequestId": "24fea8f8-6314-4634-8531-1b4421e96f27"
    }
}
```

**Example 15: 任务类型35：Shell**

任务类型35：Shell

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 1486804694126882816 \
    --TaskBaseAttribute.TaskName sh_api_250919_173319 \
    --TaskBaseAttribute.TaskTypeId 35 \
    --TaskBaseAttribute.WorkflowId 82a5d67e-7c51-4b6e-808a-8e286646bf77 \
    --TaskConfiguration.CodeContent ZWNobyAx \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue {"fromMapping":false} \
    --TaskConfiguration.BrokerIp any \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557002"
        },
        "RequestId": "f86523f9-6be3-46e8-ad0d-539f75eb4364"
    }
}
```

**Example 16: 任务类型36：Spark SQL**

任务类型36：Spark SQL

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2224252741354745856 \
    --TaskBaseAttribute.TaskName test251206_153315 \
    --TaskBaseAttribute.TaskTypeId 36 \
    --TaskBaseAttribute.WorkflowId 9ebc375d-4312-49d4-a987-a8d7d786e389 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription 251206_153218 \
    --TaskConfiguration.ResourceGroup 20231128145802713926 \
    --TaskConfiguration.CodeContent c2VsZWN0IDEzNDQyOw== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 69047 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster emr-34r7poh0 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId 69047 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557007"
        },
        "RequestId": "ec45ad2e-2db2-464b-bc10-4ab91b689d00"
    }
}
```

**Example 17: 任务类型38：Shell Form Mode（SHELL表单模式）**

任务类型38：Shell Form Mode（SHELL表单模式）

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2224252741354745856 \
    --TaskBaseAttribute.TaskName test820 \
    --TaskBaseAttribute.TaskTypeId 38 \
    --TaskBaseAttribute.WorkflowId 9ebc375d-4312-49d4-a987-a8d7d786e389 \
    --TaskBaseAttribute.OwnerUin 100028596846 \
    --TaskBaseAttribute.TaskDescription 251206_153647 \
    --TaskConfiguration.ResourceGroup 20231128145802713926 \
    --TaskConfiguration.CodeContent  \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey ftp.file.name \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue /datastudio/resource/2224252741354745856/echo.zip \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey shell.cmd \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue echo.sh \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey shell.args \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 000-zzz-1315051789 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue ap-beijing \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster  \
    --TaskConfiguration.BrokerIp any \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558003"
        },
        "RequestId": "12ba825a-d7ca-4846-a316-7024ecf434a2"
    }
}
```

**Example 18: 任务类型39：Spark（jar）**

任务类型39：Spark（jar）

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2224252741354745856 \
    --TaskBaseAttribute.TaskName spark_jar \
    --TaskBaseAttribute.TaskTypeId 39 \
    --TaskBaseAttribute.WorkflowId fb2a9bce-7704-4812-a268-ba593201e97c \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription spark_jar_20250828 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey properties \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue driver-memory=4g \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey ftp.file.name \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue /datastudio/resource/2224252741354745856/spark-examples_2.12-3.1.3.jar \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey engine.ext.className \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue org.apache.spark.examples.SparkPi \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey engine.ext.parameter \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue -sql show tables \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey engine.ext.jars \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue cosn://barry-1315051789/datastudio/resource/2224252741354745856/udf-demo-1.0-SNAPSHOT.jar \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey engine.ext.pyFiles \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue cosn://autotest-guangzhou-1315051789/datastudio/resource/2224252741354745856/demo.py \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey engine.ext.files \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue cosn://000-zzz-1315051789/datastudio/resource/2224252741354745856/hadoop-mapreduce-examples.zip \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey engine.ext.conf \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue spark.dynamicAllocation.enabled=true \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 000-zzz-1315051789 \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue ap-beijing \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue emr-34r7poh0 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.YarnQueue default \
    --TaskConfiguration.ResourceGroup 20231124174433263533 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557007"
        },
        "RequestId": "ec45ad2e-2db2-464b-bc10-4ab91b689d00"
    }
}
```

**Example 19: 任务类型39：Spark（py）**

任务类型39：Spark（py）

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2224252741354745856 \
    --TaskBaseAttribute.TaskName spark_py_0828 \
    --TaskBaseAttribute.TaskTypeId 39 \
    --TaskBaseAttribute.WorkflowId fb2a9bce-7704-4812-a268-ba593201e97c \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription spark_py_20250828 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey engine.ext.files \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey calendar_open \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 000-zzz-1315051789 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey engine.ext.pyFiles \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey engine.ext.className \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey ftp.file.name \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue /datastudio/resource/2224252741354745856/sdfs_dfsdw.py \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey engine.ext.conf \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey engine.ext.jars \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue ap-guangzhou \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey engine.ext.archives \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey properties \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey engine.ext.parameter \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamValue {"fromMapping":false} \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.YarnQueue default \
    --TaskConfiguration.ResourceGroup 20231124174433263533 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558003"
        },
        "RequestId": "12ba825a-d7ca-4846-a316-7024ecf434a2"
    }
}
```

**Example 20: 任务类型39：Spark（zip）**

任务类型39：Spark（zip）

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2224252741354745856 \
    --TaskBaseAttribute.TaskName spark_zip_0828 \
    --TaskBaseAttribute.TaskTypeId 39 \
    --TaskBaseAttribute.WorkflowId fb2a9bce-7704-4812-a268-ba593201e97c \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription spark_zip_20250828 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey properties \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue --num.executors 10 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey shell.args \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue --class org.apache.spark.examples.SparkPi spark-examples_2.12-3.3.1.jar \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey ftp.file.name \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue /datastudio/resource/2224252741354745856/spark-examples_2.12-3.3.1.zip \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 000-zzz-1315051789 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue ap-guangzhou \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue emr-34r7poh0 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.YarnQueue default \
    --TaskConfiguration.ResourceGroup 20231124174433263533 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558004"
        },
        "RequestId": "4b233f6e-b5a8-44f2-940c-d2410cedfe84"
    }
}
```

**Example 21: 任务类型40：TCHouse-P**

任务类型40：TCHouse-P

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2224252741354745856 \
    --TaskBaseAttribute.TaskName tchouse_p_0828 \
    --TaskBaseAttribute.TaskTypeId 40 \
    --TaskBaseAttribute.WorkflowId fb2a9bce-7704-4812-a268-ba593201e97c \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription tchouse_p_0828 \
    --TaskConfiguration.CodeContent c2hvdyB0YWJsZXM7 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 40659 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey databaseName \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue postgres \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey python_type \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue cdwpg-vmnm6o5y \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue wedata-fusion-test1-125730xxxx \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey sql.file.name \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue https://wedata-fusion-test1-125730xxxx.cos.ap-beijing.myqcloud.com/datastudio/project/2224252741354745856/qminliu/qmopenapi/qm_tc.sql \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue ap-beijing \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue cdwpg-vmnm6o5y \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue {"fromMapping":false} \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20231124174433263533 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174557007"
        },
        "RequestId": "ec45ad2e-2db2-464b-bc10-4ab91b689d00"
    }
}
```

**Example 22: 任务类型41: Kettle**

任务类型41: Kettle

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2658184615822913536 \
    --TaskBaseAttribute.TaskName kettle_0829 \
    --TaskBaseAttribute.TaskTypeId 41 \
    --TaskBaseAttribute.WorkflowId 31657042-6665-43ad-a85d-c7789962a844 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription kettle_0829 \
    --TaskConfiguration.ResourceGroup 20250524165457277726 \
    --TaskConfiguration.CodeContent  \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey kettle.cmd \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue sh " < installPath > /pan.sh" -rep "<repoName>" -user "<userName>" -pass "<password>" -dir "/home" -trans " trans1_250901.ktr " \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey dlcJobData \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey kettle.file.name \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue /home/trans1_250901.ktr \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue {"fromMapping":false} \
    --TaskConfiguration.BrokerIp any \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558005"
        },
        "RequestId": "ff9645aa-dd2b-4025-80fb-31206f0f2f78"
    }
}
```

**Example 23: 任务类型42：Tchouse-X**

任务类型42：Tchouse-X

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2658184615822913536 \
    --TaskBaseAttribute.TaskName tchouse_x_0829 \
    --TaskBaseAttribute.TaskTypeId 42 \
    --TaskBaseAttribute.WorkflowId 31657042-6665-43ad-a85d-c7789962a844 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription tchouse_x_0829 \
    --TaskConfiguration.ResourceGroup 20250524165457277726 \
    --TaskConfiguration.CodeContent  \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 66258 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey engine.resourcePath \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue cosn://1219-agent-1315051789/datastudio/resource/2658184615822913536/aa1a.jar \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue instance-vg8a6s3h \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey fieldDesc \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue eyJyZXNvdXJjZVBhdGgiOiLnqIvluo/ljIUiLCJjbGFzc05hbWUiOiLkuLvnsbsoTWFpbiBDbGFzcykiLCJqYXJzIjoi5L6d6LWWSkFS6LWE5rqQKC0tamFycykiLCJwYXJhbWV0ZXIiOiLnqIvluo/lhaXlj6Plj4LmlbAiLCJjb25mIjoi5L2c5Lia5Y+C5pWwKC0tY29uZmlnKSIsImZpbGVzIjoi5L6d6LWWRmlsZXPotYTmupAoLS1maWxlcykiLCJhcmNoaXZlcyI6IuS+nei1lkFyY2hpdmVz6LWE5rqQKC0tYXJjaGl2ZXMpIiwicHlGaWxlcyI6IuS+nei1llB5dGhvbui1hOa6kCJ9 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey engine.driverCores \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey engine.ext.className \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue class org.apache.spark.examples.SparkPi \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey engine.numExecutors \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue 20 \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey waitExecutionTotalTTLStrategy \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue fail \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey engine.executorCores \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue instance-vg8a6s3h \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue {"fromMapping":false} \
    --TaskConfiguration.BrokerIp any \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558007"
        },
        "RequestId": "4c44ef38-55ad-46a7-a257-554c47d1758e"
    }
}
```

**Example 24: 任务类型43：TCHouse-X SQL**

任务类型43：TCHouse-X SQL

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2224252741354745856 \
    --TaskBaseAttribute.TaskName tchouse_x_sql_qq \
    --TaskBaseAttribute.TaskTypeId 43 \
    --TaskBaseAttribute.WorkflowId fb2a9bce-7704-4812-a268-ba593201e97c \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription tchouse_x_sql_qq \
    --TaskConfiguration.CodeContent LS1UQ0hvdXNlLVggU1FMCi0tKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLS0KLS1hdXRob3I6IHNvbG9tb25kZW5nCi0tY3JlYXRlIHRpbWU6IDIwMjUtMDgtMjggMTk6NDE6NTEKLS0qKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiotLQotLeS9v+eUqFRDSG91c2UtWCBTUUznmoTnprvnur/mlbDmja7lpITnkIblvJXmk47vvIxTUUzmnIDliY3pnaLpnIDopoHmt7vliqAgLyorZW5naW5lPWJhdGNoKi8tLQpzaG93IHRhYmxlczs= \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 83112 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey python_type \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue warehouse-88ffei8j \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey engine.virtualCluster \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue warehouse01 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue default \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue ap-beijing \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue warehouse-88ffei8j \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue {"fromMapping":false} \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20231124174433263533 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558002"
        },
        "RequestId": "3ee8e50f-66d7-4800-bac9-6471c15599eb"
    }
}
```

**Example 25: 任务类型46：DLC Spark（SuperSQL引擎-Spark作业（jar））**

任务类型46：DLC Spark（SuperSQL引擎-Spark作业（jar））

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskBaseAttribute.TaskName api_DLCSPARK_46_jar_SparkBatch_250829_1756474473 \
    --TaskBaseAttribute.TaskTypeId 46 \
    --TaskBaseAttribute.WorkflowId 1adcdb07-77fe-4ee6-8d98-1cfcc2cdcfa9 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey job_type \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey dlc_region \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue ap-shanghai \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey dlcDataEngine \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue eyJBY2Nlc3NJbmZvcyI6W3siQWNjZXNzQ29ubmVjdGlvbkluZm9zIjpbImpkYmM6ZGxjOmRsYy50ZW5jZW50Y2xvdWRhcGkuY29tP3Rhc2tfdHlwZT1CYXRjaFNRTFRhc2smZGF0YWJhc2VfbmFtZT17RGF0YWJhc2VOYW1lfSZkYXRhc291cmNlX2Nvbm5lY3Rpb25fbmFtZT1EYXRhTGFrZUNhdGFsb2cmcmVnaW9uPWFwLXNoYW5naGFpJmRhdGFfZW5naW5lX25hbWU95rWL6K+V5LiT55SoX0FVVE9URVNUX+WLv+WIoCZyZXN1bHRfdHlwZT17UmVzdWx0VHlwZX0mcmVhZF90eXBlPXtSZWFkVHlwZX0iXSwiQWNjZXNzVHlwZSI6IkRMQ0pEQkMifV0sIkF1dG9BdXRob3JpemF0aW9uIjp0cnVlLCJBdXRvUmVzdW1lIjpmYWxzZSwiQXV0b1N1c3BlbmQiOmZhbHNlLCJBdXRvU3VzcGVuZFRpbWUiOjEwLCJDaGlsZEltYWdlVmVyc2lvbklkIjoiMmFkOTc5MjgtM2M1MC00ZGE2LWJlMjItNzk5N2NkYmZlZmQ3IiwiQ2lkckJsb2NrIjoiMTAuMjU1LjAuMC8xNiIsIkNsdXN0ZXJUeXBlIjoic3BhcmtfY3UiLCJDcmVhdGVUaW1lIjoxNzUwMzMwMDAwLCJDcm9udGFiUmVzdW1lU3VzcGVuZCI6MCwiQ3JvbnRhYlJlc3VtZVN1c3BlbmRTdHJhdGVneSI6eyJSZXN1bWVUaW1lIjoiIiwiU3VzcGVuZFN0cmF0ZWd5IjowLCJTdXNwZW5kVGltZSI6IiJ9LCJEYXRhRW5naW5lSWQiOiJEYXRhRW5naW5lLTBmcWlhOTdqIiwiRGF0YUVuZ2luZU5hbWUiOiLmtYvor5XkuJPnlKhfQVVUT1RFU1Rf5Yu/5YigIiwiRGVmYXVsdERhdGFFbmdpbmUiOmZhbHNlLCJEZWZhdWx0SG91c2UiOmZhbHNlLCJFbGFzdGljTGltaXQiOjAsIkVsYXN0aWNTd2l0Y2giOmZhbHNlLCJFbmdpbmVFeGVjVHlwZSI6IkJBVENIIiwiRW5naW5lR2VuZXJhdGlvbiI6IlN1cGVyU1FMIiwiRW5naW5lTmV0d29ya0lkIjoiIiwiRW5naW5lTmV0d29ya05hbWUiOiIiLCJFbmdpbmVSZXNvdXJjZUdyb3VwQ291bnQiOjAsIkVuZ2luZVJlc291cmNlVXNlZENVIjowLCJFbmdpbmVUeXBlIjoic3BhcmsiLCJFbmdpbmVUeXBlRGV0YWlsIjoiU3BhcmtCYXRjaCIsIkV4cGlyZVRpbWUiOiIwIiwiR2F0ZXdheUlkIjoiIiwiR2F0ZXdheVN0YXRlIjowLCJJZCI6MCwiSW1hZ2VWZXJzaW9uSWQiOiJiZmFkNGViYS01NGMzLTQzZTktOGI0MC0yNGVjZDQ4OGNkNzciLCJJbWFnZVZlcnNpb25OYW1lIjoiU3BhcmsgMy4yIiwiSXNBSUVuZ2luZSI6MCwiSXNBSUdhdGV3YXkiOmZhbHNlLCJJc1Bvb2xNb2RlIjpudWxsLCJJc1N1cHBvcnRBSSI6ZmFsc2UsIklzb2xhdGVkVGltZSI6IjAiLCJNYXhDbHVzdGVycyI6MSwiTWF4Q29uY3VycmVuY3kiOjUsIk1lc3NhZ2UiOiIiLCJNaW5DbHVzdGVycyI6MSwiTW9kZSI6MSwiTmV0d29ya0Nvbm5lY3Rpb25TZXQiOltdLCJQZXJtaXNzaW9ucyI6WyJVU0UiLCJNT0RJRlkiLCJPUEVSQVRFIiwiTU9OSVRPUiIsIkRFTEVURSJdLCJRdW90YUlkIjoiIiwiUmVuZXdGbGFnIjowLCJSZXNvdXJjZVR5cGUiOiJTdGFuZGFyZF9DVSIsIlJldmVyc2FsVGltZSI6IjAiLCJTY2hlZHVsZUVsYXN0aWNpdHlDb25mIjp7IlNjaGVkdWxlVHlwZSI6IiIsIlNjaGVkdWxlZEVsYXN0aWNpdHlFbmFibGVkIjpmYWxzZSwiVGltZVpvbmUiOiIifSwiU2VydmljZVR5cGUiOiJETEMiLCJTZXNzaW9uUmVzb3VyY2VUZW1wbGF0ZSI6eyJEcml2ZXJTaXplIjoic21hbGwiLCJFeGVjdXRvck1heE51bWJlcnMiOjEsIkV4ZWN1dG9yTnVtcyI6MSwiRXhlY3V0b3JTaXplIjoic21hbGwifSwiU2l6ZSI6MTI4LCJTcGVuZEFmdGVyIjowLCJTdGFydFN0YW5kYnlDbHVzdGVyIjpmYWxzZSwiU3RhdGUiOjIsIlN1YkFjY291bnRVaW4iOiIxMDAwMjk0MTEwNTYiLCJUYWdMaXN0IjpbXSwiVG9sZXJhYmxlUXVldWVUaW1lIjowLCJVaVVSTCI6Ii0xIiwiVXBkYXRlVGltZSI6MTc1MTYzMDgxNCwiVXNlckFsaWFzIjoiQVVUT19URVNUIiwiVXNlckFwcElkIjoxMzE1MDUxNzg5LCJVc2VyVWluIjoiMTAwMDI4NDQ4OTAzIiwiVnBjSW5mbyI6IntcIlZwY0lkXCI6XCJ2cGMtMzYzczR2M2FcIixcIlZwY0NpZHJCbG9ja1wiOlwiMTAuMjU1LjAuMC8xNlwiLFwiU3VibmV0SWRzXCI6W1wic3VibmV0LW5nYXFxeGY5XCIsXCJzdWJuZXQtYzlrNzR3bXJcIixcInN1Ym5ldC04bWt4a2d4bFwiLFwic3VibmV0LWI0dGZ4cGIzXCJdLFwiUHJpdmF0ZUxpbmtJbmZvXCI6e1wiVmlwXCI6XCIxMC4yNTUuMC4xM1wiLFwiRW5kcG9pbnRJZFwiOlwidnBjZS1pc2RmbzQ4dlwifSxcIlNlY3VyaXR5R3JvdXBJZFwiOlwic2ctYzc2eWp3ZzBcIixcIlZpcnR1YWxTZWN1cml0eUdyb3VwSWRcIjpcIlwiLFwiRW5pU3VibmV0SWRzXCI6bnVsbCxcIkVudGVycHJpc2VHYXRld2F5Sm5zZ3dDb25maWdcIjpudWxsfSJ9 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey dlcSparkAppPyFiles \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey dataEngine \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 测试专用_AUTOTEST_勿删 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey roleArn \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue 1131 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey dlcSparkCmdArgsV2 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue 100 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey dlcSparkMainClass \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue org.apache.spark.examples.SparkPi \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey dlcSparkAppConf \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 73170 \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey cmdargsEni \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey dlcSparkTaskVersion \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue 2 \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey dlcSparkAppJars \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamKey dlcJobData \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamKey dlcSparkAppFiles \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamKey dlcSparkAppArchives \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamKey dlcSparkAppFile \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamValue cosn://0-1315051789/datastudio/resource/2917455276892352512/0zl/spark-examples_2.12-3.1.3.jar \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamKey IsInherit \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamValue {"taskMode":"1","fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamKey spark_cmd_args \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamValue 100 \
    --TaskConfiguration.DataCluster ff4fl7vc \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId ;73170; \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174559002"
        },
        "RequestId": "d15c7f44-e8a2-4560-b61f-35f35ebfb4ab"
    }
}
```

**Example 26: 任务类型46：DLC Spark（SuperSQL引擎-Spark作业（py））**

注意：支持 SuperSQL引擎-Spark作业、标准引擎-Spark 两种引擎，需要2类用例，且区分 程序包类型 py 和 jar；字段说明：

引擎字段 dlcDataEngine 需要通过 https://cloud.tencent.com/document/product/1342/86308 ;

数据访问策略对应的角色编号 roleArn 需要通过 https://cloud.tencent.com/document/product/1342/96019



Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskBaseAttribute.TaskName api_DLCSPARK_46_py_SparkBatch_250829_1756473151 \
    --TaskBaseAttribute.TaskTypeId 46 \
    --TaskBaseAttribute.WorkflowId 1adcdb07-77fe-4ee6-8d98-1cfcc2cdcfa9 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey job_type \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey dlc_region \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue ap-shanghai \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey dlcDataEngine \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue eyJBY2Nlc3NJbmZvcyI6W3siQWNjZXNzQ29ubmVjdGlvbkluZm9zIjpbImpkYmM6ZGxjOmRsYy50ZW5jZW50Y2xvdWRhcGkuY29tP3Rhc2tfdHlwZT1CYXRjaFNRTFRhc2smZGF0YWJhc2VfbmFtZT17RGF0YWJhc2VOYW1lfSZkYXRhc291cmNlX2Nvbm5lY3Rpb25fbmFtZT1EYXRhTGFrZUNhdGFsb2cmcmVnaW9uPWFwLXNoYW5naGFpJmRhdGFfZW5naW5lX25hbWU95rWL6K+V5LiT55SoX0FVVE9URVNUX+WLv+WIoCZyZXN1bHRfdHlwZT17UmVzdWx0VHlwZX0mcmVhZF90eXBlPXtSZWFkVHlwZX0iXSwiQWNjZXNzVHlwZSI6IkRMQ0pEQkMifV0sIkF1dG9BdXRob3JpemF0aW9uIjp0cnVlLCJBdXRvUmVzdW1lIjpmYWxzZSwiQXV0b1N1c3BlbmQiOmZhbHNlLCJBdXRvU3VzcGVuZFRpbWUiOjEwLCJDaGlsZEltYWdlVmVyc2lvbklkIjoiMmFkOTc5MjgtM2M1MC00ZGE2LWJlMjItNzk5N2NkYmZlZmQ3IiwiQ2lkckJsb2NrIjoiMTAuMjU1LjAuMC8xNiIsIkNsdXN0ZXJUeXBlIjoic3BhcmtfY3UiLCJDcmVhdGVUaW1lIjoxNzUwMzMwMDAwLCJDcm9udGFiUmVzdW1lU3VzcGVuZCI6MCwiQ3JvbnRhYlJlc3VtZVN1c3BlbmRTdHJhdGVneSI6eyJSZXN1bWVUaW1lIjoiIiwiU3VzcGVuZFN0cmF0ZWd5IjowLCJTdXNwZW5kVGltZSI6IiJ9LCJEYXRhRW5naW5lSWQiOiJEYXRhRW5naW5lLTBmcWlhOTdqIiwiRGF0YUVuZ2luZU5hbWUiOiLmtYvor5XkuJPnlKhfQVVUT1RFU1Rf5Yu/5YigIiwiRGVmYXVsdERhdGFFbmdpbmUiOmZhbHNlLCJEZWZhdWx0SG91c2UiOmZhbHNlLCJFbGFzdGljTGltaXQiOjAsIkVsYXN0aWNTd2l0Y2giOmZhbHNlLCJFbmdpbmVFeGVjVHlwZSI6IkJBVENIIiwiRW5naW5lR2VuZXJhdGlvbiI6IlN1cGVyU1FMIiwiRW5naW5lTmV0d29ya0lkIjoiIiwiRW5naW5lTmV0d29ya05hbWUiOiIiLCJFbmdpbmVSZXNvdXJjZUdyb3VwQ291bnQiOjAsIkVuZ2luZVJlc291cmNlVXNlZENVIjowLCJFbmdpbmVUeXBlIjoic3BhcmsiLCJFbmdpbmVUeXBlRGV0YWlsIjoiU3BhcmtCYXRjaCIsIkV4cGlyZVRpbWUiOiIwIiwiR2F0ZXdheUlkIjoiIiwiR2F0ZXdheVN0YXRlIjowLCJJZCI6MCwiSW1hZ2VWZXJzaW9uSWQiOiJiZmFkNGViYS01NGMzLTQzZTktOGI0MC0yNGVjZDQ4OGNkNzciLCJJbWFnZVZlcnNpb25OYW1lIjoiU3BhcmsgMy4yIiwiSXNBSUVuZ2luZSI6MCwiSXNBSUdhdGV3YXkiOmZhbHNlLCJJc1Bvb2xNb2RlIjpudWxsLCJJc1N1cHBvcnRBSSI6ZmFsc2UsIklzb2xhdGVkVGltZSI6IjAiLCJNYXhDbHVzdGVycyI6MSwiTWF4Q29uY3VycmVuY3kiOjUsIk1lc3NhZ2UiOiIiLCJNaW5DbHVzdGVycyI6MSwiTW9kZSI6MSwiTmV0d29ya0Nvbm5lY3Rpb25TZXQiOltdLCJQZXJtaXNzaW9ucyI6WyJVU0UiLCJNT0RJRlkiLCJPUEVSQVRFIiwiTU9OSVRPUiIsIkRFTEVURSJdLCJRdW90YUlkIjoiIiwiUmVuZXdGbGFnIjowLCJSZXNvdXJjZVR5cGUiOiJTdGFuZGFyZF9DVSIsIlJldmVyc2FsVGltZSI6IjAiLCJTY2hlZHVsZUVsYXN0aWNpdHlDb25mIjp7IlNjaGVkdWxlVHlwZSI6IiIsIlNjaGVkdWxlZEVsYXN0aWNpdHlFbmFibGVkIjpmYWxzZSwiVGltZVpvbmUiOiIifSwiU2VydmljZVR5cGUiOiJETEMiLCJTZXNzaW9uUmVzb3VyY2VUZW1wbGF0ZSI6eyJEcml2ZXJTaXplIjoic21hbGwiLCJFeGVjdXRvck1heE51bWJlcnMiOjEsIkV4ZWN1dG9yTnVtcyI6MSwiRXhlY3V0b3JTaXplIjoic21hbGwifSwiU2l6ZSI6MTI4LCJTcGVuZEFmdGVyIjowLCJTdGFydFN0YW5kYnlDbHVzdGVyIjpmYWxzZSwiU3RhdGUiOjIsIlN1YkFjY291bnRVaW4iOiIxMDAwMjk0MTEwNTYiLCJUYWdMaXN0IjpbXSwiVG9sZXJhYmxlUXVldWVUaW1lIjowLCJVaVVSTCI6Ii0xIiwiVXBkYXRlVGltZSI6MTc1MTYzMDgxNCwiVXNlckFsaWFzIjoiQVVUT19URVNUIiwiVXNlckFwcElkIjoxMzE1MDUxNzg5LCJVc2VyVWluIjoiMTAwMDI4NDQ4OTAzIiwiVnBjSW5mbyI6IntcIlZwY0lkXCI6XCJ2cGMtMzYzczR2M2FcIixcIlZwY0NpZHJCbG9ja1wiOlwiMTAuMjU1LjAuMC8xNlwiLFwiU3VibmV0SWRzXCI6W1wic3VibmV0LW5nYXFxeGY5XCIsXCJzdWJuZXQtYzlrNzR3bXJcIixcInN1Ym5ldC04bWt4a2d4bFwiLFwic3VibmV0LWI0dGZ4cGIzXCJdLFwiUHJpdmF0ZUxpbmtJbmZvXCI6e1wiVmlwXCI6XCIxMC4yNTUuMC4xM1wiLFwiRW5kcG9pbnRJZFwiOlwidnBjZS1pc2RmbzQ4dlwifSxcIlNlY3VyaXR5R3JvdXBJZFwiOlwic2ctYzc2eWp3ZzBcIixcIlZpcnR1YWxTZWN1cml0eUdyb3VwSWRcIjpcIlwiLFwiRW5pU3VibmV0SWRzXCI6bnVsbCxcIkVudGVycHJpc2VHYXRld2F5Sm5zZ3dDb25maWdcIjpudWxsfSJ9 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey dlcSparkAppPyFiles \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey dataEngine \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 测试专用_AUTOTEST_勿删 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey roleArn \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue 1131 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey computeResourceType \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey dlcSparkCmdArgsV2 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue 100 \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey dlcSparkAppConf \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 73170 \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey cmdargsEni \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey dlcSparkTaskVersion \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue 2 \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey dlcSparkAppJars \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamKey dlcJobData \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamKey dlcSparkAppFiles \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamKey dlcSparkAppArchives \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamKey dlcSparkAppFile \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamValue cosn://0-1315051789/datastudio/resource/2917455276892352512/0zl/square_for_spark_job.py \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamKey IsInherit \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamValue {"taskMode":"1","fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamKey spark_cmd_args \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamValue 100 \
    --TaskConfiguration.DataCluster ff4fl7vc \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId ;73170; \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558005"
        },
        "RequestId": "ff9645aa-dd2b-4025-80fb-31206f0f2f78"
    }
}
```

**Example 27: 任务类型46：DLC Spark（标准引擎-Spark（jar））**

任务类型46：DLC Spark（标准引擎-Spark（jar））

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskBaseAttribute.TaskName api_DLCSPARK_46_jar_SparkSpark_250829_1756474886 \
    --TaskBaseAttribute.TaskTypeId 46 \
    --TaskBaseAttribute.WorkflowId 1adcdb07-77fe-4ee6-8d98-1cfcc2cdcfa9 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey job_type \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey dlc_region \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue ap-shanghai \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey dlcDataEngine \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue eyJBY2Nlc3NJbmZvcyI6W3siQWNjZXNzQ29ubmVjdGlvbkluZm9zIjpbXSwiQWNjZXNzVHlwZSI6IkhpdmVKREJDIn0seyJBY2Nlc3NDb25uZWN0aW9uSW5mb3MiOlsiamRiYzpkbGM6ZGxjLnRlbmNlbnRjbG91ZGFwaS5jb20/dGFza190eXBlPVNwYXJrU1FMVGFzayZkYXRhYmFzZV9uYW1lPXtEYXRhYmFzZU5hbWV9JmRhdGFzb3VyY2VfY29ubmVjdGlvbl9uYW1lPURhdGFMYWtlQ2F0YWxvZyZyZWdpb249YXAtc2hhbmdoYWkmZGF0YV9lbmdpbmVfbmFtZT3mlrDotK0mcmVzb3VyY2VfZ3JvdXBfbmFtZT17UmVzb3VyY2VHcm91cE5hbWV9Il0sIkFjY2Vzc1R5cGUiOiJETENKREJDIn1dLCJBdXRvQXV0aG9yaXphdGlvbiI6dHJ1ZSwiQXV0b1Jlc3VtZSI6ZmFsc2UsIkF1dG9TdXNwZW5kIjpmYWxzZSwiQXV0b1N1c3BlbmRUaW1lIjoxMCwiQ2hpbGRJbWFnZVZlcnNpb25JZCI6IjE2ZjQ2ZWQ0LTY2MGQtNDI2OS1iODNjLTBiMTMzYTZjYjcyMiIsIkNpZHJCbG9jayI6IjEwLjI1NS4wLjAvMTYiLCJDbHVzdGVyVHlwZSI6InNwYXJrX2N1IiwiQ3JlYXRlVGltZSI6MTc1MDI1MTkwMywiQ3JvbnRhYlJlc3VtZVN1c3BlbmQiOjAsIkNyb250YWJSZXN1bWVTdXNwZW5kU3RyYXRlZ3kiOnsiUmVzdW1lVGltZSI6IiIsIlN1c3BlbmRTdHJhdGVneSI6MCwiU3VzcGVuZFRpbWUiOiIifSwiRGF0YUVuZ2luZUlkIjoiRGF0YUVuZ2luZS1vam9yMmNuMyIsIkRhdGFFbmdpbmVOYW1lIjoi5paw6LStIiwiRGVmYXVsdERhdGFFbmdpbmUiOmZhbHNlLCJEZWZhdWx0SG91c2UiOmZhbHNlLCJFbGFzdGljTGltaXQiOjAsIkVsYXN0aWNTd2l0Y2giOmZhbHNlLCJFbmdpbmVFeGVjVHlwZSI6IkJBVENIIiwiRW5naW5lR2VuZXJhdGlvbiI6Ik5hdGl2ZSIsIkVuZ2luZU5ldHdvcmtJZCI6IkRhdGFFbmdpbmUtTmV0d29yay1jZWsydXIwOCIsIkVuZ2luZU5ldHdvcmtOYW1lIjoiZGVmYXVsdC1uZXR3b3JrLTAiLCJFbmdpbmVSZXNvdXJjZUdyb3VwQ291bnQiOjYsIkVuZ2luZVJlc291cmNlVXNlZENVIjowLCJFbmdpbmVUeXBlIjoic3BhcmsiLCJFbmdpbmVUeXBlRGV0YWlsIjoiU3RhbmRhcmRTcGFyayIsIkV4cGlyZVRpbWUiOiIwIiwiR2F0ZXdheUlkIjoiIiwiR2F0ZXdheVN0YXRlIjowLCJJZCI6MCwiSW1hZ2VWZXJzaW9uSWQiOiI4Nzg4NzA5OC01ODI3LTRiMGItYTg5Yy04MWNlNWNlOWNjYzEiLCJJbWFnZVZlcnNpb25OYW1lIjoiU3RhbmRhcmQtUyAxLjEiLCJJc0FJRW5naW5lIjoxLCJJc0FJR2F0ZXdheSI6ZmFsc2UsIklzUG9vbE1vZGUiOm51bGwsIklzU3VwcG9ydEFJIjp0cnVlLCJJc29sYXRlZFRpbWUiOiIwIiwiTWF4Q2x1c3RlcnMiOjEsIk1heENvbmN1cnJlbmN5Ijo1LCJNZXNzYWdlIjoiIiwiTWluQ2x1c3RlcnMiOjEsIk1vZGUiOjEsIk5ldHdvcmtDb25uZWN0aW9uU2V0IjpbeyJBcHBpZCI6MTMxNTA1MTc4OSwiQXNzb2NpYXRlSWQiOiIzM2E0MWIzMC05Zjc2LWU2YWItMTdkNi0zZDc5YjU2MGIzOGEiLCJDcmVhdGVUaW1lIjoxNzUwMzMwNTgxLCJEYXRhc291cmNlQ29ubmVjdGlvbkNpZHJCbG9jayI6IjEwLjAuMC4wLzE2IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25JZCI6IiIsIkRhdGFzb3VyY2VDb25uZWN0aW9uTmFtZSI6ImJpbmRfRGF0YUVuZ2luZS1vam9yMmNuM19lZ19kZWZhdWx0IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25TdWJuZXRDaWRyQmxvY2siOiIxMC4wLjAuMC8xNiIsIkRhdGFzb3VyY2VDb25uZWN0aW9uU3VibmV0SWQiOiJzdWJuZXQtZWNzNDJqNGgiLCJEYXRhc291cmNlQ29ubmVjdGlvblZwY0lkIjoidnBjLXMxcDM3YzVpIiwiRUdTdXBwb3J0IjoxLCJIb3VzZUlkIjoiRGF0YUVuZ2luZS1vam9yMmNuMyIsIkhvdXNlTmFtZSI6IuaWsOi0rSIsIklkIjozMTIsIk5ldHdvcmtDb25uZWN0aW9uRGVzYyI6ImRlZmF1bHQgYmluZCBlZyIsIk5ldHdvcmtDb25uZWN0aW9uVHlwZSI6NCwiU3RhdGUiOjEsIlN1YkFjY291bnRVaW4iOiIxMDAwNDExMzY3OTgiLCJVaW4iOiIxMDAwMjg0NDg5MDMiLCJVcGRhdGVUaW1lIjoxNzUwMzMwODU1fSx7IkFwcGlkIjoxMzE1MDUxNzg5LCJBc3NvY2lhdGVJZCI6IjZjNjFmYzZkLWE2NGItYWU5Mi1hNzNlLTZmN2I3YTQzNTRjMiIsIkNyZWF0ZVRpbWUiOjE3NTMxMTcyMzYsIkRhdGFzb3VyY2VDb25uZWN0aW9uQ2lkckJsb2NrIjoiMTAuMTAuMTYuMC8yMCIsIkRhdGFzb3VyY2VDb25uZWN0aW9uSWQiOiIiLCJEYXRhc291cmNlQ29ubmVjdGlvbk5hbWUiOiJuZXduZXQxMTExMTEiLCJEYXRhc291cmNlQ29ubmVjdGlvblN1Ym5ldENpZHJCbG9jayI6IjEwLjEwLjMxLjAvMjQiLCJEYXRhc291cmNlQ29ubmVjdGlvblN1Ym5ldElkIjoic3VibmV0LTJwNzMyN3l0IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25WcGNJZCI6InZwYy1rcHJxNDJ5byIsIkVHU3VwcG9ydCI6MCwiSG91c2VJZCI6IkRhdGFFbmdpbmUtb2pvcjJjbjMiLCJIb3VzZU5hbWUiOiLmlrDotK0iLCJJZCI6MzI2LCJOZXR3b3JrQ29ubmVjdGlvbkRlc2MiOiIiLCJOZXR3b3JrQ29ubmVjdGlvblR5cGUiOjQsIlN0YXRlIjoxLCJTdWJBY2NvdW50VWluIjoiMTAwMDI4NjUwNzk1IiwiVWluIjoiMTAwMDI4NDQ4OTAzIiwiVXBkYXRlVGltZSI6MTc1MzExNzI0MX1dLCJQZXJtaXNzaW9ucyI6WyJVU0UiLCJNT0RJRlkiLCJPUEVSQVRFIiwiTU9OSVRPUiIsIkRFTEVURSJdLCJRdW90YUlkIjoiIiwiUmVuZXdGbGFnIjowLCJSZXNvdXJjZVR5cGUiOiJTdGFuZGFyZF9DVSIsIlJldmVyc2FsVGltZSI6IjAiLCJTY2hlZHVsZUVsYXN0aWNpdHlDb25mIjp7IlNjaGVkdWxlVHlwZSI6IiIsIlNjaGVkdWxlZEVsYXN0aWNpdHlFbmFibGVkIjpmYWxzZSwiVGltZVpvbmUiOiIifSwiU2VydmljZVR5cGUiOiJETEMiLCJTZXNzaW9uUmVzb3VyY2VUZW1wbGF0ZSI6eyJEcml2ZXJTaXplIjoibGFyZ2UiLCJFeGVjdXRvck1heE51bWJlcnMiOjE1LCJFeGVjdXRvck51bXMiOjEsIkV4ZWN1dG9yU2l6ZSI6InhsYXJnZSJ9LCJTaXplIjoxMjgsIlNwZW5kQWZ0ZXIiOjAsIlN0YXJ0U3RhbmRieUNsdXN0ZXIiOmZhbHNlLCJTdGF0ZSI6MiwiU3ViQWNjb3VudFVpbiI6IjEwMDAyOTQxMTA1NiIsIlRhZ0xpc3QiOltdLCJUb2xlcmFibGVRdWV1ZVRpbWUiOjAsIlVpVVJMIjoiLTEiLCJVcGRhdGVUaW1lIjoxNzUwMjUxOTAzLCJVc2VyQWxpYXMiOiJBVVRPX1RFU1QiLCJVc2VyQXBwSWQiOjEzMTUwNTE3ODksIlVzZXJVaW4iOiIxMDAwMjg0NDg5MDMiLCJWcGNJbmZvIjoie1wiVnBjSWRcIjpcInZwYy1jODc4cDJybVwiLFwiVnBjQ2lkckJsb2NrXCI6XCIxMC4yNTUuMC4wLzE2XCIsXCJTdWJuZXRJZHNcIjpbXCJzdWJuZXQtZG5ja3Fnc3hcIixcInN1Ym5ldC03cWthdmQzMVwiLFwic3VibmV0LWw5NTF5bGJuXCIsXCJzdWJuZXQtcnk1MHB2dzNcIl0sXCJQcml2YXRlTGlua0luZm9cIjp7XCJWaXBcIjpcIjEwLjI1NS4wLjE1XCIsXCJFbmRwb2ludElkXCI6XCJ2cGNlLWtmczEyYWUxXCJ9LFwiU2VjdXJpdHlHcm91cElkXCI6XCJzZy1jNzZ5andnMFwiLFwiVmlydHVhbFNlY3VyaXR5R3JvdXBJZFwiOlwiXCIsXCJFbmlTdWJuZXRJZHNcIjpudWxsLFwiRW50ZXJwcmlzZUdhdGV3YXlKbnNnd0NvbmZpZ1wiOm51bGx9In0= \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey dlcSparkAppPyFiles \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey dataEngine \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 新购 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey roleArn \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue 1131 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey dlcSparkCmdArgsV2 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue 100 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey dlcSparkMainClass \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue org.apache.spark.examples.SparkPi \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey dlcSparkAppConf \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 73170 \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey calendar_id \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey cmdargsEni \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey dlcSparkTaskVersion \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue 2 \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamKey dlcSparkAppJars \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamKey dlcJobData \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamKey dlcSparkAppFiles \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamKey dlcSparkAppArchives \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamKey dlcSparkAppFile \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamValue cosn://0-1315051789/datastudio/resource/2917455276892352512/0zl/spark-examples_2.12-3.1.3.jar \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamKey IsInherit \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamValue {"taskMode":"1","fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.22.ParamKey spark_cmd_args \
    --TaskConfiguration.TaskExtConfigurationList.22.ParamValue 100 \
    --TaskConfiguration.DataCluster ff4fl7vc \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId ;73170; \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558008"
        },
        "RequestId": "a0aa71e0-5081-4642-861b-4757bbab02f2"
    }
}
```

**Example 28: 任务类型46：DLC Spark（标准引擎-Spark（py））**

任务类型46：DLC Spark（标准引擎-Spark（py））

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskBaseAttribute.TaskName api_DLCSPARK_46_py_SparkSpark_250829_1756474731 \
    --TaskBaseAttribute.TaskTypeId 46 \
    --TaskBaseAttribute.WorkflowId 1adcdb07-77fe-4ee6-8d98-1cfcc2cdcfa9 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey job_type \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey dlc_region \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue ap-shanghai \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey dlcDataEngine \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue eyJBY2Nlc3NJbmZvcyI6W3siQWNjZXNzQ29ubmVjdGlvbkluZm9zIjpbXSwiQWNjZXNzVHlwZSI6IkhpdmVKREJDIn0seyJBY2Nlc3NDb25uZWN0aW9uSW5mb3MiOlsiamRiYzpkbGM6ZGxjLnRlbmNlbnRjbG91ZGFwaS5jb20/dGFza190eXBlPVNwYXJrU1FMVGFzayZkYXRhYmFzZV9uYW1lPXtEYXRhYmFzZU5hbWV9JmRhdGFzb3VyY2VfY29ubmVjdGlvbl9uYW1lPURhdGFMYWtlQ2F0YWxvZyZyZWdpb249YXAtc2hhbmdoYWkmZGF0YV9lbmdpbmVfbmFtZT3mlrDotK0mcmVzb3VyY2VfZ3JvdXBfbmFtZT17UmVzb3VyY2VHcm91cE5hbWV9Il0sIkFjY2Vzc1R5cGUiOiJETENKREJDIn1dLCJBdXRvQXV0aG9yaXphdGlvbiI6dHJ1ZSwiQXV0b1Jlc3VtZSI6ZmFsc2UsIkF1dG9TdXNwZW5kIjpmYWxzZSwiQXV0b1N1c3BlbmRUaW1lIjoxMCwiQ2hpbGRJbWFnZVZlcnNpb25JZCI6IjE2ZjQ2ZWQ0LTY2MGQtNDI2OS1iODNjLTBiMTMzYTZjYjcyMiIsIkNpZHJCbG9jayI6IjEwLjI1NS4wLjAvMTYiLCJDbHVzdGVyVHlwZSI6InNwYXJrX2N1IiwiQ3JlYXRlVGltZSI6MTc1MDI1MTkwMywiQ3JvbnRhYlJlc3VtZVN1c3BlbmQiOjAsIkNyb250YWJSZXN1bWVTdXNwZW5kU3RyYXRlZ3kiOnsiUmVzdW1lVGltZSI6IiIsIlN1c3BlbmRTdHJhdGVneSI6MCwiU3VzcGVuZFRpbWUiOiIifSwiRGF0YUVuZ2luZUlkIjoiRGF0YUVuZ2luZS1vam9yMmNuMyIsIkRhdGFFbmdpbmVOYW1lIjoi5paw6LStIiwiRGVmYXVsdERhdGFFbmdpbmUiOmZhbHNlLCJEZWZhdWx0SG91c2UiOmZhbHNlLCJFbGFzdGljTGltaXQiOjAsIkVsYXN0aWNTd2l0Y2giOmZhbHNlLCJFbmdpbmVFeGVjVHlwZSI6IkJBVENIIiwiRW5naW5lR2VuZXJhdGlvbiI6Ik5hdGl2ZSIsIkVuZ2luZU5ldHdvcmtJZCI6IkRhdGFFbmdpbmUtTmV0d29yay1jZWsydXIwOCIsIkVuZ2luZU5ldHdvcmtOYW1lIjoiZGVmYXVsdC1uZXR3b3JrLTAiLCJFbmdpbmVSZXNvdXJjZUdyb3VwQ291bnQiOjYsIkVuZ2luZVJlc291cmNlVXNlZENVIjowLCJFbmdpbmVUeXBlIjoic3BhcmsiLCJFbmdpbmVUeXBlRGV0YWlsIjoiU3RhbmRhcmRTcGFyayIsIkV4cGlyZVRpbWUiOiIwIiwiR2F0ZXdheUlkIjoiIiwiR2F0ZXdheVN0YXRlIjowLCJJZCI6MCwiSW1hZ2VWZXJzaW9uSWQiOiI4Nzg4NzA5OC01ODI3LTRiMGItYTg5Yy04MWNlNWNlOWNjYzEiLCJJbWFnZVZlcnNpb25OYW1lIjoiU3RhbmRhcmQtUyAxLjEiLCJJc0FJRW5naW5lIjoxLCJJc0FJR2F0ZXdheSI6ZmFsc2UsIklzUG9vbE1vZGUiOm51bGwsIklzU3VwcG9ydEFJIjp0cnVlLCJJc29sYXRlZFRpbWUiOiIwIiwiTWF4Q2x1c3RlcnMiOjEsIk1heENvbmN1cnJlbmN5Ijo1LCJNZXNzYWdlIjoiIiwiTWluQ2x1c3RlcnMiOjEsIk1vZGUiOjEsIk5ldHdvcmtDb25uZWN0aW9uU2V0IjpbeyJBcHBpZCI6MTMxNTA1MTc4OSwiQXNzb2NpYXRlSWQiOiIzM2E0MWIzMC05Zjc2LWU2YWItMTdkNi0zZDc5YjU2MGIzOGEiLCJDcmVhdGVUaW1lIjoxNzUwMzMwNTgxLCJEYXRhc291cmNlQ29ubmVjdGlvbkNpZHJCbG9jayI6IjEwLjAuMC4wLzE2IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25JZCI6IiIsIkRhdGFzb3VyY2VDb25uZWN0aW9uTmFtZSI6ImJpbmRfRGF0YUVuZ2luZS1vam9yMmNuM19lZ19kZWZhdWx0IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25TdWJuZXRDaWRyQmxvY2siOiIxMC4wLjAuMC8xNiIsIkRhdGFzb3VyY2VDb25uZWN0aW9uU3VibmV0SWQiOiJzdWJuZXQtZWNzNDJqNGgiLCJEYXRhc291cmNlQ29ubmVjdGlvblZwY0lkIjoidnBjLXMxcDM3YzVpIiwiRUdTdXBwb3J0IjoxLCJIb3VzZUlkIjoiRGF0YUVuZ2luZS1vam9yMmNuMyIsIkhvdXNlTmFtZSI6IuaWsOi0rSIsIklkIjozMTIsIk5ldHdvcmtDb25uZWN0aW9uRGVzYyI6ImRlZmF1bHQgYmluZCBlZyIsIk5ldHdvcmtDb25uZWN0aW9uVHlwZSI6NCwiU3RhdGUiOjEsIlN1YkFjY291bnRVaW4iOiIxMDAwNDExMzY3OTgiLCJVaW4iOiIxMDAwMjg0NDg5MDMiLCJVcGRhdGVUaW1lIjoxNzUwMzMwODU1fSx7IkFwcGlkIjoxMzE1MDUxNzg5LCJBc3NvY2lhdGVJZCI6IjZjNjFmYzZkLWE2NGItYWU5Mi1hNzNlLTZmN2I3YTQzNTRjMiIsIkNyZWF0ZVRpbWUiOjE3NTMxMTcyMzYsIkRhdGFzb3VyY2VDb25uZWN0aW9uQ2lkckJsb2NrIjoiMTAuMTAuMTYuMC8yMCIsIkRhdGFzb3VyY2VDb25uZWN0aW9uSWQiOiIiLCJEYXRhc291cmNlQ29ubmVjdGlvbk5hbWUiOiJuZXduZXQxMTExMTEiLCJEYXRhc291cmNlQ29ubmVjdGlvblN1Ym5ldENpZHJCbG9jayI6IjEwLjEwLjMxLjAvMjQiLCJEYXRhc291cmNlQ29ubmVjdGlvblN1Ym5ldElkIjoic3VibmV0LTJwNzMyN3l0IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25WcGNJZCI6InZwYy1rcHJxNDJ5byIsIkVHU3VwcG9ydCI6MCwiSG91c2VJZCI6IkRhdGFFbmdpbmUtb2pvcjJjbjMiLCJIb3VzZU5hbWUiOiLmlrDotK0iLCJJZCI6MzI2LCJOZXR3b3JrQ29ubmVjdGlvbkRlc2MiOiIiLCJOZXR3b3JrQ29ubmVjdGlvblR5cGUiOjQsIlN0YXRlIjoxLCJTdWJBY2NvdW50VWluIjoiMTAwMDI4NjUwNzk1IiwiVWluIjoiMTAwMDI4NDQ4OTAzIiwiVXBkYXRlVGltZSI6MTc1MzExNzI0MX1dLCJQZXJtaXNzaW9ucyI6WyJVU0UiLCJNT0RJRlkiLCJPUEVSQVRFIiwiTU9OSVRPUiIsIkRFTEVURSJdLCJRdW90YUlkIjoiIiwiUmVuZXdGbGFnIjowLCJSZXNvdXJjZVR5cGUiOiJTdGFuZGFyZF9DVSIsIlJldmVyc2FsVGltZSI6IjAiLCJTY2hlZHVsZUVsYXN0aWNpdHlDb25mIjp7IlNjaGVkdWxlVHlwZSI6IiIsIlNjaGVkdWxlZEVsYXN0aWNpdHlFbmFibGVkIjpmYWxzZSwiVGltZVpvbmUiOiIifSwiU2VydmljZVR5cGUiOiJETEMiLCJTZXNzaW9uUmVzb3VyY2VUZW1wbGF0ZSI6eyJEcml2ZXJTaXplIjoibGFyZ2UiLCJFeGVjdXRvck1heE51bWJlcnMiOjE1LCJFeGVjdXRvck51bXMiOjEsIkV4ZWN1dG9yU2l6ZSI6InhsYXJnZSJ9LCJTaXplIjoxMjgsIlNwZW5kQWZ0ZXIiOjAsIlN0YXJ0U3RhbmRieUNsdXN0ZXIiOmZhbHNlLCJTdGF0ZSI6MiwiU3ViQWNjb3VudFVpbiI6IjEwMDAyOTQxMTA1NiIsIlRhZ0xpc3QiOltdLCJUb2xlcmFibGVRdWV1ZVRpbWUiOjAsIlVpVVJMIjoiLTEiLCJVcGRhdGVUaW1lIjoxNzUwMjUxOTAzLCJVc2VyQWxpYXMiOiJBVVRPX1RFU1QiLCJVc2VyQXBwSWQiOjEzMTUwNTE3ODksIlVzZXJVaW4iOiIxMDAwMjg0NDg5MDMiLCJWcGNJbmZvIjoie1wiVnBjSWRcIjpcInZwYy1jODc4cDJybVwiLFwiVnBjQ2lkckJsb2NrXCI6XCIxMC4yNTUuMC4wLzE2XCIsXCJTdWJuZXRJZHNcIjpbXCJzdWJuZXQtZG5ja3Fnc3hcIixcInN1Ym5ldC03cWthdmQzMVwiLFwic3VibmV0LWw5NTF5bGJuXCIsXCJzdWJuZXQtcnk1MHB2dzNcIl0sXCJQcml2YXRlTGlua0luZm9cIjp7XCJWaXBcIjpcIjEwLjI1NS4wLjE1XCIsXCJFbmRwb2ludElkXCI6XCJ2cGNlLWtmczEyYWUxXCJ9LFwiU2VjdXJpdHlHcm91cElkXCI6XCJzZy1jNzZ5andnMFwiLFwiVmlydHVhbFNlY3VyaXR5R3JvdXBJZFwiOlwiXCIsXCJFbmlTdWJuZXRJZHNcIjpudWxsLFwiRW50ZXJwcmlzZUdhdGV3YXlKbnNnd0NvbmZpZ1wiOm51bGx9In0= \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey dlcSparkAppPyFiles \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey dataEngine \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 新购 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey roleArn \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue 1131 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey computeResourceType \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey dlcSparkCmdArgsV2 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue 100 \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey dlcSparkAppConf \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 73170 \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey cmdargsEni \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey dlcSparkTaskVersion \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue 2 \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey dlcSparkAppJars \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamKey dlcJobData \
    --TaskConfiguration.TaskExtConfigurationList.14.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamKey dlcSparkAppFiles \
    --TaskConfiguration.TaskExtConfigurationList.15.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamKey dlcSparkAppArchives \
    --TaskConfiguration.TaskExtConfigurationList.16.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamKey dlcSparkAppFile \
    --TaskConfiguration.TaskExtConfigurationList.17.ParamValue cosn://0-1315051789/datastudio/resource/2917455276892352512/0zl/square_for_spark_job.py \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.18.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamKey IsInherit \
    --TaskConfiguration.TaskExtConfigurationList.19.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.20.ParamValue {"taskMode":"1","fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamKey spark_cmd_args \
    --TaskConfiguration.TaskExtConfigurationList.21.ParamValue 100 \
    --TaskConfiguration.DataCluster ff4fl7vc \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.SourceServiceId ;73170; \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558005"
        },
        "RequestId": "ff9645aa-dd2b-4025-80fb-31206f0f2f78"
    }
}
```

**Example 29: 任务类型47：TiOne**

任务类型47：TiOne

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2417334454903762944 \
    --TaskBaseAttribute.TaskName test_251206_160458 \
    --TaskBaseAttribute.TaskTypeId 47 \
    --TaskBaseAttribute.WorkflowId fb2a9bce-7704-4812-a268-ba593201e97c \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription 251206_160449 \
    --TaskConfiguration.CodeContent ZGF0ZQ== \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 16911 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey notebook_instanceId \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue nb-1222502273829092224 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey python_type \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue emr-m7o0zu6k \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey calendar_open \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey waitExecutionTotalTTL \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue -1 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey notebook_instanceName \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue test_alexnet \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue wedata-agent-gz-1257305158 \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey notebook_instanceState \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue 运行中 \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey specLabelConfItems \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ== \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey python_sub_version \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue emr-m7o0zu6k \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue {"fromMapping":false} \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20231124174433263533 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558006"
        },
        "RequestId": "c40e882d-5b8a-42f8-84ff-29c66e983137"
    }
}
```

**Example 30: 任务类型48：Trino**

任务类型48：Trino

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName test_trino_openapi111111 \
    --TaskBaseAttribute.TaskTypeId 48 \
    --TaskBaseAttribute.WorkflowId c3152ead-bd27-4c07-afbc-2ae7b54347a4 \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription test_ssh_openapi1 \
    --TaskConfiguration.CodeContent c2VsZWN0IDE7 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey calendar_open \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue 0 \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey source_service \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue 69051 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey specLabelConfItems \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ== \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey waitExecutionTotalTTL \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue -1 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey source_server \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue default \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558008"
        },
        "RequestId": "a0aa71e0-5081-4642-861b-4757bbab02f2"
    }
}
```

**Example 31: 任务类型50：DLC PySpark（SuperSQL引擎-Spark作业）**

任务类型50：DLC PySpark（SuperSQL引擎-Spark作业）；注意：支持 SuperSQL引擎-Spark作业、标准引擎-Spark 两种引擎，需要2类用例

 
字段说明：

引擎字段 dlcDataEngine 需要通过 https://cloud.tencent.com/document/product/1342/86308 ；

数据访问策略对应的角色编号 roleArn 需要通过 https://cloud.tencent.com/document/product/1342/96019

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskBaseAttribute.TaskName api_DLCPYSPARK_50_SparkBatch_250829_1756475240 \
    --TaskBaseAttribute.TaskTypeId 50 \
    --TaskBaseAttribute.WorkflowId 1adcdb07-77fe-4ee6-8d98-1cfcc2cdcfa9 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskConfiguration.CodeContent IyBQeXNwYXJrCgpmcm9tIHB5c3Bhcmsuc3FsIGltcG9ydCBTcGFya1Nlc3Npb24KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIGRhdGUKZnJvbSBweXNwYXJrLnNxbCBpbXBvcnQgUm93CiAKc3BhcmsgPSBTcGFya1Nlc3Npb24uYnVpbGRlci5hcHBOYW1lKCdOT1RJQ0U6ZGVuZ2JveHVfaGFuZHNvbWUhISEnKS5nZXRPckNyZWF0ZSgpCiAKZGYgPSBzcGFyay5jcmVhdGVEYXRhRnJhbWUoWwogICAgUm93KGE9MSwgYj0yLiwgYz0nc3RyaW5nMScsIGQ9ZGF0ZSgyMDAwLCAxLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAxLCAxMiwgMCkpLAogICAgUm93KGE9MiwgYj0zLiwgYz0nc3RyaW5nMicsIGQ9ZGF0ZSgyMDAwLCAyLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAyLCAxMiwgMCkpLAogICAgUm93KGE9NCwgYj01LiwgYz0nc3RyaW5nMycsIGQ9ZGF0ZSgyMDAwLCAzLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAzLCAxMiwgMCkpCl0pCiAKcHJpbnQoJy0tLS0tcHlzcGFyayB0ZXN0IHN0YXJ0JykKIApkZi5maWx0ZXIoZGYuYSA9PSAxKS5zaG93KCkKZGYuY3JlYXRlT3JSZXBsYWNlVGVtcFZpZXcoJ3RhYmxlQScpCnNwYXJrLnNxbCgnU0VMRUNUIGNvdW50KCopIGZyb20gdGFibGVBJykuc2hvdygpCiAKcHJpbnQoJy0tLS0tcHlzcGFyayB0ZXN0IGVuZCcpCgo= \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey dlc_region \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue ap-shanghai \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey dlcDataEngine \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue eyJBY2Nlc3NJbmZvcyI6W3siQWNjZXNzQ29ubmVjdGlvbkluZm9zIjpbImpkYmM6ZGxjOmRsYy50ZW5jZW50Y2xvdWRhcGkuY29tP3Rhc2tfdHlwZT1CYXRjaFNRTFRhc2smZGF0YWJhc2VfbmFtZT17RGF0YWJhc2VOYW1lfSZkYXRhc291cmNlX2Nvbm5lY3Rpb25fbmFtZT1EYXRhTGFrZUNhdGFsb2cmcmVnaW9uPWFwLXNoYW5naGFpJmRhdGFfZW5naW5lX25hbWU95rWL6K+V5LiT55SoX0FVVE9URVNUX+WLv+WIoCZyZXN1bHRfdHlwZT17UmVzdWx0VHlwZX0mcmVhZF90eXBlPXtSZWFkVHlwZX0iXSwiQWNjZXNzVHlwZSI6IkRMQ0pEQkMifV0sIkF1dG9BdXRob3JpemF0aW9uIjp0cnVlLCJBdXRvUmVzdW1lIjpmYWxzZSwiQXV0b1N1c3BlbmQiOmZhbHNlLCJBdXRvU3VzcGVuZFRpbWUiOjEwLCJDaGlsZEltYWdlVmVyc2lvbklkIjoiMmFkOTc5MjgtM2M1MC00ZGE2LWJlMjItNzk5N2NkYmZlZmQ3IiwiQ2lkckJsb2NrIjoiMTAuMjU1LjAuMC8xNiIsIkNsdXN0ZXJUeXBlIjoic3BhcmtfY3UiLCJDcmVhdGVUaW1lIjoxNzUwMzMwMDAwLCJDcm9udGFiUmVzdW1lU3VzcGVuZCI6MCwiQ3JvbnRhYlJlc3VtZVN1c3BlbmRTdHJhdGVneSI6eyJSZXN1bWVUaW1lIjoiIiwiU3VzcGVuZFN0cmF0ZWd5IjowLCJTdXNwZW5kVGltZSI6IiJ9LCJEYXRhRW5naW5lSWQiOiJEYXRhRW5naW5lLTBmcWlhOTdqIiwiRGF0YUVuZ2luZU5hbWUiOiLmtYvor5XkuJPnlKhfQVVUT1RFU1Rf5Yu/5YigIiwiRGVmYXVsdERhdGFFbmdpbmUiOmZhbHNlLCJEZWZhdWx0SG91c2UiOmZhbHNlLCJFbGFzdGljTGltaXQiOjAsIkVsYXN0aWNTd2l0Y2giOmZhbHNlLCJFbmdpbmVFeGVjVHlwZSI6IkJBVENIIiwiRW5naW5lR2VuZXJhdGlvbiI6IlN1cGVyU1FMIiwiRW5naW5lTmV0d29ya0lkIjoiIiwiRW5naW5lTmV0d29ya05hbWUiOiIiLCJFbmdpbmVSZXNvdXJjZUdyb3VwQ291bnQiOjAsIkVuZ2luZVJlc291cmNlVXNlZENVIjowLCJFbmdpbmVUeXBlIjoic3BhcmsiLCJFbmdpbmVUeXBlRGV0YWlsIjoiU3BhcmtCYXRjaCIsIkV4cGlyZVRpbWUiOiIwIiwiR2F0ZXdheUlkIjoiIiwiR2F0ZXdheVN0YXRlIjowLCJJZCI6MCwiSW1hZ2VWZXJzaW9uSWQiOiJiZmFkNGViYS01NGMzLTQzZTktOGI0MC0yNGVjZDQ4OGNkNzciLCJJbWFnZVZlcnNpb25OYW1lIjoiU3BhcmsgMy4yIiwiSXNBSUVuZ2luZSI6MCwiSXNBSUdhdGV3YXkiOmZhbHNlLCJJc1Bvb2xNb2RlIjpudWxsLCJJc1N1cHBvcnRBSSI6ZmFsc2UsIklzb2xhdGVkVGltZSI6IjAiLCJNYXhDbHVzdGVycyI6MSwiTWF4Q29uY3VycmVuY3kiOjUsIk1lc3NhZ2UiOiIiLCJNaW5DbHVzdGVycyI6MSwiTW9kZSI6MSwiTmV0d29ya0Nvbm5lY3Rpb25TZXQiOltdLCJQZXJtaXNzaW9ucyI6WyJVU0UiLCJNT0RJRlkiLCJPUEVSQVRFIiwiTU9OSVRPUiIsIkRFTEVURSJdLCJRdW90YUlkIjoiIiwiUmVuZXdGbGFnIjowLCJSZXNvdXJjZVR5cGUiOiJTdGFuZGFyZF9DVSIsIlJldmVyc2FsVGltZSI6IjAiLCJTY2hlZHVsZUVsYXN0aWNpdHlDb25mIjp7IlNjaGVkdWxlVHlwZSI6IiIsIlNjaGVkdWxlZEVsYXN0aWNpdHlFbmFibGVkIjpmYWxzZSwiVGltZVpvbmUiOiIifSwiU2VydmljZVR5cGUiOiJETEMiLCJTZXNzaW9uUmVzb3VyY2VUZW1wbGF0ZSI6eyJEcml2ZXJTaXplIjoic21hbGwiLCJFeGVjdXRvck1heE51bWJlcnMiOjEsIkV4ZWN1dG9yTnVtcyI6MSwiRXhlY3V0b3JTaXplIjoic21hbGwifSwiU2l6ZSI6MTI4LCJTcGVuZEFmdGVyIjowLCJTdGFydFN0YW5kYnlDbHVzdGVyIjpmYWxzZSwiU3RhdGUiOjIsIlN1YkFjY291bnRVaW4iOiIxMDAwMjk0MTEwNTYiLCJUYWdMaXN0IjpbXSwiVG9sZXJhYmxlUXVldWVUaW1lIjowLCJVaVVSTCI6Ii0xIiwiVXBkYXRlVGltZSI6MTc1MTYzMDgxNCwiVXNlckFsaWFzIjoiQVVUT19URVNUIiwiVXNlckFwcElkIjoxMzE1MDUxNzg5LCJVc2VyVWluIjoiMTAwMDI4NDQ4OTAzIiwiVnBjSW5mbyI6IntcIlZwY0lkXCI6XCJ2cGMtMzYzczR2M2FcIixcIlZwY0NpZHJCbG9ja1wiOlwiMTAuMjU1LjAuMC8xNlwiLFwiU3VibmV0SWRzXCI6W1wic3VibmV0LW5nYXFxeGY5XCIsXCJzdWJuZXQtYzlrNzR3bXJcIixcInN1Ym5ldC04bWt4a2d4bFwiLFwic3VibmV0LWI0dGZ4cGIzXCJdLFwiUHJpdmF0ZUxpbmtJbmZvXCI6e1wiVmlwXCI6XCIxMC4yNTUuMC4xM1wiLFwiRW5kcG9pbnRJZFwiOlwidnBjZS1pc2RmbzQ4dlwifSxcIlNlY3VyaXR5R3JvdXBJZFwiOlwic2ctYzc2eWp3ZzBcIixcIlZpcnR1YWxTZWN1cml0eUdyb3VwSWRcIjpcIlwiLFwiRW5pU3VibmV0SWRzXCI6bnVsbCxcIkVudGVycHJpc2VHYXRld2F5Sm5zZ3dDb25maWdcIjpudWxsfSJ9 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey python_type \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey dataEngine \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 测试专用_AUTOTEST_勿删 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey roleArn \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 1131 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey cmdargsMainArgs \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey cmdargsSparkConfig \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey computeResourceType \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey cmdargsEni \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey python_sub_version \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue python3.12 \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey IsInherit \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster ff4fl7vc \
    --TaskConfiguration.BrokerIp any \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174559002"
        },
        "RequestId": "d15c7f44-e8a2-4560-b61f-35f35ebfb4ab"
    }
}
```

**Example 32: 任务类型50：DLC PySpark（标准引擎-Spark ）**

任务类型50：DLC PySpark（标准引擎-Spark ）

注意：支持 SuperSQL引擎-Spark作业、标准引擎-Spark 两种引擎，需要2类用例

 

字段说明：

引擎字段 dlcDataEngine 需要通过 https://cloud.tencent.com/document/product/1342/86308  ；

数据访问策略对应的角色编号 roleArn 需要通过 https://cloud.tencent.com/document/product/1342/96019

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskBaseAttribute.TaskName api_DLCPYSPARK_50_SparkSpark_250829_1756475387 \
    --TaskBaseAttribute.TaskTypeId 50 \
    --TaskBaseAttribute.WorkflowId 1adcdb07-77fe-4ee6-8d98-1cfcc2cdcfa9 \
    --TaskBaseAttribute.OwnerUin 100041136798 \
    --TaskBaseAttribute.TaskDescription  \
    --TaskConfiguration.ResourceGroup 20250524170043856955 \
    --TaskConfiguration.CodeContent IyBQeXNwYXJrCgpmcm9tIHB5c3Bhcmsuc3FsIGltcG9ydCBTcGFya1Nlc3Npb24KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIGRhdGUKZnJvbSBweXNwYXJrLnNxbCBpbXBvcnQgUm93CiAKc3BhcmsgPSBTcGFya1Nlc3Npb24uYnVpbGRlci5hcHBOYW1lKCdOT1RJQ0U6ZGVuZ2JveHVfaGFuZHNvbWUhISEnKS5nZXRPckNyZWF0ZSgpCiAKZGYgPSBzcGFyay5jcmVhdGVEYXRhRnJhbWUoWwogICAgUm93KGE9MSwgYj0yLiwgYz0nc3RyaW5nMScsIGQ9ZGF0ZSgyMDAwLCAxLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAxLCAxMiwgMCkpLAogICAgUm93KGE9MiwgYj0zLiwgYz0nc3RyaW5nMicsIGQ9ZGF0ZSgyMDAwLCAyLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAyLCAxMiwgMCkpLAogICAgUm93KGE9NCwgYj01LiwgYz0nc3RyaW5nMycsIGQ9ZGF0ZSgyMDAwLCAzLCAxKSwgZT1kYXRldGltZSgyMDAwLCAxLCAzLCAxMiwgMCkpCl0pCiAKcHJpbnQoJy0tLS0tcHlzcGFyayB0ZXN0IHN0YXJ0JykKIApkZi5maWx0ZXIoZGYuYSA9PSAxKS5zaG93KCkKZGYuY3JlYXRlT3JSZXBsYWNlVGVtcFZpZXcoJ3RhYmxlQScpCnNwYXJrLnNxbCgnU0VMRUNUIGNvdW50KCopIGZyb20gdGFibGVBJykuc2hvdygpCiAKcHJpbnQoJy0tLS0tcHlzcGFyayB0ZXN0IGVuZCcpCgo= \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey dlc_region \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue ap-shanghai \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey dlcDataEngine \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue eyJBY2Nlc3NJbmZvcyI6W3siQWNjZXNzQ29ubmVjdGlvbkluZm9zIjpbXSwiQWNjZXNzVHlwZSI6IkhpdmVKREJDIn0seyJBY2Nlc3NDb25uZWN0aW9uSW5mb3MiOlsiamRiYzpkbGM6ZGxjLnRlbmNlbnRjbG91ZGFwaS5jb20/dGFza190eXBlPVNwYXJrU1FMVGFzayZkYXRhYmFzZV9uYW1lPXtEYXRhYmFzZU5hbWV9JmRhdGFzb3VyY2VfY29ubmVjdGlvbl9uYW1lPURhdGFMYWtlQ2F0YWxvZyZyZWdpb249YXAtc2hhbmdoYWkmZGF0YV9lbmdpbmVfbmFtZT3mlrDotK0mcmVzb3VyY2VfZ3JvdXBfbmFtZT17UmVzb3VyY2VHcm91cE5hbWV9Il0sIkFjY2Vzc1R5cGUiOiJETENKREJDIn1dLCJBdXRvQXV0aG9yaXphdGlvbiI6dHJ1ZSwiQXV0b1Jlc3VtZSI6ZmFsc2UsIkF1dG9TdXNwZW5kIjpmYWxzZSwiQXV0b1N1c3BlbmRUaW1lIjoxMCwiQ2hpbGRJbWFnZVZlcnNpb25JZCI6IjE2ZjQ2ZWQ0LTY2MGQtNDI2OS1iODNjLTBiMTMzYTZjYjcyMiIsIkNpZHJCbG9jayI6IjEwLjI1NS4wLjAvMTYiLCJDbHVzdGVyVHlwZSI6InNwYXJrX2N1IiwiQ3JlYXRlVGltZSI6MTc1MDI1MTkwMywiQ3JvbnRhYlJlc3VtZVN1c3BlbmQiOjAsIkNyb250YWJSZXN1bWVTdXNwZW5kU3RyYXRlZ3kiOnsiUmVzdW1lVGltZSI6IiIsIlN1c3BlbmRTdHJhdGVneSI6MCwiU3VzcGVuZFRpbWUiOiIifSwiRGF0YUVuZ2luZUlkIjoiRGF0YUVuZ2luZS1vam9yMmNuMyIsIkRhdGFFbmdpbmVOYW1lIjoi5paw6LStIiwiRGVmYXVsdERhdGFFbmdpbmUiOmZhbHNlLCJEZWZhdWx0SG91c2UiOmZhbHNlLCJFbGFzdGljTGltaXQiOjAsIkVsYXN0aWNTd2l0Y2giOmZhbHNlLCJFbmdpbmVFeGVjVHlwZSI6IkJBVENIIiwiRW5naW5lR2VuZXJhdGlvbiI6Ik5hdGl2ZSIsIkVuZ2luZU5ldHdvcmtJZCI6IkRhdGFFbmdpbmUtTmV0d29yay1jZWsydXIwOCIsIkVuZ2luZU5ldHdvcmtOYW1lIjoiZGVmYXVsdC1uZXR3b3JrLTAiLCJFbmdpbmVSZXNvdXJjZUdyb3VwQ291bnQiOjYsIkVuZ2luZVJlc291cmNlVXNlZENVIjowLCJFbmdpbmVUeXBlIjoic3BhcmsiLCJFbmdpbmVUeXBlRGV0YWlsIjoiU3RhbmRhcmRTcGFyayIsIkV4cGlyZVRpbWUiOiIwIiwiR2F0ZXdheUlkIjoiIiwiR2F0ZXdheVN0YXRlIjowLCJJZCI6MCwiSW1hZ2VWZXJzaW9uSWQiOiI4Nzg4NzA5OC01ODI3LTRiMGItYTg5Yy04MWNlNWNlOWNjYzEiLCJJbWFnZVZlcnNpb25OYW1lIjoiU3RhbmRhcmQtUyAxLjEiLCJJc0FJRW5naW5lIjoxLCJJc0FJR2F0ZXdheSI6ZmFsc2UsIklzUG9vbE1vZGUiOm51bGwsIklzU3VwcG9ydEFJIjp0cnVlLCJJc29sYXRlZFRpbWUiOiIwIiwiTWF4Q2x1c3RlcnMiOjEsIk1heENvbmN1cnJlbmN5Ijo1LCJNZXNzYWdlIjoiIiwiTWluQ2x1c3RlcnMiOjEsIk1vZGUiOjEsIk5ldHdvcmtDb25uZWN0aW9uU2V0IjpbeyJBcHBpZCI6MTMxNTA1MTc4OSwiQXNzb2NpYXRlSWQiOiIzM2E0MWIzMC05Zjc2LWU2YWItMTdkNi0zZDc5YjU2MGIzOGEiLCJDcmVhdGVUaW1lIjoxNzUwMzMwNTgxLCJEYXRhc291cmNlQ29ubmVjdGlvbkNpZHJCbG9jayI6IjEwLjAuMC4wLzE2IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25JZCI6IiIsIkRhdGFzb3VyY2VDb25uZWN0aW9uTmFtZSI6ImJpbmRfRGF0YUVuZ2luZS1vam9yMmNuM19lZ19kZWZhdWx0IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25TdWJuZXRDaWRyQmxvY2siOiIxMC4wLjAuMC8xNiIsIkRhdGFzb3VyY2VDb25uZWN0aW9uU3VibmV0SWQiOiJzdWJuZXQtZWNzNDJqNGgiLCJEYXRhc291cmNlQ29ubmVjdGlvblZwY0lkIjoidnBjLXMxcDM3YzVpIiwiRUdTdXBwb3J0IjoxLCJIb3VzZUlkIjoiRGF0YUVuZ2luZS1vam9yMmNuMyIsIkhvdXNlTmFtZSI6IuaWsOi0rSIsIklkIjozMTIsIk5ldHdvcmtDb25uZWN0aW9uRGVzYyI6ImRlZmF1bHQgYmluZCBlZyIsIk5ldHdvcmtDb25uZWN0aW9uVHlwZSI6NCwiU3RhdGUiOjEsIlN1YkFjY291bnRVaW4iOiIxMDAwNDExMzY3OTgiLCJVaW4iOiIxMDAwMjg0NDg5MDMiLCJVcGRhdGVUaW1lIjoxNzUwMzMwODU1fSx7IkFwcGlkIjoxMzE1MDUxNzg5LCJBc3NvY2lhdGVJZCI6IjZjNjFmYzZkLWE2NGItYWU5Mi1hNzNlLTZmN2I3YTQzNTRjMiIsIkNyZWF0ZVRpbWUiOjE3NTMxMTcyMzYsIkRhdGFzb3VyY2VDb25uZWN0aW9uQ2lkckJsb2NrIjoiMTAuMTAuMTYuMC8yMCIsIkRhdGFzb3VyY2VDb25uZWN0aW9uSWQiOiIiLCJEYXRhc291cmNlQ29ubmVjdGlvbk5hbWUiOiJuZXduZXQxMTExMTEiLCJEYXRhc291cmNlQ29ubmVjdGlvblN1Ym5ldENpZHJCbG9jayI6IjEwLjEwLjMxLjAvMjQiLCJEYXRhc291cmNlQ29ubmVjdGlvblN1Ym5ldElkIjoic3VibmV0LTJwNzMyN3l0IiwiRGF0YXNvdXJjZUNvbm5lY3Rpb25WcGNJZCI6InZwYy1rcHJxNDJ5byIsIkVHU3VwcG9ydCI6MCwiSG91c2VJZCI6IkRhdGFFbmdpbmUtb2pvcjJjbjMiLCJIb3VzZU5hbWUiOiLmlrDotK0iLCJJZCI6MzI2LCJOZXR3b3JrQ29ubmVjdGlvbkRlc2MiOiIiLCJOZXR3b3JrQ29ubmVjdGlvblR5cGUiOjQsIlN0YXRlIjoxLCJTdWJBY2NvdW50VWluIjoiMTAwMDI4NjUwNzk1IiwiVWluIjoiMTAwMDI4NDQ4OTAzIiwiVXBkYXRlVGltZSI6MTc1MzExNzI0MX1dLCJQZXJtaXNzaW9ucyI6WyJVU0UiLCJNT0RJRlkiLCJPUEVSQVRFIiwiTU9OSVRPUiIsIkRFTEVURSJdLCJRdW90YUlkIjoiIiwiUmVuZXdGbGFnIjowLCJSZXNvdXJjZVR5cGUiOiJTdGFuZGFyZF9DVSIsIlJldmVyc2FsVGltZSI6IjAiLCJTY2hlZHVsZUVsYXN0aWNpdHlDb25mIjp7IlNjaGVkdWxlVHlwZSI6IiIsIlNjaGVkdWxlZEVsYXN0aWNpdHlFbmFibGVkIjpmYWxzZSwiVGltZVpvbmUiOiIifSwiU2VydmljZVR5cGUiOiJETEMiLCJTZXNzaW9uUmVzb3VyY2VUZW1wbGF0ZSI6eyJEcml2ZXJTaXplIjoibGFyZ2UiLCJFeGVjdXRvck1heE51bWJlcnMiOjE1LCJFeGVjdXRvck51bXMiOjEsIkV4ZWN1dG9yU2l6ZSI6InhsYXJnZSJ9LCJTaXplIjoxMjgsIlNwZW5kQWZ0ZXIiOjAsIlN0YXJ0U3RhbmRieUNsdXN0ZXIiOmZhbHNlLCJTdGF0ZSI6MiwiU3ViQWNjb3VudFVpbiI6IjEwMDAyOTQxMTA1NiIsIlRhZ0xpc3QiOltdLCJUb2xlcmFibGVRdWV1ZVRpbWUiOjAsIlVpVVJMIjoiLTEiLCJVcGRhdGVUaW1lIjoxNzUwMjUxOTAzLCJVc2VyQWxpYXMiOiJBVVRPX1RFU1QiLCJVc2VyQXBwSWQiOjEzMTUwNTE3ODksIlVzZXJVaW4iOiIxMDAwMjg0NDg5MDMiLCJWcGNJbmZvIjoie1wiVnBjSWRcIjpcInZwYy1jODc4cDJybVwiLFwiVnBjQ2lkckJsb2NrXCI6XCIxMC4yNTUuMC4wLzE2XCIsXCJTdWJuZXRJZHNcIjpbXCJzdWJuZXQtZG5ja3Fnc3hcIixcInN1Ym5ldC03cWthdmQzMVwiLFwic3VibmV0LWw5NTF5bGJuXCIsXCJzdWJuZXQtcnk1MHB2dzNcIl0sXCJQcml2YXRlTGlua0luZm9cIjp7XCJWaXBcIjpcIjEwLjI1NS4wLjE1XCIsXCJFbmRwb2ludElkXCI6XCJ2cGNlLWtmczEyYWUxXCJ9LFwiU2VjdXJpdHlHcm91cElkXCI6XCJzZy1jNzZ5andnMFwiLFwiVmlydHVhbFNlY3VyaXR5R3JvdXBJZFwiOlwiXCIsXCJFbmlTdWJuZXRJZHNcIjpudWxsLFwiRW50ZXJwcmlzZUdhdGV3YXlKbnNnd0NvbmZpZ1wiOm51bGx9In0= \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey python_type \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue python3 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey dataEngine \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue 新购 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey roleArn \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue 1131 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey cmdargsMainArgs \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey cmdargsSparkConfig \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey computeResourceType \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey cmdargsEni \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue  \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamKey python_sub_version \
    --TaskConfiguration.TaskExtConfigurationList.10.ParamValue python3.12 \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.11.ParamValue ff4fl7vc \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamKey IsInherit \
    --TaskConfiguration.TaskExtConfigurationList.12.ParamValue 1 \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.13.ParamValue {"fromMapping":false} \
    --TaskConfiguration.DataCluster ff4fl7vc \
    --TaskConfiguration.BrokerIp any \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-29 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.CalendarId  \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.CrontabExpression 0 0 0 * * ? * \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174559006"
        },
        "RequestId": "65fbdbbb-6a9b-4002-95ba-15347e9ed6f5"
    }
}
```

**Example 33: 任务类型92：MapReduce**

任务类型92：MapReduce

Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --TaskBaseAttribute.TaskName test_mapreduce_openapi111111 \
    --TaskBaseAttribute.TaskTypeId 92 \
    --TaskBaseAttribute.WorkflowId c3152ead-bd27-4c07-afbc-2ae7b54347a4 \
    --TaskBaseAttribute.OwnerUin 100028448903 \
    --TaskBaseAttribute.TaskDescription test_ssh_openapi1 \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamKey extraInfo \
    --TaskConfiguration.TaskExtConfigurationList.0.ParamValue {"fromMapping":false} \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamKey waitExecutionTotalTTL \
    --TaskConfiguration.TaskExtConfigurationList.1.ParamValue -1 \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamKey source_cluster \
    --TaskConfiguration.TaskExtConfigurationList.2.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamKey data_cluster \
    --TaskConfiguration.TaskExtConfigurationList.3.ParamValue emr-34r7poh0 \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamKey bucket \
    --TaskConfiguration.TaskExtConfigurationList.4.ParamValue anny-gz-1315051789 \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamKey ftp.file.name \
    --TaskConfiguration.TaskExtConfigurationList.5.ParamValue /datastudio/resource/2428908825624145920/hadoop-mapreduce-examples.zip \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamKey region \
    --TaskConfiguration.TaskExtConfigurationList.6.ParamValue ap-guangzhou \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamKey task.main.param \
    --TaskConfiguration.TaskExtConfigurationList.7.ParamValue hadoop-mapreduce-examples-2.7.3.2.6.3.0-235.jar pi 10 10 \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamKey task.main.timeout \
    --TaskConfiguration.TaskExtConfigurationList.8.ParamValue 300 \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamKey task.check.timeout \
    --TaskConfiguration.TaskExtConfigurationList.9.ParamValue 5 \
    --TaskConfiguration.BrokerIp any \
    --TaskConfiguration.ResourceGroup 20231124174317834475 \
    --TaskSchedulerConfiguration.CycleType DAY_CYCLE \
    --TaskSchedulerConfiguration.ScheduleTimeZone UTC+8 \
    --TaskSchedulerConfiguration.StartTime 2025-08-26 00:00:00 \
    --TaskSchedulerConfiguration.EndTime 2099-12-31 23:59:59 \
    --TaskSchedulerConfiguration.ExecutionStartTime 00:00 \
    --TaskSchedulerConfiguration.ExecutionEndTime 23:59 \
    --TaskSchedulerConfiguration.ScheduleType 0 \
    --TaskSchedulerConfiguration.CalendarOpen 0 \
    --TaskSchedulerConfiguration.SelfDepend serial \
    --TaskSchedulerConfiguration.RunPriorityType 6 \
    --TaskSchedulerConfiguration.RetryWaitMinute 5 \
    --TaskSchedulerConfiguration.MaxRetryNumber 4 \
    --TaskSchedulerConfiguration.ExecutionTTLMinute -1 \
    --TaskSchedulerConfiguration.WaitExecutionTotalTTLMinute -1 \
    --TaskSchedulerConfiguration.AllowRedoType ALL \
    --TaskSchedulerConfiguration.InitStrategy T_PLUS_0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "20250910174558007"
        },
        "RequestId": "4c44ef38-55ad-46a7-a257-554c47d1758e"
    }
}
```

