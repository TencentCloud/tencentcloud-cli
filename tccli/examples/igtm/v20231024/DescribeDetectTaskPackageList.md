**Example 1: 探测任务套餐列表**

探测任务套餐列表

Input: 

```
tccli igtm DescribeDetectTaskPackageList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "b83ab7db-3a32-42ec-875a-aaff131836f1",
        "TaskPackageSet": [
            {
                "AutoRenewFlag": 1,
                "CostItemList": [
                    {
                        "CostName": "sv_igtm_monitor_task_mt",
                        "CostValue": 1
                    }
                ],
                "CreateTime": "2024-03-13 15:41:10",
                "CurrentDeadline": "2024-04-13 15:41:11",
                "IsExpire": 0,
                "Quota": 50,
                "Remark": "",
                "ResourceId": "task-hzxwlklfznla",
                "ResourceType": "TASK_NUM",
                "Status": "ENABLED"
            },
            {
                "AutoRenewFlag": 0,
                "CostItemList": [
                    {
                        "CostName": "sv_igtm_monitor_task_mt",
                        "CostValue": 1
                    }
                ],
                "CreateTime": "2024-03-13 14:48:20",
                "CurrentDeadline": "2024-03-12 14:48:21",
                "IsExpire": 1,
                "Quota": 1,
                "Remark": "",
                "ResourceId": "task-uukzocrmqior",
                "ResourceType": "TASK_NUM",
                "Status": "ENABLED"
            }
        ],
        "TotalCount": 2
    }
}
```

