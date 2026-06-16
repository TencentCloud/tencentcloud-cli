**Example 1: 从 DB Custom 集群中下架节点**



Input: 

```
tccli dbdc RemoveNodesFromDBCustomCluster --cli-unfold-argument  \
    --ClusterId dbcc-3hvxwggn \
    --NodeIds dbcn-8619etu0
```

Output: 
```
{
    "Response": {
        "TaskId": 66,
        "RequestId": "92118b77-cfaf-4017-bcbf-2a4984ac162b"
    }
}
```

