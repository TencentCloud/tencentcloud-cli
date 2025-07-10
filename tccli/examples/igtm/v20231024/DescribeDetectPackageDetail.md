**Example 1: 探测任务包详情**

探测任务包详情

Input: 

```
tccli igtm DescribeDetectPackageDetail --cli-unfold-argument  \
    --ResourceId xxx
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
        "RequestId": "aace8684-a8d6-454f-8fac-3e398f203620",
        "ResourceId": "task-hzxwlklfznla",
        "ResourceType": "TASK_NUM",
        "Status": "ENABLED",
        "UsedNum": 17
    }
}
```

