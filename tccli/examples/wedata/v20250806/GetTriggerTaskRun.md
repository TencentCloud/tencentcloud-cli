**Example 1: 查询任务运行详情示例**



Input: 

```
tccli wedata GetTriggerTaskRun --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskExecutionId 436462d0-d573-4b70-a0e3-b73d7f4f2492
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "1764317400033",
            "CreateUin": null,
            "CycleType": "MINUTE_CYCLE",
            "DependOnList": null,
            "DependenceFinishedTime": "1764317400081",
            "ErrorCodeStr": null,
            "ExecuteUserName": null,
            "ExecuteUserUin": "100044422442",
            "ExecutionEndTime": "1764317407000",
            "ExecutionId": "436462d0-d573-4b70-a0e3-b73d7f4f2492",
            "ExecutionResult": null,
            "ExecutionStartTime": "1764317405000",
            "ExecutionState": "SUCCESS",
            "ExecutionTime": "2000",
            "FolderId": null,
            "FolderName": null,
            "IsLatestExecution": true,
            "IssueTime": "1764317400647",
            "JobId": "6820251128161000021",
            "LeftCoordinate": null,
            "ProjectId": "1460947878944567296",
            "RerunTimes": 0,
            "ResourceGroupId": "20240222212719833743",
            "ResourceGroupName": null,
            "RetryTimes": 0,
            "RunParams": "{\"project112\":\"12\"}",
            "SupportRerun": false,
            "TaskId": "20251122104618492",
            "TaskName": "bonney_python_copy_20251122095620980_copy_20251122102557385_copy_20251122104618362",
            "TaskType": "PYTHON",
            "TaskTypeExtensions": "{\"calendar_id\":\"\",\"python_type\":\"python3\",\"startupTime\":\"0\",\"calendar_open\":\"\",\"waitExecutionTotalTTL\":\"-1\",\"calendar_name\":\"\",\"executionTTLStrategy\":\"fail\",\"bucket\":\"wedata-fusion-dev-1257305158\",\"specLabelConfItems\":\"eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ==\",\"waitExecutionTotalTTLStrategy\":\"fail\",\"python_sub_version\":\"python3.11\",\"brokerIp\":\"any\",\"tenantId\":\"1257305158\",\"ftp.file.name\":\"https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com//datastudio/project/1460947878944567296/bonneyyu/bonneyyu_test2/bonney_python_20251122104618492_20251122165921280.py\",\"region\":\"ap-nanjing\",\"runPriority\":\"6\",\"extraInfo\":\"{\\\"fromMapping\\\":false}\"}",
            "TaskTypeId": 30,
            "TaskVersionId": "342e66dc-ff00-4d91-b51d-accdf4d5adb5",
            "Timezone": "Asia/Shanghai",
            "TopCoordinate": null,
            "TriggerType": "Scheduler",
            "UpdateTime": "1764317407918",
            "UserNameInCharge": "bonneyyu",
            "UserUinInCharge": "100044422442",
            "WaitTime": "4967",
            "WorkflowExecutionId": "5071df03-1151-4bd5-9a91-b9cf1bb01b78",
            "WorkflowExecutionState": "SUCCESS",
            "WorkflowId": "b0a148ad-ce76-4a75-8a1a-14e1994f2675",
            "WorkflowName": "bonneyyu_test5",
            "WorkflowParams": "{\"project112\":\"12\"}"
        },
        "RequestId": "95def480-2558-46a5-94d2-1a1b6e70db50"
    }
}
```

