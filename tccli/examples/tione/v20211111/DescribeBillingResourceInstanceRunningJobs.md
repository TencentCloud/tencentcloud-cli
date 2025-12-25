**Example 1: 查询资源组节点运行中的任务**



Input: 

```
tccli tione DescribeBillingResourceInstanceRunningJobs --cli-unfold-argument  \
    --ResourceGroupId rsg-23d23 \
    --ResourceInstanceId sm-f342u8
```

Output: 
```
{
    "Response": {
        "RequestId": "02be3c0f-d1f1-4a8e-97bd-38128985baa7",
        "ResourceInstanceRunningJobInfos": [
            {
                "PodName": "xxx-6fb768c5d5-4fh84",
                "TaskType": "batch",
                "TaskId": "Batch-xxx",
                "TaskName": "批处理任务"
            }
        ]
    }
}
```

