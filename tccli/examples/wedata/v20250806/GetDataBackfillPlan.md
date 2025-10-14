**Example 1: 获取补录详情**



Input: 

```
tccli wedata GetDataBackfillPlan --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --DataBackfillPlanId 13faeebf-4c61-4289-924b-7fc8b6f8ca6a \
    --TimeZone UTC+8
```

Output: 
```
{
    "Response": {
        "Data": {
            "CheckParentType": "NONE",
            "CompletePercent": 0,
            "CreateUserUin": "100028579606",
            "DataBackfillPlanId": "13faeebf-4c61-4289-924b-7fc8b6f8ca6a",
            "DataBackfillPlanName": "5949f539-721c-499c-87ce-3f027550b02a",
            "DataBackfillRangeList": [
                {
                    "EndDate": "2025-09-02",
                    "ExecutionEndTime": "23:59",
                    "ExecutionStartTime": "00:00",
                    "StartDate": "2025-09-02"
                }
            ],
            "DataTimeOrder": "NORMAL",
            "EndTime": null,
            "IntegrationResourceGroupId": null,
            "ProjectId": "1460947878944567296",
            "RedefineCycleType": null,
            "RedefineParallelNum": null,
            "RedefineParamList": null,
            "RedefineSelfWorkflowDependency": "no",
            "SchedulerResourceGroupId": "20240222212719833743",
            "SkipEventListening": true,
            "StartTime": null,
            "SuccessPercent": 0,
            "TaskIds": [
                "20250827115253729"
            ]
        },
        "RequestId": "d755a2d0-fb5c-463b-8d7e-5e360b46a941"
    }
}
```

