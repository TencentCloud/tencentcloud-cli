**Example 1: 移除 DB Custom 节点的置放群组**



Input: 

```
tccli dbdc DeleteDBCustomNodesDisasterRecoverGroup --cli-unfold-argument  \
    --NodeIds dbcn-gfqtre45 \
    --DisasterRecoverGroupIds dbps-afswz0ux
```

Output: 
```
{
    "Response": {
        "TaskId": 100657,
        "RequestId": "d40006a6-ba3a-403a-88e1-0f6a1c04ba75"
    }
}
```

