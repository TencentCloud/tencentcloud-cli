**Example 1: 获取生产调度任务列表**



Input: 

```
tccli wedata DescribeProdTasks --cli-unfold-argument  \
    --ProjectId 1 \
    --PageNumber 1 \
    --Filters.0.Values tghb98uj23489ufyh \
    --Filters.0.Name tableId \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "4567",
                "TaskName": "上游任务",
                "WorkflowId": "67yughbj89yu08yh"
            }
        ],
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

