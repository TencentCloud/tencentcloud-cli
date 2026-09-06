**Example 1: 修改 DB Custom 节点的置放群组**



Input: 

```
tccli dbdc ModifyDBCustomNodesDisasterRecoverGroup --cli-unfold-argument  \
    --NodeIds dbcn-jko09g54 \
    --DisasterRecoverGroupIds dbps-afswz0ux
```

Output: 
```
{
    "Response": {
        "TaskId": 100659,
        "RequestId": "46fa2486-5b43-4947-824d-a1291fbf71c8"
    }
}
```

