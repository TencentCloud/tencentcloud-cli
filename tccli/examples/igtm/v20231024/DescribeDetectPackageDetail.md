**Example 1: 探测任务包详情**

探测任务包详情

Input: 

```
tccli igtm DescribeDetectPackageDetail --cli-unfold-argument  \
    --ResourceId task-dsdd123xdo
```

Output: 
```
{
    "Response": {
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
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0",
        "ResourceId": "task-hzxwlklfznla",
        "ResourceType": "TASK_NUM",
        "Status": "ENABLED",
        "UsedNum": 17
    }
}
```

