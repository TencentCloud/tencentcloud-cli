**Example 1: 测试**

测试

Input: 

```
tccli wedata DescribeAllUsedVersionSon --cli-unfold-argument  \
    --SearchCondition.Keyword 20230313145539749 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "BrokerIp": "any",
                    "ClusterId": null,
                    "CreateTime": "2023-03-13 14:56:23",
                    "Creator": "stackxchen",
                    "Crontab": null,
                    "CrontabExpression": null,
                    "CycleNum": null,
                    "CycleStep": 1,
                    "CycleType": "ONEOFF_CYCLE",
                    "CycleUnit": null,
                    "DelayTime": 0,
                    "DependencyRel": "and",
                    "DependencyWorkflow": "no",
                    "EndDate": null,
                    "EndTime": "2023-03-13 23:59:59",
                    "EventListenerConfig": null,
                    "EventPublisherConfig": null,
                    "ExecutionEndTime": null,
                    "ExecutionStartTime": null,
                    "ExecutionTTL": -1,
                    "FirstRunTime": null,
                    "FirstSubmitTime": null,
                    "FolderId": null,
                    "FolderName": null,
                    "InCharge": ";stackxchen;",
                    "InChargeId": "100028590605",
                    "InitStrategy": null,
                    "InstanceInitStrategy": "T_PLUS_0",
                    "LastSchedulerCommitTime": null,
                    "LastUpdate": "2023-03-13 06:56:46",
                    "Layer": null,
                    "LeftCoordinate": 710,
                    "MaxDateTime": null,
                    "MinDateTime": null,
                    "NormalizedJobStartTime": null,
                    "Notes": "",
                    "OwnId": "100028448903",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": null,
                    "ProjectName": "调度dev验证项目",
                    "RealWorkflowId": null,
                    "ResourceGroup": "20221229154930684210",
                    "RetryAble": 1,
                    "RetryWait": 5,
                    "RunPriority": 6,
                    "ScheduleDesc": null,
                    "SchedulerDesc": null,
                    "SelfDepend": "serial",
                    "ShowWorkflow": false,
                    "StartDate": null,
                    "StartTime": "2023-03-13 14:55:53",
                    "StartupTime": 0,
                    "Status": "NS",
                    "TaskAction": "",
                    "TaskId": "20230313145623119",
                    "TaskLinkInfo": null,
                    "TaskName": "son_task",
                    "TaskType": {
                        "TypeDesc": "Shell",
                        "TypeId": 35,
                        "TypeSort": "数据计算"
                    },
                    "TaskTypeDesc": null,
                    "TaskTypeId": null,
                    "TenantId": "1315051789",
                    "TopCoordinate": 520,
                    "TryLimit": 5,
                    "UpdateTime": null,
                    "UpdateUser": null,
                    "UpdateUserId": null,
                    "UserId": "100028590605",
                    "VirtualFlag": false,
                    "VirtualTaskId": null,
                    "VirtualTaskStatus": null,
                    "WorkflowId": "d3398ce9-8743-11ed-8909-bc97e105ba60",
                    "WorkflowName": "flow_01",
                    "YarnQueue": null
                }
            ],
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "2d237737-c614-4483-a70a-4e84735fb09a"
    }
}
```

