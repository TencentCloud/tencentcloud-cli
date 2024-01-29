**Example 1: DescribeWorkflowByFordIds**

DescribeWorkflowByFordIds

Input: 

```
tccli wedata DescribeWorkflowByFordIds --cli-unfold-argument  \
    --ProjectId abc \
    --FolderIdList abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "WorkflowId": "abc",
                "Owner": "abc",
                "OwnerId": "abc",
                "ProjectId": "abc",
                "ProjectIdent": "abc",
                "ProjectName": "abc",
                "WorkflowDesc": "abc",
                "WorkflowName": "abc",
                "FolderId": "abc",
                "SparkParams": "abc",
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
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

