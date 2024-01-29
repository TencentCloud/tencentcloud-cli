**Example 1: 成功**

成功

Input: 

```
tccli wedata DescribeInfoTransByTypeIdDs --cli-unfold-argument  \
    --TaskId 20230717115803666 \
    --TypeId 35
```

Output: 
```
{
    "Response": {
        "Data": {
            "Alarm": null,
            "Alarms": [
                {
                    "AlarmExt": [],
                    "AlarmId": "21245706-2456-11ee-8909-bc97e105ba60",
                    "AlarmRecipient": "",
                    "AlarmRecipientId": "",
                    "AlarmType": "overtime",
                    "AlarmWay": "",
                    "CreateTime": "2023-07-17 11:58:03",
                    "Creator": ";jonsljiang;",
                    "LastAlarmTime": null,
                    "LastFailTime": null,
                    "LastOverTime": null,
                    "ModifyTime": "2023-07-17 11:58:03",
                    "Status": 0,
                    "TaskId": "20230717115803666"
                },
                {
                    "AlarmExt": [],
                    "AlarmId": "212620a5-2456-11ee-8909-bc97e105ba60",
                    "AlarmRecipient": "",
                    "AlarmRecipientId": "",
                    "AlarmType": "failure",
                    "AlarmWay": "",
                    "CreateTime": "2023-07-17 11:58:03",
                    "Creator": ";jonsljiang;",
                    "LastAlarmTime": null,
                    "LastFailTime": null,
                    "LastOverTime": null,
                    "ModifyTime": "2023-07-17 11:58:03",
                    "Status": 0,
                    "TaskId": "20230717115803666"
                }
            ],
            "BrokerIp": "any",
            "ClusterId": null,
            "ContentType": null,
            "CreateTime": "2023-07-17 11:58:03",
            "Creater": "jonsljiang",
            "CrontabExpression": null,
            "CycleStep": 1,
            "CycleType": "DAY_CYCLE",
            "DelayTime": 0,
            "DependencyConfigList": null,
            "DependencyRel": "and",
            "DependencyWorkflow": "no",
            "EndTime": "2099-12-31 23:59:59",
            "EventListenerConfig": null,
            "EventPublisherConfig": null,
            "ExecutionEndTime": null,
            "ExecutionStartTime": null,
            "ExecutionTTL": -1,
            "FolderId": null,
            "FolderName": null,
            "ImportErrMsg": null,
            "ImportResult": null,
            "InCharge": "jonsljiang",
            "InChargeId": "100028597773",
            "InstanceInitStrategy": "T_PLUS_0",
            "LastSchedulerCommitTime": null,
            "LastUpdate": "2023-07-17 11:58:03",
            "LeftCoordinate": 338,
            "LinkId": null,
            "MaxDateTime": null,
            "MinDateTime": null,
            "NewOrUpdate": null,
            "NormalizedJobStartTime": null,
            "Notes": null,
            "OwnId": "100028448903",
            "Params": null,
            "ProductName": "DATA_DEV",
            "ProjectId": "1470547050521227264",
            "ProjectIdent": null,
            "ProjectName": null,
            "Properties": null,
            "RealWorkflowId": null,
            "RecoverFreezeStartTime": null,
            "RecycleTips": null,
            "RecycleUser": null,
            "ResourceGroup": null,
            "Retriable": 1,
            "RetryWait": 5,
            "RunPriority": 6,
            "SchedulerDesc": null,
            "ScriptChange": false,
            "SelfDepend": 2,
            "SourceServer": null,
            "StartTime": "2023-05-26 00:00:00",
            "StartupTime": 0,
            "Status": "N",
            "Submit": false,
            "TargetServer": null,
            "TaskAction": "",
            "TaskAutoSubmit": null,
            "TaskExt": {
                "DryRunExtAttributes": null,
                "DryRunParameter": null,
                "Properties": [
                    {
                        "ParamKey": "bucket",
                        "ParamValue": "wedata-fusion-dev-1257305158"
                    },
                    {
                        "ParamKey": "ftp.file.name",
                        "ParamValue": "/datastudio/project/1470547050521227264/jonsljiang/jonsljiang/jonsljiang_sh2.sh"
                    },
                    {
                        "ParamKey": "region",
                        "ParamValue": "ap-nanjing"
                    },
                    {
                        "ParamKey": "extraInfo",
                        "ParamValue": "&&&}"
                    }
                ],
                "TaskId": "20230717115803666"
            },
            "TaskId": "20230717115803666",
            "TaskLinkInfo": null,
            "TaskName": "jonsljiang_sh2",
            "TaskType": {
                "BrokerParallelism": 10,
                "CreateTime": "2022-02-12 03:13:40",
                "DefaultAliveWait": 720,
                "DoRedoParallelism": 10000,
                "DowngradePriorityTries": 2,
                "ExcludeCommonLib": false,
                "FileType": null,
                "InCharge": "admin",
                "KillAble": 0,
                "ParamList": "<parameters><parameter><name>hdpClient</name><value>/usr/hdp/current/hadoop-client</value></parameter><parameter><name>hiveClient</name><value>/usr/hdp/current/hive-client</value></parameter></parameters>",
                "PollingSeconds": 5,
                "PostHooks": null,
                "RetryLimit": 5,
                "RetryWait": 5,
                "RunJarName": "ShellRunner.jar",
                "SelectFilePath": null,
                "SourceServerType": null,
                "TargetServerType": null,
                "TaskParallelism": 10,
                "TaskTypeExtension": [
                    {
                        "TaskTypeExtKey": "endDate",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "",
                            "CandidateValues": "",
                            "ConfLevel": 2,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "",
                            "InputType": "date",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "任务停止生成实例的时间",
                            "PropLabel": "终止时间",
                            "PropName": "endDate",
                            "RankId": 19,
                            "Regex": ".*",
                            "Tip": "need to fulltill rex",
                            "TypeId": 38,
                            "ValueType": "date",
                            "VisibleFlag": 1
                        }
                    },
                    {
                        "TaskTypeExtKey": "brokerIp",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "",
                            "CandidateValues": "",
                            "ConfLevel": 2,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "any",
                            "InputType": "string",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "任务实例执行所在机器ip",
                            "PropLabel": "代理IP",
                            "PropName": "brokerIp",
                            "RankId": 19,
                            "Regex": ".*",
                            "Tip": "need to fulltill rex",
                            "TypeId": 38,
                            "ValueType": "string",
                            "VisibleFlag": 1
                        }
                    },
                    {
                        "TaskTypeExtKey": "cycleNum",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "",
                            "CandidateValues": "",
                            "ConfLevel": 2,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "1",
                            "InputType": "int",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "间隔多少周期执行一次(若是天任务，步数为2，每两天执行一次)",
                            "PropLabel": "步长",
                            "PropName": "cycleNum",
                            "RankId": 19,
                            "Regex": "^[1-9]+[0-9]*?$",
                            "Tip": "必须是正整数",
                            "TypeId": 38,
                            "ValueType": "int",
                            "VisibleFlag": 1
                        }
                    },
                    {
                        "TaskTypeExtKey": "ftp.file.name",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "",
                            "CandidateValues": "",
                            "ConfLevel": 1,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "",
                            "InputType": "button-file",
                            "IsMandatory": 1,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "任务执行资源(zip),不要将资源放到子目录",
                            "PropLabel": "shell任务执行资源(zip)",
                            "PropName": "ftp.file.name",
                            "RankId": 11,
                            "Regex": "zip$",
                            "Tip": "必须是zip结尾文件",
                            "TypeId": 38,
                            "ValueType": "string",
                            "VisibleFlag": 1
                        }
                    },
                    {
                        "TaskTypeExtKey": "taskPriority",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "高,中,低",
                            "CandidateValues": "4,5,6",
                            "ConfLevel": 2,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "6",
                            "InputType": "single-select",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "高优先级任务会优先下发（只对同一类型的任务有效）",
                            "PropLabel": "任务调度优先级",
                            "PropName": "taskPriority",
                            "RankId": 99,
                            "Regex": ".*",
                            "Tip": "need to fulltill rex",
                            "TypeId": 38,
                            "ValueType": "string",
                            "VisibleFlag": 1
                        }
                    },
                    {
                        "TaskTypeExtKey": "tryLimit",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "",
                            "CandidateValues": "",
                            "ConfLevel": 2,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "5",
                            "InputType": "int",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "任务实例尝试运行次数上限（设置为0，任务不下发）",
                            "PropLabel": "最大可运行次数",
                            "PropName": "tryLimit",
                            "RankId": 19,
                            "Regex": "^[1-9]+[0-9]*?$",
                            "Tip": "必须是正整数",
                            "TypeId": 38,
                            "ValueType": "int",
                            "VisibleFlag": 1
                        }
                    },
                    {
                        "TaskTypeExtKey": "shell.cmd",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "",
                            "CandidateValues": "",
                            "ConfLevel": 1,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "",
                            "InputType": "text-single",
                            "IsMandatory": 1,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "要执行的shell脚本的名字(如：script.sh),若在脚本中执行beeline 命令,需要在runner节点安装tez client",
                            "PropLabel": "shell命令",
                            "PropName": "shell.cmd",
                            "RankId": 12,
                            "Regex": ".*",
                            "Tip": "need to fulltill rex",
                            "TypeId": 38,
                            "ValueType": "string",
                            "VisibleFlag": 1
                        }
                    },
                    {
                        "TaskTypeExtKey": "shell.args",
                        "TaskTypeExtValue": {
                            "CandidateTexts": "",
                            "CandidateValues": "",
                            "ConfLevel": 1,
                            "CopyKey": 1,
                            "DefaultFlag": 1,
                            "DefaultValue": "",
                            "InputType": "text-single",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "PropDesc": "要执行的脚本的参数，用空格区分多个参数",
                            "PropLabel": "shell参数",
                            "PropName": "shell.args",
                            "RankId": 13,
                            "Regex": ".*",
                            "Tip": "need to fulltill rex",
                            "TypeId": 38,
                            "ValueType": "string",
                            "VisibleFlag": 1
                        }
                    }
                ],
                "TypeDesc": "SHELL",
                "TypeId": 38,
                "TypeSort": "数据计算"
            },
            "Tasks": null,
            "TenantId": "1315051789",
            "TopCoordinate": 252,
            "TryLimit": 5,
            "UpdateTime": "2023-07-17 11:58:03",
            "UpdateUser": "jonsljiang",
            "UpdateUserId": "100028597773",
            "UserFileId": null,
            "UserId": "100028597773",
            "VersionDesc": null,
            "VirtualFlag": false,
            "VirtualTaskId": null,
            "VirtualTaskStatus": null,
            "WorkflowId": "8833db8e-f870-11ed-8909-bc97e105ba60",
            "WorkflowName": "jonsljiang",
            "YarnQueue": null
        },
        "RequestId": "39cb0b7b-95c7-4cdc-a1e2-ca591b797924"
    }
}
```

**Example 2: 成功示例**

成功示例

Input: 

```
tccli wedata DescribeInfoTransByTypeIdDs --cli-unfold-argument  \
    --TaskId abc \
    --TypeId abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "abc",
            "VirtualTaskId": "abc",
            "VirtualFlag": true,
            "TaskName": "abc",
            "WorkflowId": "abc",
            "RealWorkflowId": "abc",
            "WorkflowName": "abc",
            "FolderId": "abc",
            "FolderName": "abc",
            "CreateTime": "abc",
            "LastUpdate": "abc",
            "Status": "abc",
            "InCharge": "abc",
            "InChargeId": "abc",
            "StartTime": "abc",
            "EndTime": "abc",
            "ExecutionStartTime": "abc",
            "ExecutionEndTime": "abc",
            "ProjectId": "abc",
            "ProjectIdent": "abc",
            "ProjectName": "abc",
            "CycleType": "abc",
            "CycleStep": 0,
            "CrontabExpression": "abc",
            "DelayTime": 0,
            "StartupTime": 0,
            "RetryWait": 0,
            "Retriable": 0,
            "TaskAction": "abc",
            "TryLimit": 0,
            "RunPriority": 0,
            "TaskType": {
                "TypeId": 0,
                "TypeDesc": "abc",
                "CreateTime": "abc",
                "SourceServerType": "abc",
                "TargetServerType": "abc",
                "RunJarName": "abc",
                "KillAble": 0,
                "TypeSort": "abc",
                "InCharge": "abc",
                "BrokerParallelism": 0,
                "TaskParallelism": 0,
                "DoRedoParallelism": 0,
                "DowngradePriorityTries": 0,
                "RetryWait": 0,
                "RetryLimit": 0,
                "DefaultAliveWait": 0,
                "PollingSeconds": 0,
                "ParamList": "abc",
                "TaskTypeExtension": [
                    {
                        "TaskTypeExtKey": "abc",
                        "TaskTypeExtValue": {
                            "TypeId": 0,
                            "PropName": "abc",
                            "PropLabel": "abc",
                            "DefaultFlag": 0,
                            "VisibleFlag": 0,
                            "PropDesc": "abc",
                            "RankId": 0,
                            "InputType": "abc",
                            "ValueType": "abc",
                            "DefaultValue": "abc",
                            "CandidateValues": "abc",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "ConfLevel": 0,
                            "CandidateTexts": "abc",
                            "CopyKey": 0,
                            "Regex": "abc",
                            "Tip": "abc"
                        }
                    }
                ],
                "FileType": "abc",
                "SelectFilePath": true,
                "ExcludeCommonLib": true,
                "PostHooks": "abc"
            },
            "BrokerIp": "abc",
            "ClusterId": "abc",
            "MinDateTime": "abc",
            "MaxDateTime": "abc",
            "ExecutionTTL": 0,
            "SelfDepend": 0,
            "LeftCoordinate": 0,
            "TopCoordinate": 0,
            "TaskExt": {
                "TaskId": "abc",
                "Properties": [
                    {
                        "ParamKey": "abc",
                        "ParamValue": "abc"
                    }
                ],
                "DryRunExtAttributes": [
                    {
                        "Key": "abc",
                        "Value": "abc",
                        "Description": "abc"
                    }
                ],
                "DryRunParameter": [
                    {
                        "Key": "abc",
                        "Value": "abc",
                        "Description": "abc"
                    }
                ]
            },
            "Properties": "abc",
            "Notes": "abc",
            "InstanceInitStrategy": "abc",
            "YarnQueue": "abc",
            "Alarms": [
                {
                    "AlarmId": "abc",
                    "TaskId": "abc",
                    "Status": 0,
                    "AlarmType": "abc",
                    "AlarmWay": "abc",
                    "Creator": "abc",
                    "AlarmRecipient": "abc",
                    "AlarmRecipientId": "abc",
                    "ModifyTime": "abc",
                    "LastFailTime": "abc",
                    "LastOverTime": "abc",
                    "LastAlarmTime": "abc",
                    "AlarmExt": [
                        {
                            "AlarmId": "abc",
                            "PropName": "abc",
                            "PropValue": "abc",
                            "CreateTime": "abc",
                            "ModifyTime": "abc"
                        }
                    ],
                    "CreateTime": "abc"
                }
            ],
            "Alarm": "abc",
            "ScriptChange": true,
            "Submit": true,
            "LastSchedulerCommitTime": "abc",
            "NormalizedJobStartTime": "abc",
            "RecoverFreezeStartTime": "abc",
            "SourceServer": "abc",
            "TargetServer": "abc",
            "Tasks": [
                {
                    "TaskId": "abc",
                    "VirtualTaskId": "abc",
                    "VirtualFlag": true,
                    "TaskName": "abc",
                    "WorkflowId": "abc",
                    "RealWorkflowId": "abc",
                    "WorkflowName": "abc",
                    "FolderId": "abc",
                    "FolderName": "abc",
                    "CreateTime": "abc",
                    "LastUpdate": "abc",
                    "Status": "abc",
                    "InCharge": "abc",
                    "InChargeId": "abc",
                    "StartTime": "abc",
                    "EndTime": "abc",
                    "ExecutionStartTime": "abc",
                    "ExecutionEndTime": "abc",
                    "ProjectId": "abc",
                    "ProjectIdent": "abc",
                    "ProjectName": "abc",
                    "CycleType": "abc",
                    "CycleStep": 0,
                    "CrontabExpression": "abc",
                    "DelayTime": 0,
                    "StartupTime": 0,
                    "RetryWait": 0,
                    "Retriable": 0,
                    "TaskAction": "abc",
                    "TryLimit": 0,
                    "RunPriority": 0,
                    "TaskType": {
                        "TypeId": 0,
                        "TypeDesc": "abc",
                        "CreateTime": "abc",
                        "SourceServerType": "abc",
                        "TargetServerType": "abc",
                        "RunJarName": "abc",
                        "KillAble": 0,
                        "TypeSort": "abc",
                        "InCharge": "abc",
                        "BrokerParallelism": 0,
                        "TaskParallelism": 0,
                        "DoRedoParallelism": 0,
                        "DowngradePriorityTries": 0,
                        "RetryWait": 0,
                        "RetryLimit": 0,
                        "DefaultAliveWait": 0,
                        "PollingSeconds": 0,
                        "ParamList": "abc",
                        "TaskTypeExtension": [
                            {
                                "TaskTypeExtKey": "abc",
                                "TaskTypeExtValue": {
                                    "TypeId": 0,
                                    "PropName": "abc",
                                    "PropLabel": "abc",
                                    "DefaultFlag": 0,
                                    "VisibleFlag": 0,
                                    "PropDesc": "abc",
                                    "RankId": 0,
                                    "InputType": "abc",
                                    "ValueType": "abc",
                                    "DefaultValue": "abc",
                                    "CandidateValues": "abc",
                                    "IsMandatory": 0,
                                    "MaxValue": 0,
                                    "MinValue": 0,
                                    "ConfLevel": 0,
                                    "CandidateTexts": "abc",
                                    "CopyKey": 0,
                                    "Regex": "abc",
                                    "Tip": "abc"
                                }
                            }
                        ],
                        "FileType": "abc",
                        "SelectFilePath": true,
                        "ExcludeCommonLib": true,
                        "PostHooks": "abc"
                    },
                    "BrokerIp": "abc",
                    "ClusterId": "abc",
                    "MinDateTime": "abc",
                    "MaxDateTime": "abc",
                    "ExecutionTTL": 0,
                    "SelfDepend": 0,
                    "LeftCoordinate": 0,
                    "TopCoordinate": 0,
                    "TaskExt": {
                        "TaskId": "abc",
                        "Properties": [
                            {
                                "ParamKey": "abc",
                                "ParamValue": "abc"
                            }
                        ],
                        "DryRunExtAttributes": [
                            {
                                "Key": "abc",
                                "Value": "abc",
                                "Description": "abc"
                            }
                        ]
                    },
                    "Properties": "abc",
                    "Notes": "abc",
                    "InstanceInitStrategy": "abc",
                    "YarnQueue": "abc",
                    "Alarms": [
                        {
                            "AlarmId": "abc",
                            "TaskId": "abc",
                            "Status": 0,
                            "AlarmType": "abc",
                            "AlarmWay": "abc",
                            "Creator": "abc",
                            "AlarmRecipient": "abc",
                            "AlarmRecipientId": "abc",
                            "ModifyTime": "abc",
                            "LastFailTime": "abc",
                            "LastOverTime": "abc",
                            "LastAlarmTime": "abc",
                            "AlarmExt": [
                                {
                                    "AlarmId": "abc",
                                    "PropName": "abc",
                                    "PropValue": "abc",
                                    "CreateTime": "abc",
                                    "ModifyTime": "abc"
                                }
                            ],
                            "CreateTime": "abc"
                        }
                    ],
                    "Alarm": "abc",
                    "ScriptChange": true,
                    "Submit": true,
                    "LastSchedulerCommitTime": "abc",
                    "NormalizedJobStartTime": "abc",
                    "RecoverFreezeStartTime": "abc",
                    "SourceServer": "abc",
                    "TargetServer": "abc",
                    "Tasks": [
                        {
                            "TaskId": "abc",
                            "VirtualTaskId": "abc",
                            "VirtualFlag": true,
                            "TaskName": "abc",
                            "WorkflowId": "abc",
                            "RealWorkflowId": "abc",
                            "WorkflowName": "abc",
                            "FolderId": "abc",
                            "FolderName": "abc",
                            "CreateTime": "abc",
                            "LastUpdate": "abc",
                            "Status": "abc",
                            "InCharge": "abc",
                            "InChargeId": "abc",
                            "StartTime": "abc",
                            "EndTime": "abc",
                            "ExecutionStartTime": "abc",
                            "ExecutionEndTime": "abc",
                            "ProjectId": "abc",
                            "ProjectIdent": "abc",
                            "ProjectName": "abc",
                            "CycleType": "abc",
                            "CycleStep": 0,
                            "CrontabExpression": "abc",
                            "DelayTime": 0,
                            "StartupTime": 0,
                            "RetryWait": 0,
                            "Retriable": 0,
                            "TaskAction": "abc",
                            "TryLimit": 0,
                            "RunPriority": 0,
                            "TaskType": {
                                "TypeId": 0,
                                "TypeDesc": "abc",
                                "CreateTime": "abc",
                                "SourceServerType": "abc",
                                "TargetServerType": "abc",
                                "RunJarName": "abc",
                                "KillAble": 0,
                                "TypeSort": "abc",
                                "InCharge": "abc",
                                "BrokerParallelism": 0,
                                "TaskParallelism": 0,
                                "DoRedoParallelism": 0,
                                "DowngradePriorityTries": 0,
                                "RetryWait": 0,
                                "RetryLimit": 0,
                                "DefaultAliveWait": 0,
                                "PollingSeconds": 0,
                                "ParamList": "abc",
                                "TaskTypeExtension": [
                                    {
                                        "TaskTypeExtKey": "abc",
                                        "TaskTypeExtValue": {
                                            "TypeId": 0,
                                            "PropName": "abc",
                                            "PropLabel": "abc",
                                            "DefaultFlag": 0,
                                            "VisibleFlag": 0,
                                            "PropDesc": "abc",
                                            "RankId": 0,
                                            "InputType": "abc",
                                            "ValueType": "abc",
                                            "DefaultValue": "abc",
                                            "CandidateValues": "abc",
                                            "IsMandatory": 0,
                                            "MaxValue": 0,
                                            "MinValue": 0,
                                            "ConfLevel": 0,
                                            "CandidateTexts": "abc",
                                            "CopyKey": 0,
                                            "Regex": "abc",
                                            "Tip": "abc"
                                        }
                                    }
                                ],
                                "FileType": "abc",
                                "SelectFilePath": true,
                                "ExcludeCommonLib": true,
                                "PostHooks": "abc"
                            },
                            "BrokerIp": "abc",
                            "ClusterId": "abc",
                            "MinDateTime": "abc",
                            "MaxDateTime": "abc",
                            "ExecutionTTL": 0,
                            "SelfDepend": 0,
                            "LeftCoordinate": 0,
                            "TopCoordinate": 0,
                            "TaskExt": {
                                "TaskId": "abc",
                                "Properties": [
                                    {
                                        "ParamKey": "abc",
                                        "ParamValue": "abc"
                                    }
                                ]
                            },
                            "Properties": "abc",
                            "Notes": "abc",
                            "InstanceInitStrategy": "abc",
                            "YarnQueue": "abc",
                            "Alarms": [
                                {
                                    "AlarmId": "abc",
                                    "TaskId": "abc",
                                    "Status": 0,
                                    "AlarmType": "abc",
                                    "AlarmWay": "abc",
                                    "Creator": "abc",
                                    "AlarmRecipient": "abc",
                                    "AlarmRecipientId": "abc",
                                    "ModifyTime": "abc",
                                    "LastFailTime": "abc",
                                    "LastOverTime": "abc",
                                    "LastAlarmTime": "abc",
                                    "AlarmExt": [
                                        {
                                            "AlarmId": "abc",
                                            "PropName": "abc",
                                            "PropValue": "abc",
                                            "CreateTime": "abc",
                                            "ModifyTime": "abc"
                                        }
                                    ],
                                    "CreateTime": "abc"
                                }
                            ],
                            "Alarm": "abc",
                            "ScriptChange": true,
                            "Submit": true,
                            "LastSchedulerCommitTime": "abc",
                            "NormalizedJobStartTime": "abc",
                            "RecoverFreezeStartTime": "abc",
                            "SourceServer": "abc",
                            "TargetServer": "abc",
                            "Creater": "abc",
                            "DependencyRel": "abc",
                            "DependencyWorkflow": "abc",
                            "EventListenerConfig": "abc",
                            "EventPublisherConfig": "abc",
                            "DependencyConfigList": [
                                {
                                    "MainCyclicConfig": "abc",
                                    "SubordinateCyclicConfig": "abc",
                                    "DependencyStrategy": {
                                        "PollingNullStrategy": "abc"
                                    }
                                }
                            ],
                            "VirtualTaskStatus": "abc",
                            "RecycleTips": "abc",
                            "RecycleUser": "abc",
                            "NewOrUpdate": "abc",
                            "Params": [
                                {
                                    "TaskId": "abc",
                                    "ParamKey": "abc",
                                    "ParamDefine": "abc",
                                    "ParamValue": "abc",
                                    "CreateTime": "abc",
                                    "UpdateTime": "abc"
                                }
                            ],
                            "TaskLinkInfo": [
                                {
                                    "TaskTo": "abc",
                                    "TaskFrom": "abc",
                                    "LinkType": "abc",
                                    "LinkKey": "abc",
                                    "Id": "abc",
                                    "InCharge": "abc",
                                    "LinkDependencyType": "abc",
                                    "Offset": 0,
                                    "WorkflowId": "abc",
                                    "RealFromTaskId": "abc",
                                    "RealFromTaskName": "abc",
                                    "RealFromWorkflowId": "abc",
                                    "RealFromWorkflowName": "abc",
                                    "RealProjectId": "abc",
                                    "RealProjectIdent": "abc",
                                    "RealProjectName": "abc"
                                }
                            ],
                            "ImportResult": true,
                            "ImportErrMsg": "abc",
                            "ContentType": "abc",
                            "TaskAutoSubmit": true,
                            "ProductName": "abc",
                            "OwnId": "abc",
                            "UserId": "abc",
                            "TenantId": "abc",
                            "UpdateUser": "abc",
                            "UpdateTime": "abc",
                            "UpdateUserId": "abc",
                            "SchedulerDesc": "abc",
                            "ResourceGroup": "abc",
                            "VersionDesc": "abc",
                            "LinkId": "abc",
                            "UserFileId": "abc"
                        }
                    ],
                    "Creater": "abc",
                    "DependencyRel": "abc",
                    "DependencyWorkflow": "abc",
                    "EventListenerConfig": "abc",
                    "EventPublisherConfig": "abc",
                    "DependencyConfigList": [
                        {
                            "MainCyclicConfig": "abc",
                            "SubordinateCyclicConfig": "abc",
                            "DependencyStrategy": {
                                "PollingNullStrategy": "abc"
                            }
                        }
                    ],
                    "VirtualTaskStatus": "abc",
                    "RecycleTips": "abc",
                    "RecycleUser": "abc",
                    "NewOrUpdate": "abc",
                    "Params": [
                        {
                            "TaskId": "abc",
                            "ParamKey": "abc",
                            "ParamDefine": "abc",
                            "ParamValue": "abc",
                            "CreateTime": "abc",
                            "UpdateTime": "abc"
                        }
                    ],
                    "TaskLinkInfo": [
                        {
                            "TaskTo": "abc",
                            "TaskFrom": "abc",
                            "LinkType": "abc",
                            "LinkKey": "abc",
                            "Id": "abc",
                            "InCharge": "abc",
                            "LinkDependencyType": "abc",
                            "Offset": 0,
                            "WorkflowId": "abc",
                            "RealFromTaskId": "abc",
                            "RealFromTaskName": "abc",
                            "RealFromWorkflowId": "abc",
                            "RealFromWorkflowName": "abc",
                            "RealProjectId": "abc",
                            "RealProjectIdent": "abc",
                            "RealProjectName": "abc"
                        }
                    ],
                    "ImportResult": true,
                    "ImportErrMsg": "abc",
                    "ContentType": "abc",
                    "TaskAutoSubmit": true,
                    "ProductName": "abc",
                    "OwnId": "abc",
                    "UserId": "abc",
                    "TenantId": "abc",
                    "UpdateUser": "abc",
                    "UpdateTime": "abc",
                    "UpdateUserId": "abc",
                    "SchedulerDesc": "abc",
                    "ResourceGroup": "abc",
                    "VersionDesc": "abc",
                    "LinkId": "abc",
                    "UserFileId": "abc"
                }
            ],
            "Creater": "abc",
            "DependencyRel": "abc",
            "DependencyWorkflow": "abc",
            "EventListenerConfig": "abc",
            "EventPublisherConfig": "abc",
            "DependencyConfigList": [
                {
                    "MainCyclicConfig": "abc",
                    "SubordinateCyclicConfig": "abc",
                    "DependencyStrategy": {
                        "PollingNullStrategy": "abc"
                    }
                }
            ],
            "VirtualTaskStatus": "abc",
            "RecycleTips": "abc",
            "RecycleUser": "abc",
            "NewOrUpdate": "abc",
            "Params": [
                {
                    "TaskId": "abc",
                    "ParamKey": "abc",
                    "ParamDefine": "abc",
                    "ParamValue": "abc",
                    "CreateTime": "abc",
                    "UpdateTime": "abc"
                }
            ],
            "TaskLinkInfo": [
                {
                    "TaskTo": "abc",
                    "TaskFrom": "abc",
                    "LinkType": "abc",
                    "LinkKey": "abc",
                    "Id": "abc",
                    "InCharge": "abc",
                    "LinkDependencyType": "abc",
                    "Offset": 0,
                    "WorkflowId": "abc",
                    "RealFromTaskId": "abc",
                    "RealFromTaskName": "abc",
                    "RealFromWorkflowId": "abc",
                    "RealFromWorkflowName": "abc",
                    "RealProjectId": "abc",
                    "RealProjectIdent": "abc",
                    "RealProjectName": "abc"
                }
            ],
            "ImportResult": true,
            "ImportErrMsg": "abc",
            "ContentType": "abc",
            "TaskAutoSubmit": true,
            "ProductName": "abc",
            "OwnId": "abc",
            "UserId": "abc",
            "TenantId": "abc",
            "UpdateUser": "abc",
            "UpdateTime": "abc",
            "UpdateUserId": "abc",
            "SchedulerDesc": "abc",
            "ResourceGroup": "abc",
            "VersionDesc": "abc",
            "LinkId": "abc",
            "UserFileId": "abc"
        },
        "RequestId": "abc"
    }
}
```

