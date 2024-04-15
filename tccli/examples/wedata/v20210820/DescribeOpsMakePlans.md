**Example 1: 获取补录计划**

数据补录-获取补录计划

Input: 

```
tccli wedata DescribeOpsMakePlans --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --ProjectId 147056160274522xxxx
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
                    "CheckParent": false,
                    "CompletePercent": 100,
                    "CreateTime": "2023-05-28 23:02:46",
                    "Creator": "creatorxxx",
                    "CreatorId": "10000000xxxx",
                    "IntegrationResourceGroup": "",
                    "MakeDatetimeList": [
                        {
                            "EndDate": "2023-05-26",
                            "EndTime": "03:59",
                            "StartDate": "2023-05-26",
                            "StartTime": "03:00"
                        }
                    ],
                    "MakeName": "patch_20230528230215_xx",
                    "MapParamList": [],
                    "ParallelNum": 4,
                    "PlanId": "e0bed861-0e95-44ca-9d10-28f2xxxxxxxx",
                    "ProjectId": "14705616027xxxxxxxx",
                    "Remark": null,
                    "SameCycle": true,
                    "SameSelfDependType": false,
                    "SchedulerResourceGroup": "",
                    "SourceTaskCycle": null,
                    "SuccessPercent": 100,
                    "TargetTaskAction": 1,
                    "TargetTaskCycle": "month",
                    "TaskCount": 1,
                    "TaskIdList": [
                        "2023052809431xxxx"
                    ],
                    "SchedulerResourceGroupName": null,
                    "IntegrationResourceGroupName": null,
                    "CheckParentType": null
                }
            ]
        },
        "RequestId": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    }
}
```

