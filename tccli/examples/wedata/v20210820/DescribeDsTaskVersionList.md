**Example 1: 拉取任务版本列表**

拉取任务版本列表

Input: 

```
tccli wedata DescribeDsTaskVersionList --cli-unfold-argument  \
    --ProjectId 1212 \
    --TaskId 12321312
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "VersionId": "213213",
                "TaskId": "21312321",
                "VersionNum": "1",
                "VersionRemark": "1",
                "Creator": "12312",
                "CreateTime": "null",
                "UpdateTime": "null",
                "LastSchedulerCommitTime": "131231",
                "UsedVersion": 0,
                "TaskInfo": {
                    "TaskId": "12312",
                    "VirtualTaskId": "12312",
                    "VirtualFlag": true,
                    "TaskName": "12312",
                    "WorkflowId": "12312",
                    "RealWorkflowId": "12312",
                    "WorkflowName": "12312",
                    "FolderId": "1212",
                    "FolderName": "321312",
                    "CreateTime": "1231231",
                    "LastUpdate": "1231231",
                    "Status": "1231231",
                    "InCharge": "1231231",
                    "InChargeId": "1231231",
                    "StartTime": "null",
                    "EndTime": "null",
                    "ExecutionStartTime": "null",
                    "ExecutionEndTime": "null",
                    "ProjectId": "1231231",
                    "ProjectIdent": "1231231",
                    "ProjectName": "1231231",
                    "CycleType": "1231231",
                    "CycleStep": 0,
                    "CrontabExpression": "1231231",
                    "DelayTime": 0,
                    "StartupTime": 0,
                    "RetryWait": 0,
                    "Retriable": 0,
                    "TaskAction": "1231231",
                    "TryLimit": 0,
                    "RunPriority": 0,
                    "TaskType": {
                        "TypeId": 0,
                        "TypeDesc": "1231231",
                        "CreateTime": "1231231",
                        "SourceServerType": "1231231",
                        "TargetServerType": "1231231",
                        "RunJarName": "1231231",
                        "KillAble": 0,
                        "TypeSort": "1231231",
                        "InCharge": "1231231",
                        "BrokerParallelism": 0,
                        "TaskParallelism": 0,
                        "DoRedoParallelism": 0,
                        "DowngradePriorityTries": 0,
                        "RetryWait": 0,
                        "RetryLimit": 0,
                        "DefaultAliveWait": 0,
                        "PollingSeconds": 0,
                        "ParamList": "1231231",
                        "TaskTypeExtension": [
                            {
                                "TaskTypeExtKey": "1231231",
                                "TaskTypeExtValue": {
                                    "TypeId": 0,
                                    "PropName": "1231231",
                                    "PropLabel": "1231231",
                                    "DefaultFlag": 0,
                                    "VisibleFlag": 0,
                                    "PropDesc": "1231231",
                                    "RankId": 0,
                                    "InputType": "1231231",
                                    "ValueType": "1231231",
                                    "DefaultValue": "1231231",
                                    "CandidateValues": "1231231",
                                    "IsMandatory": 0,
                                    "MaxValue": 0,
                                    "MinValue": 0,
                                    "ConfLevel": 0,
                                    "CandidateTexts": "1231231",
                                    "CopyKey": 0,
                                    "Regex": "1231231",
                                    "Tip": "1231231",
                                    "Candidates": [
                                        {
                                            "Value": "1231231",
                                            "ValueDesc": "1231231"
                                        }
                                    ]
                                }
                            }
                        ],
                        "FileType": "1231231",
                        "SelectFilePath": true,
                        "ExcludeCommonLib": true,
                        "PostHooks": "1231231"
                    },
                    "BrokerIp": "1231231",
                    "ClusterId": "1231231",
                    "MinDateTime": "1231231",
                    "MaxDateTime": "1231231",
                    "ExecutionTTL": 0,
                    "SelfDepend": "1231231",
                    "LeftCoordinate": 0,
                    "TopCoordinate": 0,
                    "TaskExt": {
                        "TaskId": "1231231",
                        "Properties": [
                            {
                                "ParamKey": "1231231",
                                "ParamValue": "1231231"
                            }
                        ],
                        "DryRunExtAttributes": [
                            {
                                "Key": "1231231",
                                "Value": "1231231",
                                "Description": "1231231"
                            }
                        ],
                        "DryRunParameter": [
                            {
                                "Key": "1231231",
                                "Value": "1231231",
                                "Description": "1231231"
                            }
                        ]
                    },
                    "Properties": "1231231",
                    "Notes": "1231231",
                    "InstanceInitStrategy": "1231231",
                    "YarnQueue": "1231231",
                    "Alarms": [
                        {
                            "AlarmId": "1231231",
                            "TaskId": "1231231",
                            "Status": 0,
                            "AlarmType": "1231231",
                            "AlarmWay": "1231231",
                            "Creator": "1231231",
                            "AlarmRecipient": "1231231",
                            "AlarmRecipientId": "1231231",
                            "ModifyTime": "1231231",
                            "LastFailTime": "1231231",
                            "LastOverTime": "1231231",
                            "LastAlarmTime": "1231231",
                            "AlarmExt": [
                                {
                                    "AlarmId": "1231231",
                                    "PropName": "1231231",
                                    "PropValue": "1231231",
                                    "CreateTime": "1231231",
                                    "ModifyTime": "1231231"
                                }
                            ],
                            "CreateTime": "1231231"
                        }
                    ],
                    "Alarm": "1231231",
                    "ScriptChange": true,
                    "Submit": true,
                    "LastSchedulerCommitTime": "1231231",
                    "NormalizedJobStartTime": "1231231",
                    "RecoverFreezeStartTime": "1231231",
                    "SourceServer": "1231231",
                    "TargetServer": "1231231",
                    "Tasks": null,
                    "Creater": "1231231",
                    "DependencyRel": "1231231",
                    "DependencyWorkflow": "1231231",
                    "EventListenerConfig": "1231231",
                    "EventPublisherConfig": "1231231",
                    "DependencyConfigList": [],
                    "VirtualTaskStatus": "1231231",
                    "RecycleTips": "1231231",
                    "RecycleUser": "1231231",
                    "NewOrUpdate": "1231231",
                    "Params": [
                        {
                            "TaskId": "1231231",
                            "ParamKey": "1231231",
                            "ParamDefine": "1231231",
                            "ParamValue": "1231231",
                            "CreateTime": "1231231",
                            "UpdateTime": "1231231"
                        }
                    ],
                    "TaskLinkInfo": [
                        {
                            "TaskTo": "1231231",
                            "TaskFrom": "1231231",
                            "LinkType": "1231231",
                            "LinkKey": "1231231",
                            "Id": "1231231",
                            "InCharge": "1231231",
                            "LinkDependencyType": "1231231",
                            "Offset": 0,
                            "WorkflowId": "1231231",
                            "RealFromTaskId": "1231231",
                            "RealFromTaskName": "1231231",
                            "RealFromWorkflowId": "1231231",
                            "RealFromWorkflowName": "1231231",
                            "RealProjectId": "1231231",
                            "RealProjectIdent": "1231231",
                            "RealProjectName": "1231231"
                        }
                    ],
                    "ImportResult": true,
                    "ImportErrMsg": "1231231",
                    "ContentType": "1231231",
                    "TaskAutoSubmit": true,
                    "ProductName": "1231231",
                    "OwnId": "1231231",
                    "UserId": "1231231",
                    "TenantId": "1231231",
                    "UpdateUser": "1231231",
                    "UpdateTime": "1231231",
                    "UpdateUserId": "1231231",
                    "SchedulerDesc": "1231231",
                    "ResourceGroup": "1231231",
                    "VersionDesc": "1231231",
                    "LinkId": "1231231",
                    "UserFileId": "1231231",
                    "SourceServiceId": "1231231",
                    "SourceServiceType": "1231231",
                    "TargetServiceId": "1231231",
                    "TargetServiceType": "1231231",
                    "ParamInList": [
                        {
                            "Id": 0,
                            "TaskId": "1231231",
                            "ParamKey": "1231231",
                            "ParamDesc": "1231231",
                            "FromTaskId": "1231231",
                            "FromParamKey": "1231231",
                            "CreateTime": "1231231",
                            "UpdateTime": "1231231",
                            "FromTaskName": "1231231",
                            "FromProjectId": "1231231",
                            "FromProjectName": "1231231"
                        }
                    ],
                    "ParamOutList": [
                        {
                            "Id": 0,
                            "TaskId": "1231231",
                            "ParamKey": "1231231",
                            "ParamDesc": "1231231",
                            "ParamDefine": "1231231",
                            "CreateTime": "1231231",
                            "UpdateTime": "1231231",
                            "TaskName": "1231231",
                            "ProjectId": "1231231",
                            "ProjectName": "1231231"
                        }
                    ],
                    "TaskFolderId": "1231231"
                },
                "ApproveStatus": "1231231",
                "ApproveName": "1231231",
                "TaskEventPublisher": [],
                "TaskRegisterOutputTable": [],
                "TaskLinkInfo": null,
                "TaskInputParam": null,
                "TaskOutputParam": null,
                "TaskParaInfo": null
            }
        ],
        "RequestId": "1231231"
    }
}
```

