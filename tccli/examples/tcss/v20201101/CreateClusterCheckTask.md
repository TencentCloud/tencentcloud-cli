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
        "TaskId": 1,
        "CreateResult": "abc",
        "NewTaskID": "abc",
        "RequestId": "abc"
    }
}
```

