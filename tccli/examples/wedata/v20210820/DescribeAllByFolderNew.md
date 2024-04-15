**Example 1: 测试**

测试

Input: 

```
tccli wedata DescribeAllByFolderNew --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --Folder.Id c789de4f-bcc7-11ed-b7fc-043f72e73c62 \
    --Folder.ProjectId 1460947878944567296 \
    --Workflows.0.WorkflowId f47ac10b-58cc-4372-a567-0e02b2c3d479 \
    --TargetFolderId c123de4f-b127-21cd-b7fc-043f98y73c62 \
    --FindType all \
    --KeyWords 
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "TotalPage": 0,
            "PageCount": 0,
            "PageNumber": 0,
            "PageSize": 0,
            "Items": [
                {
                    "Id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                    "CreateTime": "2023-03-25 09:06:00",
                    "Name": "test",
                    "ProjectId": "1460947878944567296",
                    "UpdateTime": "2023-03-25 09:06:00",
                    "ParentsFolderId": "c789de4f-bcc7-11ed-b7fc-043f72e73c62",
                    "Total": 1,
                    "Workflows": [
                        {
                            "WorkflowId": "c789de4f-bcc7-11ed-b7fc-043f72e73c62",
                            "WorkflowDesc": "wf_0",
                            "WorkflowName": "wf_0",
                            "FolderId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                            "FolderIds": [
                                "f47ac10b-58cc-4372-a567-0e02b2c3d479"
                            ],
                            "Tasks": [
                                {
                                    "TaskId": "20230405060708098",
                                    "VirtualTaskId": "",
                                    "VirtualFlag": false,
                                    "TaskName": "task_1",
                                    "WorkflowId": "c789de4f-bcc7-11ed-b7fc-043f72e73c62",
                                    "RealWorkflowId": "",
                                    "WorkflowName": "wf_0 ",
                                    "FolderId": "f47ac10b-58cc-4372-a567-0e02b2c3d479 ",
                                    "FolderName": "test_dir",
                                    "CreateTime": "2023-08-25 09:06:00 ",
                                    "LastUpdate": "2023-08-25 09:06:00 ",
                                    "Status": "",
                                    "InCharge": "tom",
                                    "InChargeId": "123435345",
                                    "StartTime": "2023-08-25 09:09:00 ",
                                    "EndTime": "2023-08-25 09:15:00 ",
                                    "ExecutionStartTime": "2023-08-25 09:09:00 ",
                                    "ExecutionEndTime": "2023-08-25 09:09:00 ",
                                    "CycleType": "D",
                                    "CycleStep": 1,
                                    "CrontabExpression": "0,1 0 0 0 0",
                                    "DelayTime": 1,
                                    "StartupTime": 1,
                                    "RetryWait": 1,
                                    "RetryAble": 1,
                                    "TaskAction": "",
                                    "TryLimit": 1,
                                    "RunPriority": 1,
                                    "TaskType": {
                                        "TypeDesc": "",
                                        "TypeId": 0,
                                        "TypeSort": ""
                                    },
                                    "BrokerIp": null,
                                    "ClusterId": null,
                                    "MinDateTime": null,
                                    "MaxDateTime": null,
                                    "ExecutionTTL": 0,
                                    "SelfDepend": null,
                                    "LeftCoordinate": 0,
                                    "TopCoordinate": 0,
                                    "Notes": null,
                                    "InstanceInitStrategy": null,
                                    "YarnQueue": null,
                                    "LastSchedulerCommitTime": null,
                                    "NormalizedJobStartTime": null,
                                    "SchedulerDesc": null,
                                    "ResourceGroup": null,
                                    "Creator": null,
                                    "DependencyRel": null,
                                    "DependencyWorkflow": null,
                                    "EventListenerConfig": null,
                                    "EventPublisherConfig": null,
                                    "VirtualTaskStatus": null,
                                    "TaskLinkInfo": {
                                        "Id": null,
                                        "LinkKey": null,
                                        "TaskFrom": null,
                                        "TaskTo": null,
                                        "InCharge": null,
                                        "LinkDependencyType": null,
                                        "Offset": null,
                                        "LinkType": null,
                                        "WorkflowId": null
                                    },
                                    "TargetServiceId": null,
                                    "Submit": null,
                                    "SourceServiceId": null,
                                    "TargetServiceType": null,
                                    "TasksStr": null,
                                    "SourceServiceType": null,
                                    "ProductName": null,
                                    "ProjectId": null,
                                    "ProjectIdent": null,
                                    "ProjectName": null,
                                    "OwnId": null,
                                    "UserId": null,
                                    "TenantId": null,
                                    "UpdateUser": null,
                                    "UpdateTime": null,
                                    "UpdateUserId": null,
                                    "TaskTypeId": 0,
                                    "TaskTypeDesc": null,
                                    "ShowWorkflow": true,
                                    "FirstSubmitTime": null,
                                    "FirstRunTime": null,
                                    "ScheduleDesc": null,
                                    "CycleNum": 0,
                                    "Crontab": null,
                                    "StartDate": null,
                                    "EndDate": null,
                                    "CycleUnit": null,
                                    "InitStrategy": null,
                                    "Layer": null
                                }
                            ],
                            "Links": [
                                {
                                    "Id": null,
                                    "LinkKey": null,
                                    "TaskFrom": null,
                                    "TaskTo": null,
                                    "InCharge": null,
                                    "LinkDependencyType": null,
                                    "Offset": null,
                                    "LinkType": null,
                                    "WorkflowId": null
                                }
                            ],
                            "UserGroupId": null,
                            "UserGroupName": null,
                            "ProjectId": null,
                            "ProjectIdent": null,
                            "ProjectName": null,
                            "Owner": null,
                            "OwnerId": null
                        }
                    ],
                    "TotalFolders": 0,
                    "FoldersList": null,
                    "FindType": null
                }
            ]
        },
        "RequestId": "e125de4f-acc3-22ed-b5fc-123f72e73c62"
    }
}
```

