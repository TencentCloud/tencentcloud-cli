**Example 1: 创建集群扫描任务示例**



Input: 

```
tccli tcss CreateClusterCheckTask --cli-unfold-argument  \
    --ClusterCheckTaskList.0.ClusterId cls-0zmsjvko \
    --ClusterCheckTaskList.0.ClusterRegion ap-guangzho
```

Output: 
```
{
    "Response": {
        "CreateResult": "Succ",
        "NewTaskID": "4647204fb0f965430b999ffb1f8d974d",
        "RequestId": "c3a11cce-91df-4fbb-a935-ac85e162c31a",
        "TaskId": 0
    }
}
```

