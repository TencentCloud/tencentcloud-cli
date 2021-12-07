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
        "RequestId": "f19fd113-9288-4f1c-9236-9f59828763a9",
        "TaskId": 32401,
        "CreateResult": "Succ"
    }
}
```

