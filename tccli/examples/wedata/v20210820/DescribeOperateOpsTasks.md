**Example 1: 失败示例**

失败示例

Input: 

```
tccli wedata DescribeOperateOpsTasks --cli-unfold-argument  \
    --ProjectId 1470561602745229312
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "2aa47359-f740-4c00-a91d-51820f08e30f"
    }
}
```

**Example 2: 任务列表查询**

任务列表查询

Input: 

```
tccli wedata DescribeOperateOpsTasks --cli-unfold-argument  \
    --WorkFlowIdList 1282d8d2-68e0-11ee-8d13-a411120f8272 \
    --TaskIdList 20231220103934257 \
    --ProjectId 1531609696110365952
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "BrokerIp": null,
                    "ClusterId": null,
                    "CreateTime": "2023-12-20 20:40:59",
                    "Creator": "MaksimGuo",
                    "Crontab": null,
                    "CrontabExpression": null,
                    "CycleNum": 1,
                    "CycleStep": null,
                    "CycleType": null,
                    "CycleUnit": "D",
                    "DelayTime": 0,
                    "DependencyRel": null,
                    "DependencyWorkflow": null,
                    "EndDate": "2099-12-31 23:59:59",
                    "EndTime": null,
                    "EventListenerConfig": null,
                    "EventPublisherConfig": null,
                    "ExecutionEndTime": null,
                    "ExecutionStartTime": null,
                    "ExecutionTTL": -1,
                    "ExecutorGroupId": null,
                    "ExecutorGroupName": null,
                    "FirstRunTime": "2023-10-12 17:18:45",
                    "FirstSubmitTime": "2023-12-21 21:06:36",
                    "FolderId": "0ab0ffbd-68e0-11ee-8d13-a4ae120f8272",
                    "FolderName": "jianweisong",
                    "InCharge": "MaksimGuo",
                    "InChargeId": null,
                    "InitStrategy": "T+0",
                    "InstanceInitStrategy": null,
                    "LastSchedulerCommitTime": "2023-12-21 21:06:36",
                    "LastUpdate": null,
                    "Layer": null,
                    "LeftCoordinate": 367,
                    "MaxDateTime": null,
                    "MinDateTime": null,
                    "NormalizedJobStartTime": null,
                    "Notes": null,
                    "OwnId": null,
                    "ProductName": null,
                    "ProjectId": "1531609696090365952",
                    "ProjectIdent": "project_wedata",
                    "ProjectName": "project_wedata",
                    "RealWorkflowId": null,
                    "ResourceGroup": null,
                    "RetryAble": 1,
                    "RetryWait": 5,
                    "RunPriority": 6,
                    "ScheduleDesc": "每天00:00执行一次",
                    "SchedulerDesc": null,
                    "SelfDepend": "serial",
                    "ShowWorkflow": false,
                    "SourceServiceId": null,
                    "SourceServiceType": null,
                    "StartDate": "2023-10-12 17:18:45",
                    "StartTime": null,
                    "StartupTime": null,
                    "Status": "F",
                    "TargetServiceId": null,
                    "TargetServiceType": null,
                    "TaskAction": "",
                    "TaskId": "20231220203934257",
                    "TaskLinkInfo": null,
                    "TaskName": "1111asdasdadsd",
                    "TaskType": null,
                    "TaskTypeDesc": "MapReduce",
                    "TaskTypeId": 92,
                    "TenantId": "1315051789",
                    "TopCoordinate": 227,
                    "TryLimit": 5,
                    "UpdateTime": null,
                    "UpdateUser": "MaksimGuo",
                    "UpdateUserId": "100029483142",
                    "UserId": "100029483142",
                    "VirtualFlag": false,
                    "VirtualTaskId": null,
                    "VirtualTaskStatus": null,
                    "WorkflowId": "1282d8d2-68e0-11ee-8d13-a4ae120f8272",
                    "WorkflowName": "1002",
                    "YarnQueue": null,
                    "TasksStr": "testss",
                    "Submit": true
                }
            ],
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "ce9d691e-47fc-4378-92db-3fa248e84166"
    }
}
```

